from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import json
import gradio as gr
import sys
import os


print("init app")

# Opening JSON file
f = open('secret/openai.json')
data = json.load(f)
print(data)

os.environ["OPENAI_API_KEY"] = data["secret"]

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    print("init prompt_helper")
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    print("done")

    print("init llm_predictor")
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
    print("done")

    print("init documents")
    documents = SimpleDirectoryReader(directory_path).load_data()
    print("done")

    print("init index")
    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    print("done")

    print("init saving to disc")
    index.save_to_disk('index.json')
    print("done")

    return index

def chatbot(input_text):
    print("GPTSimpleVectorIndex.load_from_disk")
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    print("init query")
    response = index.query(input_text, response_mode="compact")
    print("done")
    return response.response

print("init iface")
iface = gr.Interface(fn=chatbot,
    inputs=gr.components.Textbox(lines=7, label="Enter your text"),
    outputs="text",
    title="Custom-trained AI Chatbot")
print("done iface")

print("init construct_index")
index = construct_index("docs")
print("done construct_index")

print("launching iface")
iface.launch(server_name="0.0.0.0", server_port=7860)
print("iface launched")

print("done app")

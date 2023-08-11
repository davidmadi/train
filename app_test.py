import gradio as gr

def echo(message, history):
    print(message)
    return message

demo = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot")
print("launching")
demo.launch(server_name="0.0.0.0", server_port=7860)

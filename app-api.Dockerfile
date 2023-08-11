FROM python:3.9.2
WORKDIR /usr/src/app
RUN python -m pip install -U pip

RUN pip install --upgrade pip
RUN pip install openai
RUN pip install gpt_index==0.4.24
RUN pip install langchain==0.0.148
RUN pip install PyPDF2
RUN pip install PyCryptodome
RUN pip install gradio==3.40.1

COPY . .

CMD [ "python", "./app.py" ]
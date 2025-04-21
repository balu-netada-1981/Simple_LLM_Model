import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_openai import ChatOpenAI  
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
## Langchain Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
groq_api_key=os.getenv("GROQ_API_KEY", "")
##Prompt Template
prompt=ChatPromptTemplate.from_messages(
   [
        ("system","You are a helpful assistent. please respond to the question asked"),
        ("user","Question:{question}"),
        ("placeholder", "{conversation}")
    ]
    
)
## streamlit Framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("what question you have in mind")
##ollama gemma model
llm=ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
   st.write(chain.invoke({"question":input_text}))
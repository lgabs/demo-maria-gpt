"""Python file to serve as the frontend"""
import streamlit as st

# check if chromadb was successfully imported
import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# how I am using chroma as a vectorstore
# docsearch = Chroma(
#     persist_directory="embeddings", embedding_function=OpenAIEmbeddings()
# )

# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Maria dos Anjos Demo")
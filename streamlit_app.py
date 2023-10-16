"""Python file to serve as the frontend"""
import streamlit as st

# check if chromadb was successfully imported
# following this troubleshooting https://docs.trychroma.com/troubleshooting#sqlite
# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# how I am using chroma as a vectorstore
# docsearch = Chroma(
#     persist_directory="embeddings", embedding_function=OpenAIEmbeddings()
# )

# the above code loads an already calculated embeddings
# it's breaking in ths part, so let's test it 

print(chromadb.config)

# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Maria dos Anjos Demo")
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def criar_groq(documents, groq_api_key: str):
    
    embeddings = HuggingFaceEmbeddings(model_name="setence-transformers/all-mpnet-base-v2")

    vectordb = FAISS.from_documents(documents, embeddings)

    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    llm = ChatGroq(
        model="groq-3.5-turbo",
        temperature=0,
        groq_api_key=groq_api_key
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False
    )
    return qa_chain
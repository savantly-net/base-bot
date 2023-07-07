"""Create a ConversationalRetrievalChain for question/answering."""
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks.tracers import LangChainTracer
from langchain.chains import ConversationalRetrievalChain
from base_bot.prompts import (REPHRASE_PROMPT, QA_PROMPT)
from langchain.chains.llm import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.vectorstores.base import VectorStore

def get_chain(
    vectorstore: VectorStore, rephrase_handler, stream_handler, tracing: bool = False
) -> ConversationalRetrievalChain:
    manager = BaseCallbackManager([])
    rephrase_manager = BaseCallbackManager([rephrase_handler])
    stream_manager = BaseCallbackManager([stream_handler])
    if tracing:
        tracer = LangChainTracer()
        tracer.load_default_session()
        manager.add_handler(tracer)
        rephrase_manager.add_handler(tracer)
        stream_manager.add_handler(tracer)

    rephrase_generator_llm = OpenAI(
        temperature=0,
        verbose=True,
        callback_manager=rephrase_manager,
    )
    streaming_llm = OpenAI(
        streaming=True,
        callback_manager=stream_manager,
        verbose=True,
        temperature=0,
    )

    rephrase_generator = LLMChain(
        llm=rephrase_generator_llm, prompt=REPHRASE_PROMPT, callback_manager=manager
    )
    doc_chain = load_qa_chain(
        streaming_llm, chain_type="stuff", prompt=QA_PROMPT, callback_manager=manager
    )

    qa = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(),
        combine_docs_chain=doc_chain,
        question_generator=rephrase_generator,
        callback_manager=manager,
    )
    return qa

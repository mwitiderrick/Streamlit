import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Select an Option",
    [
        "Classify Text",
        "Question Answering",
        "Text Generation",
        "Named Entity Recognition",
        "Summarization",
        "Translation",
    ],
)

if option == "Classify Text":
    text = st.text_area(label="Enter text")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Question Answering":
    q_a = pipeline("question-answering")
    context = st.text_area(label="Enter context")
    question = st.text_area(label="Enter question")
    if context and question:
        answer = q_a({"question": question, "context": context})
        st.write(answer)
elif option == "Text Generation":
    text = st.text_area(label="Enter text")
    if text:
        text_generator = pipeline("text-generation")
        answer = text_generator(text)
        st.write(answer)
elif option == "Named Entity Recognition":
    text = st.text_area(label="Enter text")
    if text:
        ner = pipeline("ner")
        answer = ner(text)
        st.write(answer)
elif option == "Summarization":
    summarizer = pipeline("summarization")
    article = st.text_area(label="Paste Article")
    if article:
        summary = summarizer(article, max_length=400, min_length=30)
        st.write(summary)
elif option == "Translation":
    translator = pipeline("translation_en_to_de")
    text = st.text_area(label="Enter text")
    if text:
        translation = translator(text)
        st.write(translation)

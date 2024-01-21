import streamlit as st
from streamlit_extras.streaming_write import write
from streamlit_chat import message

from Gemini import model

st.set_page_config(
    page_title="Chatbot",
    layout="wide",
    page_icon="🗣️",
    menu_items=None,
)

with st.container():
    st.title("Google Gemini Chatbot")
    st.subheader("Just an ordinary bot using Googl's Gemini Pro model API")
    st.divider()


def main():
    with st.chat_message("Gemini"):
        write("Hello, I'm Gemini. How can I help you?")
    chat = model.start_chat(history=[])

    prompt = st.chat_input("Say something")
    if prompt:
        message(prompt, is_user=True)

    if prompt:
        response = chat.send_message(prompt, stream=True)
        with st.chat_message("Gemini"):
            for chunk in response:
                write(chunk.text)


if __name__ == "__main__":
    main()

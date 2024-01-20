import streamlit as st
import requests
import jinja2


st.write("Hello world!")

users = requests.get("http://127.0.0.1:8000/users").json()

st.dataframe(users)

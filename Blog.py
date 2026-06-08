import google.generativeai as genai
import streamlit as st
genai.configure(api_key="YOUR_API_KEY")
model=genai.GenerativeModel("gemini-2.5-flash")
prompt=st.text_input("AI BLOG GENERATOR 🤖")
uh =("You are a AI Blog Post Generator. Generate full blog article from a title. Key features include title, tone control and headings.   ")
if st.button("submit"):
    response = model.generate_content(prompt+uh)
    st.write(response.text)




# py -m pip install streamlit
#py -m pip install google generativeai
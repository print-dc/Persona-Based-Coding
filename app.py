import streamlit as st
from groq import Groq
from langchain_groq import ChatGroq

st.title("Persona-Based Coding Assistant")

# Load API key
groq_api_key = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Fetch available models
models = client.models.list()
model_names = [m.id for m in models.data]

# Dropdown for persona
persona = st.selectbox("Choose Persona:", ["Beginner Mentor", "Code Reviewer", "Bug Fixer"])

# Dropdown for models (auto-populated)
model_choice = st.selectbox("Choose Groq Model:", model_names)

# Temperature slider
temperature = st.slider("Temperature:", 0.0, 1.0, 0.2)

# LLM
llm = ChatGroq(
    model=model_choice,
    groq_api_key=groq_api_key,
    temperature=temperature
)

# User input
user_input = st.text_area("Enter your coding question:")

if st.button("Generate Response"):
    response = llm.invoke(user_input)
    st.write(f"**{persona} Response:**")
    st.write(response.content)
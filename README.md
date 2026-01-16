# Persona-Based-Coding 🚀

A **Streamlit-based AI coding assistant** that responds differently based on selected personas such as **Beginner Mentor**, **Code Reviewer**, and **Bug Fixer**.  
Built using **Groq LLMs** and **LangChain** for fast, low-latency AI responses.

---

## ✨ Features

- 🎭 **Persona-based responses**
  - Beginner Mentor → simple explanations
  - Code Reviewer → structured feedback & best practices
  - Bug Fixer → debugging-focused guidance

- 🎛️ **Model & temperature selection**
- 🖥️ **Clean and interactive Streamlit UI**
- 🔐 **Secure API key handling using `secrets.toml`**

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- Groq API  
- Git & GitHub  

---

## 📂 Project Structure

```text
Persona-Based-Coding/
├── app.py                # Main Streamlit application
├── personas.py           # Persona prompt definitions
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignored files (secrets, cache)
└── .streamlit/
    └── secrets.toml      # API key (not committed)

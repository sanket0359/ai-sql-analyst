# 🤖 AI-Powered Retail Data Analyst

A professional **Generative AI** dashboard that allows users to query a SQL database using Natural Language. Built with **LangChain**, **Groq (Llama 3.3)**, and **Streamlit**, this tool bridges the gap between raw data and business insights.

## 🚀 Key Features
* **Natural Language to SQL:** Converts English questions into complex SQL queries automatically.
* **Interactive Dashboard:** Side-by-side view of the AI chat and a live database preview.
* **Automated Data Pipeline:** Imports raw `data.csv` (Retail Sales) into a structured SQLite database.
* **High Performance:** Powered by Groq’s LPU for sub-second AI response times.

## 🛠️ Tech Stack
* **LLM:** Groq (Llama-3.3-70b-versatile)
* **Framework:** LangChain (SQL Agent)
* **Frontend:** Streamlit
* **Database:** SQLite / SQLAlchemy
* **Data Processing:** Pandas


## 🧠 Challenges & Solutions
* **State Management:** Streamlit is stateless by nature. I used `st.session_state` to store chat history, ensuring a seamless conversation flow.
* **Schema Mapping:** Handled messy CSV headers by implementing a cleaning layer in Pandas before SQL migration.
* **Agent Reliability:** Fine-tuned the LangChain SQL Agent to ensure it only performs "Read" operations, keeping the database safe from accidental deletions.

---
**Developed by Sanket** | Data Analyst Intern 2026 🚀

---


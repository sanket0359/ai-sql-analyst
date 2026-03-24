import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sanket's AI Retail Analyst", 
    page_icon="🛒", 
    layout="wide"
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .stTextInput > div > div > input { border-radius: 10px; }
    .stAlert { border-radius: 10px; }
    [data-testid="stSidebar"] { background-color: #111; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 AI Retail Sales Assistant")
st.markdown("Analyze your Kaggle Sales data using Natural Language.")
st.markdown("---")

# --- SIDEBAR: SETTINGS ---
with st.sidebar:
    st.header("⚙️ Configuration")
    groq_api_key = st.text_input("Groq API Key", type="password", help="Enter your key from console.groq.com")
    
    st.divider()
    st.info("""
    **Dataset Loaded:** `data.csv`
    **Table Name:** `sales`
    
    **Try Asking:**
    - "What is the total revenue by category?"
    - "Who is the customer with the highest purchase?"
    - "Show me average sales per gender."
    """)
    
    if st.button("🔄 Refresh Application"):
        st.rerun()

# --- MAIN APPLICATION LOGIC ---
if groq_api_key:
    try:
        # 1. DATABASE CONNECTION
        # Connecting to the DB created from your CSV
        engine = create_engine("sqlite:///office_data.db")
        db = SQLDatabase(engine)
        
        # 2. INITIALIZE THE LLM (Groq Llama 3)
        llm = ChatGroq(
            model_name="llama-3.3-70b-versatile", 
            groq_api_key=groq_api_key,
            temperature=0
        )

        # 3. CREATE THE AI AGENT
        agent_executor = create_sql_agent(
            llm=llm, 
            db=db, 
            agent_type="openai-tools", 
            verbose=True
        )

        # 4. USER INTERFACE LAYOUT
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("💬 Ask Your Sales Data")
            user_query = st.text_input(
                "Query:", 
                placeholder="e.g., 'Compare total sales between Male and Female customers'"
            )

            if user_query:
                with st.spinner("AI is analyzing your CSV data..."):
                    try:
                        # Running the agent
                        response = agent_executor.invoke({"input": user_query})
                        
                        # Displaying the Answer
                        st.markdown("### 🎯 Analysis Result")
                        st.success(response["output"])
                        
                    except Exception as ai_err:
                        st.error(f"AI Error: {ai_err}")

        with col2:
            st.subheader("📋 CSV Data Preview")
            # CHANGED: Now reading from the 'sales' table created by your new create_db.py
            try:
                df = pd.read_sql("SELECT * FROM sales LIMIT 100", engine)
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.caption("Showing the first 100 rows of your dataset.")
            except Exception as db_err:
                st.error("Table 'sales' not found. Did you run create_db.py?")

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
else:
    st.warning("👈 Please enter your Groq API Key in the sidebar to start.")

# --- FOOTER ---
st.markdown("---")
st.caption("Developed by Sanket | Data Analyst Intern 🚀 | Project: Text-to-SQL for Kaggle Datasets")
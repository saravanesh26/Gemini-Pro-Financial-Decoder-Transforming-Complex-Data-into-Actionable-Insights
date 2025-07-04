from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import streamlit as st

@st.cache_resource
def initialize_llm():
    try:
        api_key = st.secrets["API_KEY"] if "API_KEY" in st.secrets else "-DWMDXKgO7_kM4h0XxM"
        genai.configure(api_key=api_key)
        llm = GoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.7
        )
        return llm
    except Exception as e:
        st.error(f"LLM Init Error: {str(e)}")
        return None

PROMPT_TEMPLATES = {
    "balance_sheet": PromptTemplate(
        input_variables=["balance_sheet_data"],
        template="""
        Analyze the following balance sheet:
        {balance_sheet_data}
        Return key insights.
        """
    ),
    "profit_loss": PromptTemplate(
        input_variables=["profit_loss_data"],
        template="""
        Analyze this profit and loss data:
        {profit_loss_data}
        Provide detailed insights.
        """
    ),
    "cash_flow": PromptTemplate(
        input_variables=["cash_flow_data"],
        template="""
        Analyze this cash flow:
        {cash_flow_data}
        Provide key takeaways.
        """
    )
}

def generate_summary(prompt_type, data, llm):
    try:
        summary_data = data.head(10).to_dict('records')
        prompt = PROMPT_TEMPLATES[prompt_type].format(**{f"{prompt_type}_data": str(summary_data)})
        return llm.invoke(prompt)
    except Exception as e:
        return f"Summary error: {str(e)}"

import streamlit as st
from file_uploader import load_file
from llm_handler import initialize_llm, generate_summary
from visualizer import create_enhanced_visuals

st.set_page_config(
    page_title="Gemini Pro Financial Decoder",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)

# UI Styling
st.markdown("""
<style>
    /* Add minimal layout styling here if needed */
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h1>Gemini Pro Financial Decoder</h1>
    <p>Advanced Financial Analysis with AI-Powered Insights</p>
</div>
""", unsafe_allow_html=True)

# LLM Init
llm = initialize_llm()
if llm is None:
    st.error("Cannot proceed without LLM initialization")
    st.stop()

# Sidebar File Uploads
st.sidebar.header("Upload Financial Documents")
balance_sheet_file = st.sidebar.file_uploader("Balance Sheet", type=["csv", "xlsx", "xls"])
profit_loss_file = st.sidebar.file_uploader("Profit & Loss Statement", type=["csv", "xlsx", "xls"])
cash_flow_file = st.sidebar.file_uploader("Cash Flow Statement", type=["csv", "xlsx", "xls"])

if st.button("Generate Comprehensive Financial Analysis"):
    with st.spinner("Analyzing financial data..."):
        files = {
            'balance_sheet': (balance_sheet_file, 'Balance Sheet'),
            'profit_loss': (profit_loss_file, 'Profit & Loss Statement'),
            'cash_flow': (cash_flow_file, 'Cash Flow Statement')
        }

        for key, (file, name) in files.items():
            if file:
                df = load_file(file)
                if df is not None:
                    summary = generate_summary(key, df, llm)
                    st.subheader(f"{name} Analysis")
                    st.markdown(summary)
                    create_enhanced_visuals(df, name)
        st.success("Analysis complete!")

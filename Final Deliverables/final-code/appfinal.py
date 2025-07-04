import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
from typing import Optional, Dict, Any
import io
import openpyxl

# Configure page settings
st.set_page_config(
    page_title="Gemini Pro Financial Decoder",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS styling
st.markdown("""
<style>
    .stApp {
        background: radial-gradient( #150050 20%, #000000 80% );
    }
    header[data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0); /* Fully transparent */
    }
            
    .main-header {
        background: radial-gradient(#150050 75%);
        padding: 2rem 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(255,255,255,0.3);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #3F0071 0%, #610094 100%); **
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem ;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #fff;
    }
    
    .summary-card {
        background: radial-gradient(135deg, #dba6f3 5%, #3F0071 40%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0);
    }
    
    .upload-section {
        background: linear-gradient(135deg, #e4c0c0 0%, #FB2576 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(255,255,255,10);
    }
            
    [data-testid=stSidebar] {
        background-color: rgba(0, 0, 0, 0.3);
    }

    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #0c31d4 0%, #150050 70%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 2px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(255,255,255,0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    

    
    .error-message {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
        color: #721c24;
        margin: 1rem 0;
    }
    
    .success-message {
        background: linear-gradient(135deg, #a8e6cf 0%, #dcedc1 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        color: #155724;
        margin: 1rem 0;
    }
    
    .data-table {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Configuration
@st.cache_resource
def initialize_llm():
    """Initialize the LLM with error handling"""
    try:
        # Try to get API key from secrets first, then fallback to hardcoded
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
        except:
            # Fallback to the original API key if secrets not available
            api_key = "-DWMDXKgO7_kM4h0XxM"
        
        genai.configure(api_key=api_key)
        
        llm = GoogleGenerativeAI(
            model="gemini-1.5-flash", 
            google_api_key=api_key, 
            temperature=0.7
        )
        return llm
    except Exception as e:
        st.error(f"Failed to initialize LLM: {str(e)}")
        return None

# Enhanced prompt templates with better structure
PROMPT_TEMPLATES = {
    "balance_sheet": PromptTemplate(
        input_variables=["balance_sheet_data"],
        template="""
        As a financial analyst, analyze the following balance sheet data and provide insights:
        
        Data: {balance_sheet_data}
        
        Please provide:
        1. Key financial health indicators
        2. Asset and liability analysis
        3. Liquidity position
        4. Capital structure insights
        5. Notable trends or concerns
        
        Format your response in clear, actionable insights.
        """
    ),
    "profit_loss": PromptTemplate(
        input_variables=["profit_loss_data"],
        template="""
        As a financial analyst, analyze the following profit and loss statement and provide insights:
        
        Data: {profit_loss_data}
        
        Please provide:
        1. Revenue performance analysis
        2. Profitability metrics
        3. Cost structure analysis
        4. Operating efficiency insights
        5. Key performance trends
        
        Format your response in clear, actionable insights.
        """
    ),
    "cash_flow": PromptTemplate(
        input_variables=["cash_flow_data"],
        template="""
        As a financial analyst, analyze the following cash flow statement and provide insights:
        
        Data: {cash_flow_data}
        
        Please provide:
        1. Operating cash flow analysis
        2. Investment activities review
        3. Financing activities assessment
        4. Liquidity and cash management
        5. Cash flow sustainability
        
        Format your response in clear, actionable insights.
        """
    )
}

@st.cache_data
def load_file(file) -> Optional[pd.DataFrame]:
    """Load and validate uploaded files with enhanced error handling"""
    if file is None:
        return None
    
    try:
        file_content = file.read()
        file.seek(0)  # Reset file pointer
        
        if file.name.endswith('.csv'):
            df = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
        elif file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(io.BytesIO(file_content))
        else:
            st.error("Unsupported file format. Please upload CSV or Excel files.")
            return None
        
        # Basic data validation
        if df.empty:
            st.warning(f"The uploaded file '{file.name}' is empty.")
            return None
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        return df
    
    except Exception as e:
        st.error(f"Error loading file '{file.name}': {str(e)}")
        return None

def generate_summary(prompt_type: str, data: pd.DataFrame, llm) -> str:
    """Generate AI summary with enhanced error handling"""
    if data is None or llm is None:
        return "Error: No data provided or LLM not initialized."
    
    try:
        # Convert DataFrame to a more readable format
        data_summary = {
            'shape': data.shape,
            'columns': data.columns.tolist(),
            'sample_data': data.head(10).to_dict('records'),
            'summary_stats': data.describe().to_dict() if len(data.select_dtypes(include=['number']).columns) > 0 else {}
        }
        
        prompt = PROMPT_TEMPLATES[prompt_type].format(**{f"{prompt_type}_data": str(data_summary)})
        response = llm.invoke(prompt)
        return response
    
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def create_enhanced_visuals(data: pd.DataFrame, title: str, chart_type: str = "auto"):
    """Create enhanced visualizations with Plotly"""
    if data is None or data.empty:
        st.warning(f"No data available for {title}")
        return
    
    st.markdown(f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <p>Data Shape: {data.shape[0]} rows × {data.shape[1]} columns</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display data table with styling
    with st.expander(f"View {title} Data Table", expanded=False):
        st.markdown('<div class="data-table">', unsafe_allow_html=True)
        st.dataframe(data, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Get numeric columns for visualization
    numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
    
    if not numeric_cols:
        st.info(f"No numeric data found in {title} for visualization.")
        return
    
    # Create visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        if len(numeric_cols) >= 2:
            # Line chart for trends
            fig_line = px.line(
                data, 
                y=numeric_cols[:5],  # Limit to first 5 numeric columns
                title=f"{title} - Trend Analysis",
                template="plotly_white"
            )
            fig_line.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333333'),
                showlegend=True
            )
            st.plotly_chart(fig_line, use_container_width=True)
    
    with col2:
        if len(numeric_cols) >= 1:
            # Bar chart
            fig_bar = px.bar(
                data.head(10), 
                y=numeric_cols[0],
                title=f"{title} - Top 10 Values",
                template="plotly_white",
                color=numeric_cols[0],
                color_continuous_scale="Viridis"
            )
            fig_bar.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333333')
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    
    # Additional summary statistics
    if len(numeric_cols) > 0:
        st.markdown("### 📈 Statistical Summary")
        summary_stats = data[numeric_cols].describe()
        st.dataframe(summary_stats, use_container_width=True)

def main():
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>Gemini Pro Financial Decoder</h1>
        <p>Advanced Financial Analysis with AI-Powered Insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize LLM
    llm = initialize_llm()
    
    if llm is None:
        st.error("Cannot proceed without proper LLM initialization. Please check your API key.")
        return
    
    # Sidebar for file uploads
    with st.sidebar:
        st.markdown("""
        <div class="upload-section">
            <h3>Upload Financial Documents</h3>
            <p>Upload your financial statements in CSV or Excel format</p>
        </div>
        """, unsafe_allow_html=True)
        
        balance_sheet_file = st.file_uploader(
            "Balance Sheet", 
            type=["csv", "xlsx", "xls"],
            help="Upload your balance sheet data"
        )
        
        profit_loss_file = st.file_uploader(
            "Profit & Loss Statement", 
            type=["csv", "xlsx", "xls"],
            help="Upload your P&L statement"
        )
        
        cash_flow_file = st.file_uploader(
            "Cash Flow Statement", 
            type=["csv", "xlsx", "xls"],
            help="Upload your cash flow statement"
        )
        
        # Analysis options
        st.markdown("### Analysis Options")
        include_detailed_charts = st.checkbox("Include Detailed Charts", value=True)
        analysis_depth = st.selectbox("Analysis Depth", ["Standard", "Detailed", "Executive Summary"])
    
    # Main content area
    files_uploaded = any([balance_sheet_file, profit_loss_file, cash_flow_file])
    
    if not files_uploaded:
        st.markdown("""
        <div class="summary-card">
            <h3>Welcome to Financial Decoder</h3>
            <p>Upload your financial statements using the sidebar to get started with AI-powered analysis!</p>
            <ul>
                <li>Balance Sheet Analysis</li>
                <li>Profit & Loss Insights</li>
                <li>Cash Flow Assessment</li>
                <li>Interactive Visualizations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Generate reports button
    if st.button("Generate Comprehensive Financial Analysis", type="primary"):
        with st.spinner("Analyzing financial data and generating insights..."):
            
            # Process each file
            files_data = {
                'balance_sheet': (balance_sheet_file, 'Balance Sheet'),
                'profit_loss': (profit_loss_file, 'Profit & Loss Statement'),
                'cash_flow': (cash_flow_file, 'Cash Flow Statement')
            }
            
            results = {}
            
            for file_type, (file_obj, display_name) in files_data.items():
                if file_obj is not None:
                    # Load data
                    data = load_file(file_obj)
                    
                    if data is not None:
                        # Generate AI summary
                        summary = generate_summary(file_type, data, llm)
                        results[file_type] = {'data': data, 'summary': summary, 'name': display_name}
                        
                        # Display results
                        st.markdown(f"## {display_name} Analysis")
                        
                        # AI Summary
                        st.markdown(f"""
                        <div class="summary-card">
                            <h4>AI-Generated Insights</h4>
                            <p>{summary}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Visualizations
                        if include_detailed_charts:
                            create_enhanced_visuals(data, display_name)
                        
                        st.markdown("---")
            
            # Overall summary if multiple files processed
            if len(results) > 1:
                st.markdown("## Executive Summary")
                st.markdown("""
                <div class="summary-card">
                    <h4>Overall Financial Health</h4>
                    <p>Based on the uploaded financial statements, here's a comprehensive overview of the financial position.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Create summary metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Documents Analyzed", len(results))
                
                with col2:
                    total_data_points = sum(data['data'].shape[0] * data['data'].shape[1] for data in results.values())
                    st.metric("Total Data Points", f"{total_data_points:,}")
                
                with col3:
                    st.metric("Analysis Complete", "100%")
            
            # Success message
            st.markdown("""
            <div class="success-message">
                <h4>Analysis Complete!</h4>
                <p>Your financial analysis has been generated successfully. Review the insights above for key findings and recommendations.</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

import pandas as pd
import streamlit as st
import io

def load_file(file):
    if file is None:
        return None
    try:
        content = file.read()
        file.seek(0)
        if file.name.endswith('.csv'):
            df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        elif file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(io.BytesIO(content))
        else:
            st.error("Unsupported format")
            return None
        if df.empty:
            st.warning("File is empty")
            return None
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"File load error: {str(e)}")
        return None

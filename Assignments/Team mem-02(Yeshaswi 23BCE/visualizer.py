import streamlit as st
import plotly.express as px

def create_enhanced_visuals(data, title):
    if data is None or data.empty:
        st.warning("No data to visualize")
        return

    st.subheader(f"{title} Visualizations")

    numeric_cols = data.select_dtypes(include='number').columns.tolist()
    if not numeric_cols:
        st.info("No numeric columns to plot")
        return

    fig = px.line(data, y=numeric_cols[:3], title=f"{title} Trends")
    st.plotly_chart(fig, use_container_width=True)

    fig_bar = px.bar(data.head(10), y=numeric_cols[0], title=f"Top 10 {numeric_cols[0]}")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.write("Statistical Summary")
    st.dataframe(data[numeric_cols].describe())

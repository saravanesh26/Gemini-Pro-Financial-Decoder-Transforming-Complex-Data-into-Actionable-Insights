
# Gemini-Pro-Financial-Decoder - Transforming Complex Data into Actionable Insights

## Team Members
- Saravanesh 23BCE8183 (Team Leader)  
- Nicholas 23BCE8212  
- Yeshaswi 23BCE8200  
- Vardhan 23BCE8186  

## Details
**Doc Ver**: 1.0  

---

## 📊 Gemini Pro Financial Decoder

Transform your financial analysis with AI-powered insights and interactive visualizations.

An intelligent financial analysis tool that leverages Google's Gemini Pro LLM to automatically analyze balance sheets, profit & loss statements, and cash flow data. Built with Streamlit for an intuitive web interface and modular architecture for easy maintenance.

---

## ✨ Features

- 🤖 **AI-Powered Analysis** – Google Gemini Pro generates intelligent financial insights  
- 📊 **Interactive Visualizations** – Beautiful charts and graphs  
- 📁 **Multi-Format Support** – Upload CSV and Excel files seamlessly  
- 🔍 **Comprehensive Reports** – Balance Sheet, P&L, and Cash Flow analysis  
- ⚡ **Real-time Processing** – Get insights in seconds  
- 🛡️ **Secure** – Files processed in memory only  

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key (Gemini Pro)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/gemini-financial-decoder.git
cd gemini-financial-decoder

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export GOOGLE_API_KEY="your_api_key_here"

# Run the application
streamlit run app.py
```

---

## 📁 Project Structure

```
gemini-financial-decoder/
├── app.py               # Main Streamlit application
├── file_uploader.py     # File processing module
├── llm_handler.py       # LLM integration and prompt handling
├── visualizer.py        # Data visualization components
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🔧 Core Components

### Main Application (`app.py`)
- Streamlit configuration with wide layout and expandable sidebar
- File Upload Interface: Supports Balance Sheet, P&L, and Cash Flow statements
- Processing pipeline for coordinating file loading, AI analysis, and visualization
- Graceful error handling

### Key Functions
- `initialize_llm()`: Sets up Google Gemini Pro connection  
- `load_file()`: Processes uploaded CSV/Excel files  
- `generate_summary()`: Creates AI-powered financial insights  
- `create_enhanced_visuals()`: Generates interactive charts and graphs  

---

## 💡 Usage

1. Upload financial documents via the sidebar  
2. Click **"Generate Comprehensive Financial Analysis"**  
3. Review AI-generated insights and interactive visuals  
4. Export or save your results  

---

## 📊 Supported File Types

- `.csv`  
- `.xlsx`, `.xls`

---

## 🎯 Analysis Types

- **Balance Sheet**: Financial health, assets/liabilities analysis  
- **Profit & Loss**: Revenue trends, profitability  
- **Cash Flow**: Liquidity, cash management metrics  

---

## 🛠️ Technical Architecture

```
┌─────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Streamlit   │────│ File Uploader   │────│ Data Processor  │
│ Interface   │    │ Module          │    │ (Pandas)        │
└─────────────┘    └─────────────────┘    └─────────────────┘
       │                    │                       │
       ▼                    ▼                       ▼
┌─────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Visualizer  │    │ LLM Handler     │    │ Google Gemini   │
│ (Plotly)    │    │ (LangChain)     │    │ Pro API         │
└─────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🔒 Security Features

- No data persistence: Files processed in-memory  
- Secure API key handling via environment variables  
- Input validation for file type and content  
- Session isolation for multi-user safety  

---

## 🚀 Performance

- ⏱️ Analysis completion within 30 seconds  
- 📁 Supports file sizes up to 50MB  
- 👥 Optimized for concurrent users  
- 🧠 Efficient memory usage  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
```bash
git checkout -b feature/amazing-feature
```
3. Commit your changes  
```bash
git commit -m "Add amazing feature"
```
4. Push to GitHub  
```bash
git push origin feature/amazing-feature
```
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 🆘 Support

- 📖 **Documentation**: Check the Wiki  
- 🐞 **Issues**: Report bugs or feature requests  
- 💬 **Discussions**: Join the community  

---

## 🙏 Acknowledgments

- Google – Gemini Pro LLM API  
- Streamlit – For intuitive app development  
- Plotly – For advanced interactive visualizations  
- Open-source community  

---

Made with ❤️ for financial professionals and business owners.  
**Transform your financial analysis workflow with the power of AI.**

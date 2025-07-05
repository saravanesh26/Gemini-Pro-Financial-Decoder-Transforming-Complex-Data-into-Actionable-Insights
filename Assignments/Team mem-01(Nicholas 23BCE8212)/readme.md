# File Uploader Module

**Team Member 01 - Assignment Submission**

## Overview

The `file_uploader.py` module handles file uploads and parsing for the [Gemini Pro Financial Decoder](https://github.com/saravanesh26/Gemini-Pro-Financial-Decoder-Transforming-Complex-Data-into-Actionable-Insights/tree/main) project.

## Features

- Supports CSV and Excel files (.csv, .xlsx, .xls)
- Data validation and error handling
- Automatic header cleaning
- Streamlit integration

## Installation

```bash
pip install pandas streamlit
```

## Usage

```python
from file_uploader import load_file

# In Streamlit app
uploaded_file = st.file_uploader("Upload File", type=['csv', 'xlsx', 'xls'])
df = load_file(uploaded_file)
```

## Function Reference

### `load_file(file)`
- **Input**: File object from Streamlit uploader
- **Output**: pandas DataFrame or None
- **Features**: Format detection, encoding handling, data cleaning

## Error Handling

- Unsupported format warnings
- Empty file detection
- Parsing error messages
- File pointer reset

## File Structure

```
assignments/team_member_01/
├── file_uploader.py
├── file_uploader_documentation.pdf
└── README.md
```

## Integration

Works with:
- `app.py` - Main application
- LLM Handler - AI processing
- Visualizer - Chart generation

## Assignment Deliverables

- ✅ Module implementation
- ✅ PDF documentation
- ✅ README file
- ✅ Error handling system

---

**Team Member 01 - Module Development**  
*Gemini Pro Financial Decoder Project*

def load_css():
    return """
    <style>
        .stApp {
            background: radial-gradient(#150050 20%, #000000 80%);
        }
        header[data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0);
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
            background: linear-gradient(135deg, #3F0071 0%, #610094 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem;
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
    """

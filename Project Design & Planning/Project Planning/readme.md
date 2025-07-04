👥 Team Responsibilities
A clear division of labor is crucial for efficient project execution. Each team member will be assigned specific modules and responsibilities, fostering ownership and specialized expertise:

•	Team Lead (Saravanesh 23BCE8183)
(LLM Configuration + Prompt Generation) - llm_handler.py
o	Responsibilities: Focuses on optimizing the interaction with the Gemini Pro model. This includes crafting effective prompts to elicit accurate and insightful financial analyses, managing API calls, and handling model responses. Explores techniques for context window management and error handling specific to the LLM.
o	Key Deliverables: llm_handler.py, prompt templates, AI response parsing logic.
(CSS Modularization) - styles.py
o	Responsibilities: Dedicated to creating a polished and consistent visual experience. This involves writing custom CSS to style all Streamlit components, ensuring responsiveness, defining color palettes, typography, and spacing for a premium look and feel. Will work closely with the Team Lead on UI/UX design.
o	Key Deliverables: styles.py, custom CSS rules, potentially a UI/UX style guide.

•	Member 01 (Nicholas 23BCE8212)
(File Reading, Error Handling) - file_uploader.py
o	Responsibilities: Develops the robust file upload component. This involves implementing secure file reading for .csv and .xlsx formats using Pandas, performing initial data validation (e.g., checking for expected columns, data types), and comprehensive error handling for malformed or unsupported files.
o	Key Deliverables: file_uploader.py, data loading functions, data validation rules.


•	Member 02 (Yeshaswi 23BCE8200)
(Data Visualization) - visualizer.py
o	Responsibilities: Designs and implements all interactive financial visualizations using Plotly. This role requires an understanding of how to effectively represent financial data graphically to highlight trends and key metrics. Responsible for generating various chart types based on the processed data.
o	Key Deliverables: visualizer.py, Plotly chart generation functions, interactive dashboard components

•	Member 03 (Vardhan 23BCE8186)
(Main Logic, Streamlit Layout) - app.py
o	Responsibilities: Overall project coordination, defining the application's flow and user journey. Orchestrates the integration of all modules. Designs the main Streamlit layout and ensures seamless transitions between different views. Handles core data passing between components and manages session state.
o	Key Deliverables: app.py (main application file), project structure, integration testing.


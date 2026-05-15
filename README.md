Vender Agreement Review

*Project Overview*

The Vender Agreement Rewiew Prototype is a Python Streamlit application designed for internal legal operations. It helps users upload vender agreement and automatically extract important clauses, agreement details, and risk-related information

*Features*

# Upload agreements in PDF, DOCX, or TXT format
# Extract document text automatically
# Detect important clauses using regex and keyword matching
# Generate summaries of agreements
# Store processed review data in JSON format
# Simple and user-friendly Streamlit interface

*Technologies Used*

# Python
# Streamlit
# pdfplumber / PyMuPDF
# python-docx
# Regex & keyword-based logic
# JSON for data storage

*Project Structure*
vendor_agreement_review/
│── app.py                 # Main Streamlit app
│── extractor.py           # Extracts text from files
│── clause_detector.py     # Detects important clauses
│── summarizer.py          # Creates agreement summaries
│── utils.py               # Helper functions
│── output/
│   └── processed_reviews.json
│── requirements.txt


*Installation*

# pip install -r requirement.txt #

*Run the application*

# streamlit run app.py #



*Purpose*
This project reduces manual effort in reviewing vendor agreements and helps legal teams quickly identify important contractual information.
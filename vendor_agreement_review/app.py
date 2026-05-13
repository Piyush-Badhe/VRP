import streamlit as st
import pandas as pd

from extractor import extract_text
from clause_detector import (
    detect_clauses,
    extract_effective_date,
    generate_flags
)

from summarizer import generate_summary
from utils import save_review_output


st.set_page_config(
    page_title="Vendor Agreement Review Prototype",
    layout="wide"
)


st.title("Vendor Agreement Review Prototype")


st.sidebar.header("Upload Agreement")

uploaded_file = st.sidebar.file_uploader(
    "Choose Agreement File",
    type=["pdf", "docx", "txt"]
)


if uploaded_file:

    with st.spinner("Processing agreement..."):

        extracted_text = extract_text(uploaded_file)

        clause_results = detect_clauses(extracted_text)

        effective_date = extract_effective_date(extracted_text)

        flags = generate_flags(clause_results)

        summary = generate_summary(
            uploaded_file.name,
            effective_date,
            clause_results,
            flags
        )

        output_payload = {
            "document_name": uploaded_file.name,
            "effective_date": effective_date,
            "clauses": clause_results,
            "flags": flags,
            "summary": summary
        }

        save_review_output(output_payload)

    st.success("Agreement processed successfully")

    st.subheader("Document Overview")

    col1, col2, col3 = st.columns(3)

    found_count = len([
        item for item in clause_results
        if item["status"] == "Found"
    ])

    missing_count = len([
        item for item in clause_results
        if item["status"] == "Missing"
    ])

    col1.metric("Document", uploaded_file.name)
    col2.metric("Clauses Found", found_count)
    col3.metric("Missing Clauses", missing_count)

    st.markdown("---")

    st.subheader("Extracted Details")

    st.write(f"**Effective Date:** {effective_date}")

    st.markdown("---")

    st.subheader("Clause Review Table")

    table_data = []

    for item in clause_results:
        table_data.append({
            "Clause": item["clause"],
            "Status": item["status"],
            "Snippet": item["snippet"]
        })

    clause_df = pd.DataFrame(table_data)

    st.dataframe(
        clause_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Flagged Review Items")

    if flags:
        for flag in flags:
            st.warning(flag)
    else:
        st.success("No major review concerns detected.")

    st.markdown("---")

    st.subheader("Internal Review Summary")

    st.text_area(
        "Summary",
        summary,
        height=250
    )

else:
    st.info("Upload an agreement document to begin review.")
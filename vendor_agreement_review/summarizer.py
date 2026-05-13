def generate_summary(document_name, effective_date, clause_results, flags):
    found_count = len(
        [item for item in clause_results if item["status"] == "Found"]
    )

    missing_count = len(
        [item for item in clause_results if item["status"] == "Missing"]
    )

    summary = f"""
Document Review Summary

The agreement document '{document_name}' was processed successfully.

The detected effective date is: {effective_date}.

A total of {found_count} key legal and operational clauses were identified,
while {missing_count} clauses require additional manual review.

Key review observations:
"""

    if flags:
        for flag in flags:
            summary += f"\n- {flag}"

    else:
        summary += "\n- No major clause gaps were identified."

    summary += """

This review was generated using automated clause detection logic and should
be validated by the legal operations team before final approval.
"""

    return summary.strip()
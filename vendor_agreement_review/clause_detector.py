import re


CLAUSE_PATTERNS = {
    "Effective Date": [
        r"effective date[:\s].{0,50}",
        r"commencement date[:\s].{0,50}"
    ],

    "Agreement Term": [
        r"term of (this )?agreement.{0,100}",
        r"agreement shall remain in effect.{0,100}"
    ],

    "Renewal Clause": [
        r"automatic renewal.{0,100}",
        r"renewed for successive.{0,100}"
    ],

    "Termination": [
        r"terminate.{0,100}",
        r"termination for cause.{0,100}"
    ],

    "Payment Terms": [
        r"payment terms.{0,100}",
        r"invoice shall be paid.{0,100}"
    ],

    "Confidentiality": [
        r"confidential information.{0,100}",
        r"non-disclosure.{0,100}"
    ],

    "Limitation of Liability": [
        r"limitation of liability.{0,120}",
        r"liable for indirect damages.{0,120}"
    ],

    "Governing Law": [
        r"governed by the laws of.{0,100}",
        r"governing law.{0,100}"
    ],

    "Data Security": [
        r"data security.{0,120}",
        r"security controls.{0,120}",
        r"data protection.{0,120}"
    ],

    "Service Level": [
        r"service level.{0,120}",
        r"uptime commitment.{0,120}",
        r"response time.{0,120}"
    ]
}


def detect_clauses(text):
    results = []

    normalized_text = text.lower()

    for clause_name, patterns in CLAUSE_PATTERNS.items():
        clause_found = False
        snippet = ""

        for pattern in patterns:
            match = re.search(pattern, normalized_text, re.IGNORECASE)

            if match:
                clause_found = True

                start = max(match.start() - 80, 0)
                end = min(match.end() + 120, len(text))

                snippet = text[start:end].replace("\n", " ")
                break

        results.append({
            "clause": clause_name,
            "status": "Found" if clause_found else "Missing",
            "snippet": snippet
        })

    return results


def extract_effective_date(text):
    patterns = [
        r"effective date[:\s]+([A-Za-z0-9,\s]+)",
        r"dated[:\s]+([A-Za-z0-9,\s]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return "Not identified"


def generate_flags(clause_results):
    flags = []

    for item in clause_results:
        if item["status"] == "Missing":
            flags.append(f"{item['clause']} clause not identified.")

    return flags
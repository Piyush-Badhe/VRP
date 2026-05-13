import json
import os


OUTPUT_FILE = "output/processed_reviews.json"


def save_review_output(data):
    os.makedirs("output", exist_ok=True)

    existing_data = []

    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as file:
            try:
                existing_data = json.load(file)
            except Exception:
                existing_data = []

    existing_data.append(data)

    with open(OUTPUT_FILE, "w") as file:
        json.dump(existing_data, file, indent=4)
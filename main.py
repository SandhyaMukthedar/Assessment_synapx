import json
from extractor import extract_fnol_data
from router import route_claim
from utils import get_missing_fields

INPUT_FILE = "sample_docs/sample_fnol.txt"
OUTPUT_FILE = "output/result.json"

def main():
    with open(INPUT_FILE, "r") as file:
        text = file.read()

    extracted_data = extract_fnol_data(text)
    missing_fields = get_missing_fields(extracted_data)

    routed_to, reason = route_claim(extracted_data, text)

    result = {
        "extracted_data": extracted_data,
        "missing_fields": missing_fields,
        "routed_to": routed_to,
        "reason": reason
    }

    print(json.dumps(result, indent=4))

    with open(OUTPUT_FILE, "w") as file:
        json.dump(result, file, indent=4)

if __name__ == "__main__":
    main()
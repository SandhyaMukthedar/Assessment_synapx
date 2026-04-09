import re

def extract_fnol_data(text: str) -> dict:
    data = {}

    patterns = {
        # Policy Information
        "policy_number": r"Policy Number[:\-]?\s*(\w+)",
        "policyholder_name": r"Policyholder Name[:\-]?\s*([A-Za-z ]+)",
        "effective_dates": r"Effective Dates[:\-]?\s*([\w\s\-\/]+)",

        # Incident Information
        "incident_date": r"Date[:\-]?\s*([\d\-\/]+)",
        "incident_time": r"Time[:\-]?\s*([\d:APMapm ]+)",
        "location": r"Location[:\-]?\s*([A-Za-z ,]+)",
        "description": r"(?:Description|Details)[:\-]?\s*(.+)",

        # Involved Parties
        "claimant": r"Claimant[:\-]?\s*([A-Za-z ]+)",
        "third_parties": r"Third Parties[:\-]?\s*([A-Za-z ,]+)",
        "contact_details": r"Contact[:\-]?\s*([\d+ ]+)",

        # Asset Details
        "asset_type": r"Asset Type[:\-]?\s*([A-Za-z ]+)",
        "asset_id": r"Asset ID[:\-]?\s*(\w+)",
        "estimated_damage": r"Estimated Damage[:\-]?\s*(\d+)",

        # Other Mandatory Fields
        "claim_type": r"Claim Type[:\-]?\s*([A-Za-z ]+)",
        "attachments": r"Attachments[:\-]?\s*(Yes|No)",
        "initial_estimate": r"Initial Estimate[:\-]?\s*(\d+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        data[key] = match.group(1).strip() if match else None

    return data
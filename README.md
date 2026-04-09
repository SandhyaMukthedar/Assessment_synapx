# FNOL Automation Assignment

## Overview
This project processes an FNOL (First Notice of Loss) document by extracting key information and routing the insurance claim based on defined business rules. The solution simulates a real-world claim intake and triaging system.

## Features
- Extracts structured data from unstructured text using regular expressions  
- Identifies missing or incomplete fields  
- Applies rule-based logic for claim routing  
- Detects potential fraud-related keywords  
- Outputs results in structured JSON format  

## Tech Stack
- Python  
- Regular Expressions (re module)  
- JSON  

## Project Structure
assessment-2/
├── main.py  
├── extractor.py  
├── router.py  
├── utils.py  
├── sample_docs/  
│   └── sample_fnol.txt  
└── output/  

## How to Run
1. Navigate to the project directory  
   cd assessment-2  

2. Run the application  
   python main.py  

## Sample Output
{
    "extracted_data": {
        "policy_number": "POL12345",
        "policyholder_name": "Ramesh Kumar",
        "effective_dates": "01-01-2025 to 31-12-2025",
        "incident_date": "12-01-2025",
        "incident_time": "10:30 AM",
        "location": "Bangalore",
        "description": "Minor accident",
        "claimant": "Ramesh Kumar",
        "third_parties": "Suresh",
        "contact_details": "9876543210",
        "asset_type": "Car",
        "asset_id": "KA01AB1234",
        "estimated_damage": "20000",
        "claim_type": "Accident",
        "attachments": "Yes",
        "initial_estimate": "20000"
    },
    "missing_fields": [],
    "routed_to": "fast_track"
}

## Business Rules Implemented
- Missing required fields are routed to manual review  
- Fraud-related keywords are routed for investigation  
- Injury-related cases are routed to a specialist team  
- Claims with amount less than 25,000 are fast-tracked  
- Claims are routed based on incident type (accident, theft, fire)  

## Notes
- Modular structure improves readability and maintainability  
- Designed to be easily extendable for additional rules  
- Handles incomplete and varied input formats effectively
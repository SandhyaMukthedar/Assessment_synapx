from typing import Tuple, Dict

def route_claim(data: Dict, text: str) -> Tuple[str, str]:

    text_lower = text.lower()

    # Missing fields
    missing_fields = [k for k, v in data.items() if not v]
    if missing_fields:
        return "manual_review", "Missing required fields"

    # Fraud detection
    if any(word in text_lower for word in ["fraud", "fake", "suspicious"]):
        return "investigation", "Fraud-related keywords detected"

    # Injury detection (fix for 'no injury')
    if "injury" in text_lower and "no injury" not in text_lower:
        return "specialist_team", "Injury detected"

    # Claim amount check
    estimate = data.get("initial_estimate") or data.get("estimated_damage")
    if estimate:
        try:
            if int(estimate) < 25000:
                return "fast_track", "Low claim amount (<25000)"
        except:
            pass

    # Claim type routing
    claim_type = (data.get("claim_type") or "").lower()

    if "accident" in claim_type:
        return "auto_claims", "Accident claim"
    elif "theft" in claim_type:
        return "theft_claims", "Theft claim"
    elif "fire" in claim_type:
        return "fire_claims", "Fire claim"

    return "manual_review", "Default fallback"
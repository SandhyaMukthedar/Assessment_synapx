def get_missing_fields(data: dict) -> list:
    return [key for key, value in data.items() if not value]
import uuid

def generate_api_key() -> str:
    return uuid.uuid4().hex
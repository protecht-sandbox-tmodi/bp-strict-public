import hashlib

def fingerprint(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()

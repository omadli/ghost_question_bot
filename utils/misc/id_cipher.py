

def cipher(user_id: int) -> str:
    return hex(user_id)[2:][::-1]


def decipher(code: str) -> int:
    return int(code[::-1], 16)

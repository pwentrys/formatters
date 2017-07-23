BEGINS = ['.git', '.idea', '.vs']
CONTAINS = ['__pycache__']
ENDS = ['routes.py']


def allowed(string: str) -> bool:
    for begins in BEGINS:
        if string.startswith(begins):
            return False

    for contains in CONTAINS:
        if string.__contains__(contains):
            return False

    for ends in ENDS:
        if string.endswith(ends):
            return False

    return True

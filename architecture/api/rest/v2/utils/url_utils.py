

class UrlUtils:
    def __init__(self):
        pass

    @staticmethod
    def join_path(base: str, path: str) -> str:
        base = base.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"


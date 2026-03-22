import hashlib

class Hasher():
    @staticmethod
    def to_md5(text:str):
        bytes = text.encode("utf-8")
        hash = hashlib.md5(bytes).hexdigest()
        return hash

hasher = Hasher()
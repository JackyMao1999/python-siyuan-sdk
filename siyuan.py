class SiYuan():
    def __init__(self, sy_ip:str, sy_port:str, sy_token:str) -> None:
        self.url = f"http://{sy_ip}:{sy_port}"
        self.token = sy_token
        self.headers = {"Authorization":f"Token {sy_token}"}


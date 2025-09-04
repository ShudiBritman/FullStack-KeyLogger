import socket
import requests
from iwriter import IWriter

class NetworkWriter(IWriter):
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.machine_name = socket.gethostname()

    def send_data(self, data: str, machine_name: str) -> None:
        payload = {
            "machine": machine_name,
            "data": data
        }
        try:
            response = requests.post(self.server_url, json=payload, timeout=5)
            response.raise_for_status()
            print(f"[NetworkWriter] Data sent to {self.server_url} for {machine_name}")
        except Exception as e:
            print(f"[NetworkWriter] Error sending data: {e}")
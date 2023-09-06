import requests
import os


class Banxico:
    def __init__(self):
        self.base_url = os.environ.get("BANXICO_BASEURL")
        self.token = os.environ.get("BANXICO_TOKEN")
        self.headers = {"Bmx-Token": self.token, "Accept": "application/json"}

    def banxico_get_series_datos(self, serie):
        try:
            response = requests.request(
                "GET", f"{self.base_url}/series/{serie}/datos", headers=self.headers
            )
            return response
        except Exception as e:
            # TODO: Log Error
            raise Exception(f"Error in banxico_get_series_datos: {e}")

    def banxico_get_series_datos_oportuno(self, serie):
        try:
            response = requests.request(
                "GET",
                self.base_url + "/series/" + serie + "/datos/oportuno",
                headers=self.headers,
            )
            return response
        except Exception as e:
            # TODO: Log Error
            raise Exception(f"Error in banxico_get_series_datos_oportuno: {e}")

    @staticmethod
    def get_series() -> dict:
        series = {
            "Fix Dollar": "SF43718",
            "UDIS": "SP68257",
            "Cetes 28 Dias": "SF60633",
            "Dollar": "SF60653",
            "Euro": "SF46410",
            "Yen Japones": "SF46406",
            "Libra Esterlina": "SF46407",
            "Dólar Canadiense": "SF60632",
            "Reservas Internacionales": "SF43707",
        }
        return series

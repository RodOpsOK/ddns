import requests
import yaml

class Tools:

    def getIp(self, get_ip_from):
        try:
            response = requests.get(get_ip_from, timeout=5)
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            print(f"[!] Помилка запиту до {get_ip_from}: {e}")
            return exit()

    def getYaml(self, filename) -> dict:
        with open(filename, "r") as f:
            config = yaml.safe_load(f)
        return config

    def setYaml(self, filename, param, value):
        config = self.getYaml(filename)
        config[param] = value
        with open(filename, "w") as f:
            res = yaml.dump(config, f, sort_keys=False)
        return res
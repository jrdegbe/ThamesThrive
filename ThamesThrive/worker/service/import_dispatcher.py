import requests


class ImportDispatcher:

    def __init__(self, credentials, importer, webhook_url: str):
        self.importer = importer
        self.webhook_url = webhook_url
        self.credentials = credentials

    def run(self, ThamesThrive_api_url):
        if ThamesThrive_api_url[-1] == '/':
            ThamesThrive_api_url = ThamesThrive_api_url[:-1]
        for data, progress, batch in self.importer.data(self.credentials):
            url = f"{ThamesThrive_api_url}{self.webhook_url}"
            response = requests.post(url, json=data, verify=False)
            print(url, response.json())
            yield progress, batch


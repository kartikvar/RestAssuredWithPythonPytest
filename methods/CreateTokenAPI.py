import requests

from Configurations.readConfigurations import readConfig
from TestData.CreateTokenData import create_token_valid_data, create_token_invalid_data


class CreateTokenAPI:

    create_token_url = readConfig()["app_url"]["base_url"] + readConfig()["end_points"]["create_token"]

    def method_create_token_with_valid_credentials(self):
        flag = True
        response = requests.post(url=self.create_token_url, json=create_token_valid_data, verify=False)
        if response.status_code != 200:
            if "token" not in response.json():
                flag = False
        return flag

    def method_create_token_with_invalid_credentials(self):
        flag = True
        response = requests.post(url=self.url, json=create_token_invalid_data, verify=False)
        if response.status_code == 200:
            if "token" in response.json():
                flag = False
        return flag

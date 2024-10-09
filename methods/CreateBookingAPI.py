import json

import requests

from Configurations.readConfigurations import readConfig
from TestData.CreateBookingData import create_booking_valid_data, create_booking_invalid_data
from utilities.GetDataFromJSON import GetDataFromJSON


class CreateBookingAPI:

    create_booking_url = readConfig()["app_url"]["base_url"] + readConfig()["end_points"]["create_booking"]
    json_path = "D:\\Learn_SDET\\Rest Assured\\Learn_RestAssured_SDET\\Codes\\RestAssured_Framework_Python_Pytest\\RestAssuredWithPythonPytest\\TestData\\CreateBookingMultipleData.json"


    def method_create_booking_with_valid_data(self):
        flag = True
        response = requests.post(url=self.create_booking_url, json=create_booking_valid_data, verify=False)
        if response.status_code != 200:
            if "bookingid" not in response.json():
                if response.json()["booking"]["firstname"] != "Swapnil":
                    if response.json()["booking"]["lastname"] != "Rawat":
                        flag = False
        print(response.json())
        return flag

    def method_create_booking_with_invalid_data(self):
        flag = True
        response = requests.post(url=self.create_booking_url, json=create_booking_invalid_data, verify=False)
        if response.status_code == 200:
            if "bookingid" in response.json():
                flag = False
        print("Status code for create booking with invalid data is --> {}".format(response.status_code))
        return flag

    def method_create_booking_with_json_data(self):
        flag = True
        response = requests.post(url=self.create_booking_url, json=self.reading_data_from_json_file(), verify=False)
        if response.status_code != 200:
            flag = False
            # if "bookingid" not in response.json():
            #     if response.json()["booking"]["firstname"] != "Swapnil":
            #         if response.json()["booking"]["lastname"] != "Rawat":
            #             flag = False
        print(response.json())
        return flag

    def reading_data_from_json_file(self):
        with open(self.json_path, "r") as reader:
            data = json.load(reader)
            return data

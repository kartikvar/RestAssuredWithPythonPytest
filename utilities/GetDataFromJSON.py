import json


class GetDataFromJSON:

    @staticmethod
    def getData():
        json_file_path = (
            "D:\\Learn_SDET\\Rest Assured\\Learn_RestAssured_SDET\\Codes\\RestAssured_Framework_Python_Pytest"
            "\\RestAssuredWithPythonPytest\\TestData\\CreateBookingMultipleData.json")
        with open(json_file_path, "r") as file:
            json_data = file.read()
            data = json.loads(json_data)
            return data

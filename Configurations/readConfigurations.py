import configparser

config_file_path = ("D:\\Learn_SDET\\Rest Assured\\Learn_RestAssured_SDET\\Codes\\RestAssured_Framework_Python_Pytest"
                    "\\RestAssuredWithPythonPytest\\Configurations\\config.ini")


def readConfig():
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config

import logging

path = ("D:\\Learn_SDET\\Rest Assured\\Learn_RestAssured_SDET\\Codes\\RestAssured_Framework_Python_Pytest"
        "\\RestAssuredWithPythonPytest\\Logs\\log_file.log")


class LogGeneration:
    @staticmethod
    def logging():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler(path)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

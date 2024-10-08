'''
take screenshot in case of test failure
code taken from https://github.com/pytest-dev/pytest/issues/230
'''
import allure
import pytest
from allure_commons.types import AttachmentType

screenshot_path = ("D:\\Learn_SDET\\Rest Assured\\Learn_RestAssured_SDET\\Codes\\RestAssured_Framework_Python_Pytest"
                   "\\RestAssuredWithPythonPytest\\Screenshot\\screen_shot.png")
baseURL = ReadConfiguration.get_application_url()
username = ReadConfiguration.get_application_username()
password = ReadConfiguration.get_application_password()


@pytest.fixture()
def setup():
    pass

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.yield_fixture
def tear_down_login(request, setup):
    driver = setup
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screen_shot", attachment_type=AttachmentType.PNG)
        driver.save_screenshot(screenshot_path)

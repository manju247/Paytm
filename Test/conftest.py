import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="F:\Softwares\Testing\chromedriver_win32\chromedriver.exe")
    driver.get("https://paytm.com/")
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
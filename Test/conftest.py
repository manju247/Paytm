import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://paytm.com/")
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.close()
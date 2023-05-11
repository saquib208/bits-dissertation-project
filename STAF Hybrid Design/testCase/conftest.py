from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(params=["chrome"],scope='class')
def setup_driver(request):
    if request.param == "chrome":
            web_driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

    if request.param=="firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    if request.param=="edge":
        web_driver = webdriver.Edge(service=Service(ChromeDriverManager.install()))


    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching chrome browser.........")
    elif browser=='firefox':
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching firefox browser.........")
    return web_driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'STAF Framework'
    config._metadata['Module Name'] = 'Web Functionality'
    config._metadata['Architect'] = 'Saquib'
    config._metadata['Language'] ='Python'
    config._metadata['Report'] = 'HTML'
    config._metadata['Language'] = 'Python'


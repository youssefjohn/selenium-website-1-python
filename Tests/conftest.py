import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def individual_setup():
    print("Setting up single test")
    yield
    print("Tearing down single test")


homepage = "https://courses.letskodeit.com/"
practisepage = "https://courses.letskodeit.com/practice"

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()

    print("Running CLASS level setup")
    driver.get(url=homepage)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    print("Tearing CLASS down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


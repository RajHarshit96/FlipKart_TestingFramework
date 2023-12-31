import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = None




def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):  # when u declare one fixture u ahve request as a instance
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":

        from selenium.webdriver.chrome.service import Service
        s = Service(executable_path="C:\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)


    elif browser_name == "firefox":

        from selenium.webdriver.firefox.service import Service
        s = Service(executable_path="C:\\FireFoxDriver\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)


    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/input[@type='text']").send_keys("7987547286")
    driver.find_element(By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/input[@type='password']").send_keys("Sanasingh12@")
    driver.find_element(By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/button[@type='submit']").click()
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
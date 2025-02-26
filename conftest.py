import os
import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def load_config():
    # Предполагается, что config.yaml находится в корне репозитория
    with open("config.yaml") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


# Загрузка конфигурации при старте тестов
config = load_config()


@pytest.fixture(scope="session")
def credentials():
    # Фикстура возвращает учетные данные из config.yaml
    return config.get("credentials", {})


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер для запуска тестов (chrome или firefox)")
    parser.addoption("--browser-version", action="store", default=None,
                     help="Версия браузера (при необходимости)")
    parser.addoption("--remote", action="store_true", default=False,
                     help="Использовать удалённый WebDriver (например, Selenoid)")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    browser_version = request.config.getoption("--browser-version")
    remote = request.config.getoption("--remote")

    if remote:
        capabilities = {"browserName": browser}
        if browser_version:
            capabilities["version"] = browser_version
        command_executor = "http://localhost:4444/wd/hub"
        driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=capabilities
        )
    else:
        if browser == "chrome":
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Браузер '{browser}' не поддерживается")

    driver.maximize_window()
    yield driver
    driver.quit()

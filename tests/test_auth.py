import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Authentication")
@allure.story("User Login")
def test_login(driver, credentials):
    driver.get("https://www.saucedemo.com/")

    # Ввод логина и пароля из config
    driver.find_element(By.ID, "user-name").send_keys(credentials.get("username"))
    driver.find_element(By.ID, "password").send_keys(credentials.get("password"))

    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 15)

    header = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='title' and text()='Products']")))
    assert header.is_displayed(), "Страница с товарами не отображается"

    inventory_item = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item")))
    assert inventory_item.is_displayed(), "Элемент товара не найден, список товаров не загружен"


@allure.feature("Authorization")
@allure.story("User Logout")
def test_logout(driver, credentials):

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(credentials.get("username"))
    driver.find_element(By.ID, "password").send_keys(credentials.get("password"))
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 15)


    header = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='title' and text()='Products']")))
    assert header.is_displayed(), "Страница с товарами не отображается после входа"


    inventory_item = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item")))
    assert inventory_item.is_displayed(), "Элемент товара не найден, список товаров не загружен"


    driver.find_element(By.ID, "react-burger-menu-btn").click()


    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "div.bm-menu-wrap").get_attribute("hidden") is None)


    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_link.click()


    login_wrapper = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "login_wrapper-inner")))
    assert login_wrapper.is_displayed(), "Контейнер логина не отображается после выхода"

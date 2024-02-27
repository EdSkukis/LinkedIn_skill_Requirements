import os
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переходим на страницу
url = "https://markets.ft.com/data/funds/uk/results"
driver.get(url)


try:
    # Ожидаем появления нового окна
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    # Переключаемся на новое окно
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    # Ждем, пока не появится кнопка "Accept Cookies" в новом окне
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@title='Accept Cookies']"))
    )
    print("Кнопка 'Accept Cookies' найдена в новом окне!")
    # Здесь можно выполнить действия с найденной кнопкой
    accept_cookies_button.click()  # Например, кликнуть по кнопк
    # element = WebDriverWait(driver, 3).until(
    #     EC.visibility_of_element_located((By.XPATH, "//button[@title='Accept Cookies']"))
    # )
    # element.click()
    print("0. Accept Cookies")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[1]/span[2]'))
    )
    element.click()
    print("1. Investment focus")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[1]/ul/li[2]'))
    )
    element.click()
    print("2. Alternative Investments")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[2]/ul/li[97]'))
    )
    element.click()
    print("3.1. Property - Direct Other")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[2]/ul/li[100]'))
    )
    element.click()
    print("3.2. Property - Indirect Europe")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[2]/ul/li[95]'))
    )
    element.click()
    print("3.3. Property - Direct Europe")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[2]/ul/li[101]'))
    )
    element.click()
    print("3.4. Property - Indirect Global")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/ul/li[1]/div[2]/div/div[2]/ul/li[101]'))
    )
    element.click()
    print("3.5. Property - Direct Global")

    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[2]/div/div/div[2]/section/form/div[2]/button[2]'))
    )
    element.click()
    print("4. Go")

except Exception as error:
    # handle the exception
    print("An exception occurred:", error)

print(requests.get(url).text)


# # Создаем пустой список для хранения результатов
# results = []


# Закрываем веб-драйвер после завершения работы
driver.quit()

# # Сохраняем результаты в JSON файл
# with open('funds_data.json', 'w') as f:
#     json.dump(results, f, indent=4)

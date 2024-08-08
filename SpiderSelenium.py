from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get('https://www.superselectos.com/products?keyword=carnes')

    time.sleep(6)

    # Capturar y mostrar la URL actual
    current_url = driver.current_url
    print(f'URL actual: {current_url}')

    selectElements = driver.find_element(By.LINK_TEXT, value='Siguiente')
    selectElements.click()

    time.sleep(3)

    #actualiza la url
    current_url = driver.current_url
    print(f'URL actual después de navegar: {current_url}')

finally:
    # Cerrar el navegador
    driver.quit()

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


product_urls = {
    "UDM Pro": "https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/udm-pro",
}


def isInStock(url):
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        badges = wait.until(presence_of_all_elements_located((By.CSS_SELECTOR, ".comProduct__badge")))
        for badge in badges:
            if badge.text == "In-Stock":
                return True
    return False


def sendNotification(product_name):
    response = requests.post("https://api.pushover.net/1/messages.json", data={
        'token': os.environ['PUSHOVER_API_TOKEN'],
        'user': os.environ['PUSHOVER_USER_TOKEN'],
        'message': product_name + ' is in stock now!',
        'priority': 1,
    })
    print(response.json())


if __name__ == '__main__':
    for product_name, product_url in product_urls.items():
        if isInStock(product_url):
            sendNotification(product_name)

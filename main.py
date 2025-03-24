from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
items = ["Time machine", "Portal", "Alchemy lab", "Shipment", "Mine", "Factory", "Grandma", "Cursor"]
start_time = time.time()

while True:
    cookie.click()
    if time.time() - start_time >= 5:
        start_time = time.time()
        money = driver.find_element(By.ID, "money").text.replace(",", "")
        money = int(money) if money.isdigit() else 0
        for item in items:
            try:
                item_element = driver.find_element(By.XPATH, f'//*[@id="buy{item}"]/b')
                item_price = item_element.text.split("-")[-1].strip().replace(",", "")
                item_price = int(item_price) if item_price.isdigit() else float("inf")
                if money >= item_price:
                    driver.find_element(By.ID, f"buy{item}").click()
                    break
            except Exception:
                pass

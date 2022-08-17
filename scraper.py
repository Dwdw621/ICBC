from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Setting up the webdriver
edge_options = Options()
#edge_options.add_argument("--headless")
service = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_options)

# Login to ICBC
driver.get("https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver")
driver.find_element(By.ID, "mat-input-0").send_keys("Wang")
driver.find_element(By.ID, "mat-input-1").send_keys("2569783")
driver.find_element(By.ID, "mat-input-2").send_keys("Dang")
driver.find_element(By.XPATH,
                    "/html/body/app-root/app-login/mat-card/mat-card-content/form/span[2]/div[3]/mat-checkbox/label/span[1]").click()
WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/app-root/app-login/mat-card/mat-card-content/form/div[3]/button[2]"))).click()

# Reschedule
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,
                                                           "/html/body/app-root/app-driver/div/mat-card/div[5]/div[1]/app-appointments/div/div[2]/div/div[4]/button[1]"))).click()
WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-cancel/div/div/div[2]/button[2]/span[1]"))).click()

site_list = {"Richmond": "/html/body/div/div/div/mat-dialog-container/app-search-modal/div[2]/div/div[2]/div[2]",
             "Kingsway": "/html/body/div/div/div/mat-dialog-container/app-search-modal/div[2]/div/div[5]/div",
             "Point Grey": "/html/body/div/div/div/mat-dialog-container/app-search-modal/div[2]/div/div[4]/div"}


def is_available():
    try:
        pick_city()
        for site in site_list:
            driver.find_element(By.XPATH, site_list[site]).click()
            time.sleep(2)
            dates = driver.find_elements(By.CLASS_NAME, "date-title")
            for date in dates:
                print("Success!")
                if "August" in date.text:
                    return True
            driver.find_element(By.XPATH,
                                "/html/body/div/div[2]/div/mat-dialog-container/app-eligible-tests/div/div[3]/button[1]/span[1]").click()
    except:
        print("Scraper error")
        exit()


def pick_city():
    try:
        driver.find_element(By.ID, "mat-input-3").send_keys("Ric")
        time.sleep(.2)

        driver.find_element(By.XPATH,
                            "/html/body/div/div/div/mat-dialog-container/app-search-modal/div/div/form/div[1]/mat-radio-group/div/mat-radio-button/label/span[2]").click()
        driver.find_element(By.ID, "mat-input-3").click()
        time.sleep(.2)

        driver.find_element(By.ID, "mat-input-3").send_keys("hmo")
        time.sleep(.2)

        driver.find_element(By.XPATH,
                            "/html/body/div/div/div/mat-dialog-container/app-search-modal/div/div/form/div[1]/mat-radio-group/div/mat-radio-button/label/span[2]").click()
        driver.find_element(By.ID, "mat-input-3").click()
        time.sleep(.2)

        driver.find_element(By.ID, "mat-input-3").send_keys("nd")
        time.sleep(.2)

        driver.find_element(By.XPATH,
                            "/html/body/div/div/div/mat-dialog-container/app-search-modal/div/div/form/div[1]/mat-radio-group/div/mat-radio-button/label/span[2]").click()
        driver.find_element(By.ID, "mat-input-3").click()
        time.sleep(.2)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/mat-option[1]/span").click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div/mat-dialog-container/app-search-modal/div/div/form/div[2]/button"))).click()
        time.sleep(0.5)
    except:
        print("City picker error!")
        exit()


def by_XPATH(val):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, val)))


def by_ID(val):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, val)))

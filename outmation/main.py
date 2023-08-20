# %%
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import os
import time
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

original_window = driver.current_window_handle

# %%
SCHOOL_ID = os.environ.get("SCHOOL_ID") or input("input school id please.")
USER_NAME = os.environ.get("USER_NAME") or input("input user name please.")
PASSWORD = os.environ.get("PASSWORD") or input("input password please.")
SITE_URL = "https://goldfingerschool.jp/school/main.php"

driver.get(SITE_URL)

school_id_input_element = driver.find_element(
    by=By.XPATH, value='//*[@id="info-box"]/div/div[1]/form/dl/dd[1]/input'
)
username_input_element = driver.find_element(
    by=By.XPATH, value='//*[@id="info-box"]/div/div[1]/form/dl/dd[2]/input'
)
password_input_element = driver.find_element(
    by=By.XPATH, value='//*[@id="info-box"]/div/div[1]/form/dl/dd[3]/input'
)
login_button = driver.find_element(
    by=By.XPATH, value='//*[@id="info-box"]/div/div[1]/form/dl/dt[4]/input[2]'
)
school_id_input_element.clear()
username_input_element.clear()
password_input_element.clear()
school_id_input_element.send_keys(SCHOOL_ID)
username_input_element.send_keys(USER_NAME)
password_input_element.send_keys(PASSWORD)
SCHOOL_ID = USER_NAME = PASSWORD = None
login_button.click()
time.sleep(1)
# %%
driver.find_element(
    by=By.XPATH, value='/html/body/div/ul[3]/li[3]/form/div/input[2]'
).click()
done_button = driver.find_elements(
    by=By.CLASS_NAME, value="done-button-class"
)

for i in range(len(done_button)):
    driver.find_elements(
        by=By.CLASS_NAME, value="done-button-class")[i].click()
    driver.find_element(By.TAG_NAME, "body").send_keys(" ")
    driver.execute_script(
        'setTimeout(() => { document.querySelectorAll("#textdata rt,rp").forEach(each => each.remove()); document.querySelector("#inputdata").value = document.querySelector("#textdata").textContent; document.getElementById("checkbutton").click(); document.getElementById("alertify-ok").click(); document.getElementById("backtohome1").click();}, 0)'
    )
    time.sleep(0.5)


# %%
driver.quit()

# %%

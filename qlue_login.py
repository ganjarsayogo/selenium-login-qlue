import unittest
import time
import warnings
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin(unittest.TestCase): 

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, options=options)
        warnings.simplefilter('ignore', ResourceWarning)        

    def test_1_success_login(self): 
        driver = self.driver
        driver.get('https://dashboard-dev.qlue.ai/login?email=&redirect_to=')
        time.sleep(1)
        driver.find_element(By.NAME, 'email').send_keys('ganjar.sayogo1@gmail.com')
        time.sleep(1)
        driver.find_element(By.NAME, 'password').send_keys('Ganjar123')
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[4]/div/div').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/main/div[2]/div/form/button').click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div/h3").text
        self.assertEqual(response_data, 'Welcome To Qlue Dashboard!')

    def test_2_failed_login_with_empty_email_and_password(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[2]/div/input")))
        assert username.get_attribute("validationMessage") == "Please fill out this field."       
    
    def test_3_failed_login_with_empty_email(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("Ganjar123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[2]/div/input")))
        assert username.get_attribute("validationMessage") == "Please fill out this field."       

    def test_4_failed_login_with_empty_password(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("ganjar.sayogo@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        assert password.get_attribute("validationMessage") == "Please fill out this field."       

    def test_5_failed_login_with_symbol_password(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("ganjar.sayogo1@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("G@njar123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        password = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[4]/div[2]").text
        self.assertEqual(password, 'Wrong password')

    def test_6_failed_login_with_phone_number(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("081345755941")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("Ganjar123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[2]/div/input")))
        assert username.get_attribute("validationMessage") == "Please include an '@' in the email address. '081345755941' is missing an '@'."

    def test_7_failed_login_with_added_space_in_password(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("ganjar.sayogo@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("Ganjar123 ")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        password = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[4]/div[2]").text
        self.assertEqual(password, 'Wrong password')

    def test_8_failed_login_with_unregistered_email(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("ganjar@gmail.co.id")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("Ganjar1234")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        username = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[2]/div[2]").text
        self.assertEqual(username, 'Email or phone is not registered')

    def test_9_failed_login_with_password_turned_uppercased(self):
        driver = self.driver
        driver.get("https://dashboard-dev.qlue.ai/login?email=&redirect_to=")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("ganjar.sayogo@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("GANJAR123 ")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/button").click()
        time.sleep(1)

        password = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[2]/div/form/div[4]/div[2]").text
        self.assertEqual(password, 'Wrong password')
   
    def tearDown(self): 
        self.driver.quit()

if __name__ == "__main__": 
    unittest.main()
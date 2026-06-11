import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTESTCASE1():
    def setup_method(self, method):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_tESTCASE1(self):
        self.driver.get("https://drsstaging.pta.gov.pk/drs-git/drs-revamp-client/")
        self.driver.set_window_size(697, 728)
        
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(1) .card-title").click()
        self.driver.find_element(By.ID, "imei_1").click()
        self.driver.find_element(By.ID, "imei_1").send_keys("990017412593838")
        
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        self.driver.find_element(By.ID, "otp").click()
        
        jenkins_otp = os.environ.get("MY_OTP", "")
        
        if jenkins_otp:
            self.driver.find_element(By.ID, "otp").send_keys(jenkins_otp)
            print(f"OTP {jenkins_otp} successfully entered!")
        else:
            print("Error: OTP environment variable 'MY_OTP' not found!")
        
        self.driver.execute_script("window.scrollTo(0,450)")

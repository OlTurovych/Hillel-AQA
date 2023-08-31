import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests


class TestAddCar:
    def setup_class(self):
        chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.driver.implicitly_wait(5)
        self.session = requests.session()
        self.user_email = "fitotest___42@test.com"
        self.user_password = "Option123!"


    def test_user_registration(self):
        user_data = {
            "name": "Olga",
            "lastName": "Testing",
            "email": self.user_email,
            "password": self.user_password,
            "repeatPassword": self.user_password,
        }

        registration = self.session.post(
            url="https://qauto2.forstudy.space/api/auth/signup", json=user_data
        )
        assert registration.status_code == 201

    def test_login_with_selenium(self):
        sign_in_button = self.driver.find_element(
            By.XPATH, "//button[text()='Sign In']"
        )
        sign_in_button.click()
        email_field = self.driver.find_element(By.ID, "signinEmail")
        password_field = self.driver.find_element(By.ID, "signinPassword")

        email_field.send_keys(self.user_email)
        password_field.send_keys(self.user_password)
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()

        assert self.driver.find_element(
            By.XPATH, "//p[contains(text(), 'any cars in your garage')]"
        )

    def test_add_car(self):
        self.driver.find_element(
            By.XPATH, '//button[@class="btn btn-primary" and text()="Add car"]'
        ).click()
        self.driver.find_element(By.ID, "addCarBrand").click()
        self.driver.find_element(
            By.XPATH, '//select[@name="carBrandId"]/option[text()="BMW"]'
        ).click()
        self.driver.find_element(By.ID, "addCarModel").click()
        self.driver.find_element(
            By.XPATH, '//select[@name="carModelId"]/option[text()="X5"]'
        ).click()
        self.driver.find_element(By.ID, "addCarMileage").send_keys("100")
        self.driver.find_element(By.XPATH, '//button[text()="Add"]').click()

    def test_added_car(self):
        assert len(self.driver.find_elements(
            By.XPATH, '//ul//li[@class="car-item"]')
        ) > 0
        
    def test_check_car_api(self):
        expected_brand = "BMW"
        expected_model = "X5"
        expected_mileage = 100

        response = self.session.get(url="https://qauto2.forstudy.space/api/cars")
        assert response.status_code == 200

        cars = response.json()
        # print(cars)
        for car in cars['data']:
            if car['brand'] == expected_brand \
                and car['model'] == expected_model \
                and car['mileage'] == expected_mileage:
                    break
        else:
            raise AssertionError("Car not found in API response")
        
        assert True

    def teardown_class(self):
        self.session.delete(url="https://qauto2.forstudy.space/api/users")
        self.driver.close()

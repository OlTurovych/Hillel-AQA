import requests


class TestUserCreation:
    def setup_class(self):
        self.session = requests.session()
        self.user_email = "test1305@test.com"
        self.user_password = "Qwerty12345"

    def test_user_creation(self):
        success_reg_test_data = {
            "name": "John",
            "lastName": "Dou",
            "email": self.user_email,
            "password": self.user_password,
            "repeatPassword": self.user_password,
        }
        result = self.session.post(
            url="https://qauto2.forstudy.space/api/auth/signup",
            json=success_reg_test_data,
        )
        assert result.status_code == 201

    def teardown_class(self):
        login_dict = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False,
        }

        result = self.session.post(
            url="https://qauto2.forstudy.space/api/auth/signin", json=login_dict
        )
        assert result.status_code == 200
        self.session.delete(url="https://qauto2.forstudy.space/api/users/")

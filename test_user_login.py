import requests


class TestLogin:
    def setup_class(self):
        self.session = requests.session()
        self.user_email = "test130555578@test.com"
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

    def test_user_login(self):
        login_creds = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": True,
        }

        result = self.session.post(
            url="https://qauto2.forstudy.space/api/auth/signin", json=login_creds
        )
        assert result.status_code == 200
        proofed_login = self.session.get(
            url="https://qauto2.forstudy.space/api/users/profile"
        )
        assert proofed_login.status_code == 200

    def teardown_class(self):
        deleted_user = self.session.delete(url="https://qauto2.forstudy.space/api/users/")
        assert deleted_user.status_code == 200


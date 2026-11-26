import allure
from playwright.sync_api import APIRequestContext, APIResponse

from clients.base_client import BaseClient


class AccountClient(BaseClient):
    def __init__(self, api_request_context: APIRequestContext) -> None:
        super().__init__(api_request_context)

    @allure.step("Проверка авторизации пользователя")
    def verify_login(self, email: str | None = None, password: str | None = None)  -> APIResponse:
        payload = {}
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        return self.post("/api/verifyLogin", payload)

    @allure.step("Создание аккаунта")    
    def create_account(
            self,
            user_data: dict[str, str],
        )  -> APIResponse:
        payload = {
            "name": user_data["username"], 
            "firstname": user_data["first_name"], 
            "lastname": user_data["last_name"], 
            "address1": user_data["address_1"], 
            "address2": user_data["address_2"], 
            "mobile_number": user_data["phone"], 
            "birth_date": user_data["day"], 
            "birth_month": user_data["month"], 
            "birth_year": user_data["year"],
            "title": "Mr",
            "country": "United States",
            "password": user_data["password"],
            "state": user_data["state"],
            "city": user_data["city"],
            "zipcode": user_data["zipcode"],
            "company": user_data["company"], 
            "email": user_data["email"],
        }
        return self.post("/api/createAccount", payload)

    @allure.step("Обновление аккаунта")    
    def update_account(
            self,
            user_data: dict[str, str],
        )  -> APIResponse:
        payload = {
            "name": user_data["username"], 
            "firstname": user_data["first_name"], 
            "lastname": user_data["last_name"], 
            "address1": user_data["address_1"], 
            "address2": user_data["address_2"], 
            "mobile_number": user_data["phone"], 
            "birth_date": user_data["day"], 
            "birth_month": user_data["month"], 
            "birth_year": user_data["year"],
            "title": "Mr",
            "country": "United States",
            "password": user_data["password"],
            "state": user_data["state"],
            "city": "New York",
            "zipcode": user_data["zipcode"],
            "company": user_data["company"], 
            "email": user_data["email"],
        }
        return self.put("/api/updateAccount", payload)

    @allure.step("Удаление аккаунта")    
    def delete_account(
        self, 
        user_data: dict[str, str]
        )  -> APIResponse:
        payload = {
            "password": user_data["password"],
            "email": user_data["email"],
            }
        return self.delete("/api/deleteAccount", payload)
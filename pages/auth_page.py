import allure
from playwright.sync_api import Page, expect

from pages.account_creation_page import AccountCreationPage
from pages.base_page import BasePage
from pages.home_page import HomePage


class AuthPage(BasePage):
    URL = "https://www.automationexercise.com/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.username_input = page.locator('[data-qa="signup-name"]')
        self.signup_email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
    
    @allure.step("Открытие страницы авторизации и регистрации")    
    def open_page(self) -> None:
        self.open(self.URL)
        
    @allure.step("Проверка видимости форм входа и регистрации") 
    def check_visible_auth_form(self) -> None:
        expect(self.username_input).to_be_visible()
        expect(self.login_email_input).to_be_visible()
        expect(self.login_button).to_be_visible()
        expect(self.signup_email_input).to_be_visible()
        expect(self.login_password_input).to_be_visible()
        expect(self.signup_button).to_be_visible()

    @allure.step("Заполнение формы регистрации (имя: '{username}', email: '{email}')") 
    def fill_registration_form(
            self,
            username: str,
            email: str,
    ) -> None:
        self.username_input.fill(username)
        self.signup_email_input.fill(email)
    
    @allure.step("Нажатие кнопки регистрации (Signup)")   
    def click_registration_button(self) -> None:
        self.signup_button.click()
    
    @allure.step("Начало регистрации пользователя '{username}' ({email})") 
    def registration_as(self, username: str, email: str) -> None:
        self.open_page()
        self.check_visible_auth_form()
        self.fill_registration_form(
            username=username,
            email=email,
            )
        self.click_registration_button()
        return AccountCreationPage(self.page)
    
    @allure.step("Заполнение формы входа (email: '{email}')")        
    def fill_login_form(
            self,
            email: str,
            password: str,
    ) -> None:
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
    
    @allure.step("Нажатие кнопки входа (Login)")    
    def click_login_button(self) -> None:
        self.login_button.click()
        from pages.home_page import HomePage
        return HomePage(self.page)
        
    @allure.step("Авторизация пользователя ({email})")     
    def login_as(self, email: str, password: str) -> HomePage:
            self.open_page()
            self.check_visible_auth_form()
            self.fill_login_form(
                email=email,
                password=password,
                )
            return self.click_login_button()
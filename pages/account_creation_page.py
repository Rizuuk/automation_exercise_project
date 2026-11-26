import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.final_account_creation_page import FinalAccountCreationPage


class AccountCreationPage(BasePage):
    URL = "https://www.automationexercise.com/signup"

    def __init__(self, page: Page):
        super().__init__(page)
        
        
        self.username_input = page.locator('#name')
        self.email = page.locator('#email')
        self.password_input = page.locator('#password')
        self.mr_button = page.locator('#id_gender1')
        self.mrs_button = page.locator('#id_gender2')
        self.select_day = page.locator('#days')
        self.select_months = page.locator('#months')
        self.select_years = page.locator('#years') 
        self.newsletter = page.locator('#newsletter')
        self.optin = page.locator('#optin')
        self.first_name = page.locator('#first_name')
        self.last_name = page.locator('#last_name')
        self.company = page.locator('#company')
        self.address_1 = page.locator('#address1')
        self.address_2 = page.locator('#address2')
        self.select_country = page.locator('#country')
        self.state = page.locator('#state')
        self.city = page.locator('#city')
        self.zipcode = page.locator('#zipcode')
        self.mobile_number = page.locator('#mobile_number')
        self.create_account_button = page.locator('[data-qa="create-account"]')
        
    @allure.step("Открытие страницы регистрации аккаунта")
    def open_page(self) -> None:
        self.open(self.URL)
    
    @allure.step("Проверка видимости формы деталей аккаунта")    
    def check_visible_account_details_form(self) -> None:
        expect(self.username_input).to_be_visible(timeout=15000)
        expect(self.password_input).to_be_visible()
        expect(self.create_account_button).to_be_visible()
    
    @allure.step("Заполнение формы аккаунта")    
    def fill_account_form(
            self,
            gender: str,
            password: str,
            day: str,
            months: str,
            years: str,
            newsletter: bool,
            optin: bool,
            first_name: str,
            last_name: str,
            address_1: str,
            country: str,
            state: str,
            city: str,
            zipcode: str,
            mobile_number: str,
            company: str = "",
            address_2: str = "",
    ) -> None:
        if gender == "mr":
            self.mr_button.click()
        elif gender == "mrs":
            self.mrs_button.click()
        self.password_input.fill(password)
        self.select_day.select_option(day)
        self.select_months.select_option(months)
        self.select_years.select_option(years)
        if newsletter == True:
            self.newsletter.click()
        if optin == True:
            self.optin.click()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address_1.fill(address_1)
        self.address_2.fill(address_2)
        self.select_country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)
    
    @allure.step("Нажатие на создание аккаунта")    
    def click_create_account_button(self) -> "FinalAccountCreationPage":
        self.create_account_button.click()
        return FinalAccountCreationPage(self.page)
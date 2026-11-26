import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class FinalAccountCreationPage(BasePage):
    URL = "https://www.automationexercise.com/account_created"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.account_created = page.locator('[data-qa="account-created"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')
    
    @allure.step("Проверка перехода на страницу подтверждения создания аккаунта")      
    def check_opened_final_account_creation(self) -> None:
        self.check_current_url(self.URL)
    
    @allure.step("Проверка отображения сообщения об успешном создании аккаунта (Account Created!)")      
    def check_visible_final_account_creation(self) -> None:
        expect(self.account_created).to_be_visible()
        expect(self.account_created).to_have_text("Account Created!")
        expect(self.continue_button).to_be_visible()
    
    @allure.step("Нажатие кнопки Continue после создания аккаунта")      
    def click_continue_button(self) -> None:
        self.continue_button.click()
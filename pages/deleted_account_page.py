import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DeletedAccountPage(BasePage):
    URL = "https://www.automationexercise.com/delete_account"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.title_account_deleted = page.locator('[data-qa="account-deleted"]')
        self.delete_account_continue_button = page.locator('[data-qa="continue-button"]')
        
    @allure.step("Открытие страницы подтверждения удаления аккаунта")  
    def open_page(self) -> None:
        self.open(self.URL)
    
    @allure.step("Проверка отображения сообщения об успешном удалении аккаунта (Account Deleted!)")      
    def check_account_deleted_screen_visible(self) -> None:
        expect(self.title_account_deleted).to_be_visible()
        expect(self.title_account_deleted).to_have_text("Account Deleted!")
        expect(self.delete_account_continue_button).to_be_visible()
        
    @allure.step("Нажатие кнопки Continue после удаления аккаунта")    
    def delete_account_continue_button_click(self):
        self.delete_account_continue_button.click()
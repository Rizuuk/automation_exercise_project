import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.deleted_account_page import DeletedAccountPage


class HomePage(BasePage):
    URL = "https://www.automationexercise.com/"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.shop_menu = page.locator('.shop-menu.pull-right')
        self.logout_button = page.locator('.shop-menu a:has-text("Logout")')
        self.delete_account_button = page.locator('.shop-menu a:has-text("Delete Account")')

    @allure.step("Открытие главной страницы") 
    def open_page(self) -> None:
        self.open(self.URL)

    @allure.step("Проверка отображения меню авторизованного пользователя (Logout и Delete Account)")         
    def check_authorized_navigation_menu(self) -> None:
        expect(self.shop_menu).to_be_visible()
        expect(self.logout_button).to_contain_text("Logout")
        expect(self.delete_account_button).to_contain_text("Delete Account")
    
    @allure.step("Нажатие кнопки удаления аккаунта (Delete Account)")     
    def delete_account_button_click(self):
        self.delete_account_button.click()
        return DeletedAccountPage(self.page)
    
    @allure.step("Нажатие кнопки выхода из аккаунта (Logout)") 
    def logout_button_click(self):
        self.logout_button.click()
        from pages.auth_page import AuthPage
        return AuthPage(self.page)
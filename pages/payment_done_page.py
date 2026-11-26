import re

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class PaymentDonePage(BasePage):
    URL = "https://www.automationexercise.com/payment_done"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.order_placed = page.locator('[data-qa="order-placed"]')
        self.download_invoice_button = page.get_by_role("link", name="Download Invoice")
        self.continue_button = page.locator('[data-qa="continue-button"]')
    
    @allure.step("Проверка отображения страницы успешной оплаты заказа")     
    def check_visible_payment_done(self) -> None:
        expect(self.order_placed).to_be_visible()
        expect(self.download_invoice_button).to_be_visible()
        expect(self.continue_button).to_be_visible()
    
    @allure.step("Проверка URL страницы подтверждения заказа (/payment_done)")     
    def check_opened_payment_done(self) -> None:
        expect(self.page).to_have_url(re.compile(rf"{self.URL}/\d+"))
    
    @allure.step("Нажатие кнопки Continue после оформления заказа")         
    def continue_button_click(self):
        self.continue_button.click()
            
        
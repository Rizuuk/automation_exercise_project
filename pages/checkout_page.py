import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.payment_page import PaymentPage


class CheckoutPage(BasePage):
    URL = "https://www.automationexercise.com/checkout"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.checkout_information = page.locator('.checkout-information')
        self.place_order_button = page.get_by_role("link", name="Place Order")
    
    @allure.step("Проверка отображения информации о заказе и кнопки Place Order")      
    def check_visible_checkout(self) -> None:
            expect(self.checkout_information).to_be_visible()
            expect(self.place_order_button).to_be_visible()
    
    @allure.step("Нажатие кнопки подтверждения заказа (Place Order)")          
    def place_order_button_click(self):
            self.place_order_button.click()
            return PaymentPage(self.page)
import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    URL = "https://www.automationexercise.com/view_cart"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.check_out_button = page.locator('.btn.btn-default.check_out')
        self.total_price = page.locator('.cart_total_price')
        
    @allure.step("Открытие страницы корзины")     
    def open_page(self) -> None:
            self.open(self.URL)
    
    @allure.step("Проверка отображения корзины и кнопки оформления заказа")       
    def check_visible_cart(self) -> None:
        expect(self.check_out_button).to_be_visible()
    
    @allure.step("Проверка количества позиций товаров в корзине (ожидается: {value})")     
    def quantity_of_goods_count(self, value: int):
        expect(self.total_price).to_have_count(value)
    
    @allure.step("Нажатие кнопки оформления заказа (Proceed To Checkout)")     
    def check_out_button_click(self):
        self.check_out_button.click()
        return CheckoutPage(self.page)
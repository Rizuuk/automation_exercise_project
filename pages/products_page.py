import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductsPage(BasePage):
    URL = "https://www.automationexercise.com/products"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.search_button = page.locator('[type="button"]#submit_search')
        self.continue_shopping_button = page.locator('.btn.btn-success.close-modal.btn-block')
        self.view_cart_button = page.locator('.text-center a:has-text("View Cart")')
        
    @allure.step("Открытие страницы всех товаров")          
    def open_page(self) -> None:
            self.open(self.URL)
    
    @allure.step("Проверка отображения страницы товаров")        
    def check_visible_products(self) -> None:
        expect(self.search_button).to_be_visible()
    
    @allure.step("Добавление товара '{product_name}' в корзину")    
    def add_product_to_cart_by_name(self, product_name: str):
        product_card = self.page.locator(".product-image-wrapper").filter(has_text=product_name)
        product_card.hover()
        product_card.locator(".product-overlay .add-to-cart").click()
    
    @allure.step("Нажатие кнопки продолжения покупок (Continue Shopping)")    
    def continue_shopping_button_click(self):
        self.continue_shopping_button.click()
    
    @allure.step("Переход в корзину из модального окна (View Cart)")    
    def view_cart_button_click(self):
        self.view_cart_button.click()
        return CartPage(self.page)
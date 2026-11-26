from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
        self.products_button = page.locator('.shop-menu a:has-text("Products")')
        self.cart_button = page.locator('.shop-menu a:has-text("Cart")')

    def open(self, url: str) -> None:
        self.page.goto(url)

    def check_current_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)
        
    def products_button_click(self):
        self.products_button.click()
        from pages.products_page import ProductsPage
        return ProductsPage(self.page)
    
    def cart_button_click(self):
        self.cart_button.click()
        from pages.cart_page import CartPage
        return CartPage(self.page)
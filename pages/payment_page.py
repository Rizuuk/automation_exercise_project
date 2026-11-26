import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class PaymentPage(BasePage):
    URL = "https://www.automationexercise.com/payment"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.name_on_card = page.locator('[name="name_on_card"]')
        self.card_number = page.locator('[name="card_number"]')
        self.cvc = page.locator('[name="cvc"]')
        self.expiry_month = page.locator('[name="expiry_month"]')
        self.expiry_year = page.locator('[name="expiry_year"]')
        self.pay_button = page.locator('#submit')
        self.heading_payment = page.locator('.heading')
    
    @allure.step("Проверка отображения заголовка страницы оплаты (Payment)")     
    def check_visible_heading_payment(self) -> None:
            expect(self.heading_payment).to_be_visible()
            expect(self.heading_payment).to_have_text("Payment")
    
    @allure.step("Заполнение платежных данных карты")         
    def fill_payment_form(
                self,
                name_on_card: str,
                card_number: str,
                cvc: str,
                card_month: str,
                card_year: str,
        ) -> None:
            self.name_on_card.fill(name_on_card)
            self.card_number.fill(card_number)
            self.cvc.fill(cvc)
            self.expiry_month.fill(card_month)
            self.expiry_year.fill(card_year)
    
    @allure.step("Нажатие кнопки подтверждения оплаты (Pay and Confirm Order)")          
    def pay_button_click(self):
        self.pay_button.click()
        from pages.payment_done_page import PaymentDonePage
        return PaymentDonePage(self.page)
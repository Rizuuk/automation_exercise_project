from playwright.sync_api import Page, expect

from pages.base_page import BasePage


def test_successful_purchase(created_user_page, user_data: dict[str, str]): 
    base_page = BasePage(created_user_page)
    products_page = base_page.products_button_click()
    products_page.check_visible_products()
    products_page.add_product_to_cart_by_name("Summer White Top")
    products_page.continue_shopping_button_click()
    products_page.add_product_to_cart_by_name("Blue Top")
    cart_page = products_page.view_cart_button_click()
    cart_page.check_visible_cart()
    cart_page.quantity_of_goods_count(2)
    checkout_page = cart_page.check_out_button_click()
    checkout_page.check_visible_checkout()
    payment_page = checkout_page.place_order_button_click()
    payment_page.check_visible_heading_payment()
    payment_page.fill_payment_form(
        name_on_card=user_data["full_name"],
        card_number=user_data["card_number"],
        cvc=user_data["cvc"],
        card_month=user_data["card_month"],
        card_year=user_data["card_year"],
    )
    payment_done_page = payment_page.pay_button_click()
    payment_done_page.check_visible_payment_done()
    payment_done_page.continue_button_click()
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.ui
def test_user_lifecycle(user_data, created_user_page): 
    home_page = HomePage(created_user_page)
    home_page.check_authorized_navigation_menu()
    auth_page = home_page.logout_button_click()
    auth_page.check_visible_auth_form()
    home_page = auth_page.login_as(
        email=user_data["email"],
        password=user_data["password"],
        )
    home_page.check_authorized_navigation_menu()
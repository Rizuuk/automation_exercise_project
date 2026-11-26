import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.ui
def test_delete_account(created_user_page): 
    home_page = HomePage(created_user_page)
    home_page.check_authorized_navigation_menu()
    deleted_account_page = home_page.delete_account_button_click()
    deleted_account_page.check_account_deleted_screen_visible()
    deleted_account_page.delete_account_continue_button_click()  
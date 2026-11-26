import pytest
from playwright.sync_api import Page, expect

from pages.auth_page import AuthPage


@pytest.mark.ui
def test_registration(
    user_data: dict[str, str],
    auth_page: AuthPage,
    ):

    account_creation_page = auth_page.registration_as(
        username=user_data["username"],
        email=user_data["email"],
        )
    
    account_creation_page.check_visible_account_details_form()
    account_creation_page.fill_account_form(
            gender="mr",
            password=user_data["password"],
            day=user_data["day"],
            months=user_data["month"],
            years=user_data["year"],
            newsletter=user_data["newsletter"],
            optin=user_data["optin"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            address_1=user_data["address_1"],
            country="United States",
            state=user_data["state"],
            city=user_data["city"],
            zipcode=user_data["zipcode"],
            mobile_number=user_data["phone"],
            company=user_data["company"],
            )
    
    final_account_creation_page = account_creation_page.click_create_account_button()
    
    final_account_creation_page.check_opened_final_account_creation()
    final_account_creation_page.check_visible_final_account_creation()
    final_account_creation_page.click_continue_button()
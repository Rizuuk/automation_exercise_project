import allure
import pytest
from faker import Faker
from playwright.sync_api import APIRequestContext, Page, Playwright

from clients.account_client import AccountClient
from clients.products_client import ProductsClient
from pages.auth_page import AuthPage

fake = Faker()


@pytest.fixture
def user_data() -> dict[str, str]:
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return {
        "email": fake.email(),
        "password": fake.password(),
        "username": fake.first_name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address_1": fake.street_address(),
        "address_2": fake.street_address(),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "phone": fake.phone_number(),
        "month": dob.strftime("%B"),
        "year": dob.strftime("%Y"),
        "day": dob.strftime("%#d"),
        "newsletter": fake.boolean(),
        "optin": fake.boolean(),
        "card_number": fake.credit_card_number(),
        "cvc": fake.credit_card_security_code(),
        "card_month": fake.month(),
        "card_year": str(fake.random_int(min=2027, max=2035)),
        "full_name": fake.name(),
    }
    
@pytest.fixture
def auth_page(page: Page) -> AuthPage:
    return AuthPage(page)    

@pytest.fixture
def created_user_page(
    #Создает страницу пользователя 
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
    
    return final_account_creation_page.page


@pytest.fixture
def products_client(api_request_context: APIRequestContext) -> ProductsClient:
    return ProductsClient(api_request_context)

@pytest.fixture
def api_request_context(playwright: Playwright, base_url: str):
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()
    
@pytest.fixture
def account_client(api_request_context: APIRequestContext) -> AccountClient:
    return AccountClient(api_request_context)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("created_user_page")
        if page is not None:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG,
            )

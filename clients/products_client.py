import allure
from playwright.sync_api import APIRequestContext, APIResponse

from clients.base_client import BaseClient


class ProductsClient(BaseClient):
    def __init__(self, api_request_context: APIRequestContext) -> None:
        super().__init__(api_request_context)
     
    @allure.step("Получение списка всех товаров")   
    def get_products_list(self) -> APIResponse:
        return self.get("/api/productsList")
    
    @allure.step("Поиск товара по запросу: '{product_name}'")
    def search_product(self, product_name: str) -> APIResponse:
        return self.post("/api/searchProduct", {"search_product": product_name})
    
    @allure.step("Отправка запрещенного POST-запроса на получение списка товаров")
    def post_products_list(self)  -> APIResponse:
        return self.post("/api/productsList")
    

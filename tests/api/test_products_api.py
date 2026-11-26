import json

import pytest

from clients.products_client import ProductsClient


@pytest.mark.api
def test_get_products_list(products_client: ProductsClient) -> None:
    response = products_client.get_products_list()
    response_data = json.loads(response.text())

    assert response.status == 200
    assert response_data["responseCode"] == 200
    assert len(response_data["products"]) > 0
    
@pytest.mark.api
def test_search_product(products_client: ProductsClient) -> None:
    query = "top"
    response = products_client.search_product(query)
    response_data = json.loads(response.text())
    
    assert response.status == 200
    assert response_data["responseCode"] == 200
    assert len(response_data["products"]) > 0
    for product in response_data["products"]:
        assert (
            query in product["name"].lower() 
            or query in  product["category"]["category"].lower()
            ), f"Товар '{product['name']}' (категория '{product['category']['category']}') не подходит"
    

@pytest.mark.api
def test_post_products_list_not_allowed(products_client: ProductsClient) -> None:
    response = products_client.post_products_list()
    response_data = json.loads(response.text())
    
    assert response.status == 200
    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."
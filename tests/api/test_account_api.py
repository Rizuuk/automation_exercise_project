import json

import pytest

from clients.account_client import AccountClient


@pytest.mark.api
def test_wrong_verify_login(account_client: AccountClient) -> None:
    email = "email"
    password = "password"
    response = account_client.verify_login(email, password)
    response_data = json.loads(response.text())
    
    assert response.status == 200
    assert response_data["responseCode"] == 404 
    assert response_data["message"] == "User not found!"
    
@pytest.mark.api
def test_empty_verify_login(account_client: AccountClient) -> None:
    response = account_client.verify_login()
    response_data = json.loads(response.text())
    
    assert response.status == 200
    assert response_data["responseCode"] == 400 
    assert response_data["message"] == "Bad request, email or password parameter is missing in POST request."
    
@pytest.mark.api
def test_user_account_lifecycle_api(account_client: AccountClient, user_data: dict[str, str]) -> None:
    response = account_client.create_account(user_data)
    response_data = json.loads(response.text())
    
    assert response.status == 200
    assert response_data["responseCode"] == 201 
    assert response_data["message"] == "User created!"
    
    response = account_client.verify_login(
        user_data["email"], 
        user_data["password"]
        )
    response_data = json.loads(response.text())
        
    assert response.status == 200
    assert response_data["responseCode"] == 200 
    assert response_data["message"] == "User exists!"
    
    response = account_client.update_account(user_data)
    response_data = json.loads(response.text())
        
    assert response.status == 200
    assert response_data["responseCode"] == 200 
    assert response_data["message"] == "User updated!"
    
    response = account_client.delete_account(user_data)
    response_data = json.loads(response.text())
            
    assert response.status == 200
    assert response_data["responseCode"] == 200 
    assert response_data["message"] == "Account deleted!"
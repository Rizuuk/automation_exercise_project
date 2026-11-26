from playwright.sync_api import APIRequestContext, APIResponse


class BaseClient:
    def __init__(self, api_request_context: APIRequestContext) -> None:
        self.request = api_request_context
    
    def get(self, url: str) -> APIResponse:
        return self.request.get(url)
    
    def post(self, url: str, form: dict | None = None) -> APIResponse:
        return self.request.post(url, form=form)
    
    def put(self, url: str, form: dict | None = None) -> APIResponse:
        return self.request.put(url, form=form)
    
    def delete(self, url: str, form: dict | None = None) -> APIResponse:
        return self.request.delete(url, form=form)
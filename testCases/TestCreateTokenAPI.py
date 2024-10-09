from methods.CreateTokenAPI import CreateTokenAPI


class TestCreateTokenAPI(CreateTokenAPI):

    def test_create_token_api_with_valid_credentials(self):
        response = self.method_create_token_with_valid_credentials()
        assert response is True

    def test_create_token_api_with_invalid_credentials(self):
        response = self.method_create_token_with_invalid_credentials()
        assert response is True

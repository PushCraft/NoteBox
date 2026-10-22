from src.handler import lambda_handler


def test_placeholder_returns_not_implemented():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 501

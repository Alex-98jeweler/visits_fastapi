import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from src.main import app




@pytest.mark.anyio
async def test_get_domains():
    async with AsyncClient(app=app, ) as client:
        response = await client.get('/visited_domains')
    json = response.json()
    assert response.status_code == 200
    assert json['status'] == 'success'


# def test_success_resposne():
#     links = {
#         'links': ['https://example1.com', 'https://example2.com', 'https://example3.com']
#     }
#     response = client.post('/visited_links', json=links)
#     assert response.status_code == 200
#     assert response.json() == {"status": "success", "message": "success", "data": []}

# def test_validation_error_response():
#     links = {
#         'links': [1, 2, 3, ]
#     }
#     response = client.post('/visited_links', json=links)
#     assert response.status_code == 422

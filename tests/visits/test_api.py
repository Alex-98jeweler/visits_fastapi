from datetime import datetime

from httpx import AsyncClient


async def test_success_resposne(ac: AsyncClient):
    links = {
        'links': [
            'https://example1.com',
            'https://example2.com',
            'https://example3.com'
        ]
    }
    response = await ac.post('/visited_links', json=links)
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "success",
        "data": []
    }


async def test_validation_error_response(ac: AsyncClient):
    links = {
        'links': [1, 2, 3, ]
    }
    response = await ac.post('/visited_links', json=links)
    assert response.status_code == 422


async def test_get_domains(ac: AsyncClient):
    response = await ac.get("/visited_domains")
    json = response.json()
    assert response.status_code == 200
    assert json['status'] == 'success'


async def test_get_with_params(ac: AsyncClient):
    response = await ac.get(
        '/visited_domains',
        params={
            'from_': datetime.now().timestamp() - 3600,
            'to': datetime.now().timestamp()
        }
    )
    json = response.json()
    assert json['status'] == 'success'


async def test_get_with_wrong_params(ac: AsyncClient):
    response = await ac.get(
        '/visited_domains',
        params={
            'from_': 'wrong1',
            'to': 'wrong2'
        }
    )
    assert response.status_code == 422

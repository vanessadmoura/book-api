from tests.utils.create_book import create_response_successful_generate, create_valid_book, create_valid_list_book


def test_get_all_books_when_successfully(client, mocker):
    list_books_mock = mocker.MagicMock(return_value=create_valid_list_book())
    mocker.patch("controller.book_controller.get_all_book", list_books_mock)

    response = client.get("/api/v1/book")

    assert response.status_code == 200
    assert len(response.json) == 2

    
def test_get_book_by_id_when_successfully(client, mocker):
    list_book_mock = mocker.MagicMock(return_value=create_valid_book())
    mocker.patch("controller.book_controller.get_book_by_id", list_book_mock)

    response = client.get("/api/v1/book/1")

    assert response.status_code == 200
    assert "id" in response.json
    assert "livro" in response.json
    assert "escritor" in response.json


def test_get_book_by_id_when_id_not_exits(client, mocker):
    list_book_mock = mocker.MagicMock(return_value=[])
    mocker.patch("controller.book_controller.get_book_by_id", list_book_mock)

    response = client.get("/api/v1/book/99")

    assert response.status_code == 200
    assert len(response.json) == 0


def test_register_book_when_successfully(client, mocker):
    body = {"livro": "anyvalue",
            "escritor": "anyvalue"}
    register_book_mock = mocker.MagicMock()
    mocker.patch("controller.book_controller.register_book", register_book_mock)
    
    response = client.post("/api/v1/book", json=body)

    assert response.status_code == 201
    assert "id" in response.json
    assert "livro" in response.json
    assert "escritor" in response.json


def test_modify_book_when_successfully(client, mocker):
    body = {"livro": "anyvalue",
            "escritor": "anyvalue"}
    modify_book_response_mock = mocker.MagicMock(return_value=create_response_successful_generate())
    mocker.patch("controller.book_controller.modify_book", modify_book_response_mock)

    response = client.put("/api/v1/book/1", json=body)
    assert response.status_code == 200


def test_delete_book_when_successfully(client, mocker):
    delete_book_mock = mocker.MagicMock()
    mocker.patch("controller.book_controller.delete_book", delete_book_mock)

    response = client.delete("/api/v1/book/1")

    assert response.status_code == 200
    assert "mensagem" in response.json


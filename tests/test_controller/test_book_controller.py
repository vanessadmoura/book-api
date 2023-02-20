from tests.utils.create_book import create_response_successful_generate, create_valid_book, create_valid_list_book


def test_get_all_books(client, mocker):
    list_books_mock = mocker.MagicMock(return_value=create_valid_list_book())
    mocker.patch("controller.book_controller.get_all_book", list_books_mock)

    response = client.get("/book")

    assert response.status_code == 200
    assert len(response.json) == 2

    
def test_get_book_by_id(client, mocker):
    list_book_mock = mocker.MagicMock(return_value=create_valid_book())
    mocker.patch("controller.book_controller.get_book_by_id", list_book_mock)

    response = client.get("/book/1")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_register_book(client, mocker):
    body = {"livro": "any_value",
            "escritor": "any_value"}
    register_book_mock = mocker.MagicMock()
    mocker.patch("controller.book_controller.register_book", register_book_mock)
    
    response = client.post("/book", json=body)

    assert response.status_code == 201
    assert "id" in response.json
    assert "livro" in response.json
    assert "escritor" in response.json


def test_modify_book(client, mocker):
    body = {"livro": "any_value",
            "escritor": "any_value"}
    modify_book_mock = mocker.MagicMock()
    mocker.patch("controller.book_controller.modify_book", modify_book_mock)

    response = client.put("/book/1", json=body)
    assert response.status_code == 200


def test_delete_book(client, mocker):
    delete_book_mock = mocker.MagicMock()
    mocker.patch("controller.book_controller.delete_book", delete_book_mock)

    response = client.delete("/book/1")

    assert response.status_code == 200
    assert "mensagem" in response.json
def test_get_all_books(client):
    response = client.get("/book")
    assert response.status_code == 200
    
def test_get_book_by_id(client):
    response = client.get("/book/1")
    assert response.status_code == 200

def test_register_book(client):
    body = {"livro": "Python",
            "escritor": "Igor"}
    response = client.post("/book", json=body)
    assert response.status_code == 201

def test_modify_book(client):
    body = {"livro": "Java",
            "escritor": "Igor"}
    response = client.put("/book/1", json=body)
    assert response.status_code == 200

def test_delete_book(client):
    response = client.delete("/book/1")
    assert response.status_code == 200
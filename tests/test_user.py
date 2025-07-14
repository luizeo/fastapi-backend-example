def test_create_user(client):
    response = client.post("/users/", json={
        "name": "Luiz",
        "email": "luizeduardo.unb@gmail.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Luiz"
    assert data["email"] == "luizeduardo.unb@gmail.com"

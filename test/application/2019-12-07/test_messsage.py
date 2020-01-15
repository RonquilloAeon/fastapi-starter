def test_message_create_list(test_client, version_header):
    payload = {"subject": "heyhey", "message": "testing"}
    create_response = test_client.post(
        "/messages",
        json=payload,
        headers=version_header
    )

    assert create_response.status_code == 201

    response = test_client.get("/messages", headers=version_header)
    results = response.json()

    assert len(results) == 1

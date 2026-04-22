def test_root_redirects_to_static_page(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_activities_items_have_expected_fields(client):
    response = client.get("/activities")
    data = response.json()

    required_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    assert data, "Expected at least one activity in the response"
    for details in data.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)

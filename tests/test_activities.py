def test_get_activities_returns_activity_collection(client):
    # Arrange
    # No special setup needed; the in-memory store already contains activities.

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]

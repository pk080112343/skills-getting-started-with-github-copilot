from src.app import activities


def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"
    activities[activity_name]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Removed {email} from {activity_name}"


def test_unregister_for_missing_email_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"
    activities[activity_name]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == f"{email} is not signed up for {activity_name}"

# Mergington High School Activities API

This project is a small FastAPI web application for managing extracurricular
activities at Mergington High School. The backend exposes JSON endpoints, while
the static frontend displays activity cards and provides signup and unregister
controls.

## Features and functionality

| Feature | Description |
| --- | --- |
| Activity directory | Lists each activity's description, schedule, participant limit, and current availability. |
| Activity signup | Registers a student's email for an existing activity. Duplicate registrations are rejected. |
| Participant management | Displays signed-up participants on each activity card. |
| Participant unregister | Removes a participant through the trash button next to their email. |
| Live activity updates | Refreshes the activity cards after signup or unregister, so changes appear without a browser reload. |
| Interactive API documentation | FastAPI provides Swagger UI at `/docs` and ReDoc at `/redoc`. |
| Backend test suite | Pytest tests the activity, signup, duplicate-signup, and unregister behavior using AAA (Arrange-Act-Assert). |

When new functionality is added, include a short description as a new row in
this table.

## Project structure

- `app.py`: FastAPI application, in-memory activity model, and API routes.
- `static/index.html`: page structure for the activity directory and signup form.
- `static/app.js`: loads activities, submits signups, and unregisters participants.
- `static/styles.css`: visual styling for the page and activity cards.
- `../tests/`: pytest backend tests.

## Getting started

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd src
uvicorn app:app --reload
```

Open the application at http://localhost:8000/:

- `/`: activity directory and signup form
- `/docs`: Swagger UI API documentation
- `/redoc`: alternative ReDoc API documentation

Run the backend tests from the repository root:

```bash
pytest tests -q
```

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/activities` | Returns all activities and their current participant lists. |
| POST | `/activities/{activity_name}/signup?email=student@mergington.edu` | Registers a participant; duplicate registrations return `400`. |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Removes a participant; unknown participants return `404`. |

## Data model and application logic

The application uses the `activities` dictionary in `app.py` as an in-memory
data model. Each activity uses its name as the identifier and contains:

- `description`: what students do in the activity.
- `schedule`: when the activity meets.
- `max_participants`: the enrollment limit used to calculate available spots.
- `participants`: a list of signed-up student email addresses.

The signup route first verifies that the activity exists and that the email is
not already registered, then appends the email to `participants`. The
unregister route verifies the activity and participant before removing the
email. Because the model is in memory, all changes reset when the server
restarts.

import requests

BASE_URL = "http://127.0.0.1:8000"


# Test the introduction and health endpoints.
for path in ["/", "/health"]:
    response = requests.get(BASE_URL + path, timeout=30)

    print("\nGET", path)
    print("Status:", response.status_code)
    print("Result:", response.json())

    assert response.status_code == 200


# Test two inputs with different sentiments.
sentences = [
    ("I love this movie. It was fantastic!", "POSITIVE"),
    ("This movie was terrible. I hated every minute of it.", "NEGATIVE"),
]

for text, expected_label in sentences:
    response = requests.post(
        BASE_URL + "/predict",
        json={"text": text},
        timeout=60,
    )

    print("\nInput:", text)
    print("Status:", response.status_code)
    print("Result:", response.json())

    assert response.status_code == 200
    assert response.json()["label"] == expected_label
    assert 0 <= response.json()["score"] <= 1


# Test empty text, a missing field, and an incorrect type.
invalid_inputs = [
    ({"text": "   "}, 400),
    ({}, 422),
    ({"text": 123}, 422),
]

for data, expected_status in invalid_inputs:
    response = requests.post(
        BASE_URL + "/predict",
        json=data,
        timeout=30,
    )

    print("\nInvalid input:", data)
    print("Status:", response.status_code)
    print("Result:", response.json())

    assert response.status_code == expected_status


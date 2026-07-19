import requests
import subprocess
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/photospicker.mediaitems.readonly"
]

def create_picker_session():
    creds = Credentials.from_authorized_user_file(
        "credentials/token.json",
        SCOPES
    )

    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://photospicker.googleapis.com/v1/sessions",
        headers=headers,
        json={}
    )

    result = response.json()

    print(result)

    # Open the official Google Photos Picker
    subprocess.run(["open", result["pickerUri"]])

    return result
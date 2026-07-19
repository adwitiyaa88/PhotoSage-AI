import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/photospicker.mediaitems.readonly"
]


def authenticate():
    # Already authenticated
    if os.path.exists("credentials/token.json"):
        print("Already authenticated.")
        return Credentials.from_authorized_user_file(
            "credentials/token.json",
            SCOPES
        )

    # First login
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials/client_secret.json",
        SCOPES
    )

    credentials = flow.run_local_server(port=0)

    os.makedirs("credentials", exist_ok=True)

    with open("credentials/token.json", "w") as token:
        token.write(credentials.to_json())

    print("Authentication successful.")
    return credentials
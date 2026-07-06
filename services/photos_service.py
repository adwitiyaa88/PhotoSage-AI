from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/photoslibrary.readonly"
]


def get_photos(limit=20):
    creds = Credentials.from_authorized_user_file(
        "credentials/token.json",
        SCOPES
    )

    # Refresh expired credentials
    if creds.expired and creds.refresh_token:
        print("Refreshing access token...")
        creds.refresh(Request())

        with open("credentials/token.json", "w") as token:
            token.write(creds.to_json())

    service = build(
        "photoslibrary",
        "v1",
        credentials=creds,
        static_discovery=False,
    )

    results = service.mediaItems().list(
        pageSize=limit
    ).execute()

    return results.get("mediaItems", [])
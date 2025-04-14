import os
from dotenv import load_dotenv
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Load environment variables from .env file
load_dotenv()

def upload_video(file_path, word):
    # Load the variables from environment
    description = os.getenv("YOUTUBE_DESCRIPTION")
    category_id = os.getenv("YOUTUBE_CATEGORY")
    privacy_status = os.getenv("YOUTUBE_PRIVACY")

    title = os.getenv("YOUTUBE_TITLE").replace("#1", word)


    # Set up OAuth 2.0 credentials
    creds = Credentials(
        None,
        refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["YOUTUBE_CLIENT_ID"],
        client_secret=os.environ["YOUTUBE_CLIENT_SECRET"],
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    creds.refresh(google.auth.transport.requests.Request())
    youtube = build('youtube', 'v3', credentials=creds)

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype='video/*')

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": category_id
            },
            "status": {
                "privacyStatus": privacy_status
            }
        },
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")

    print("Upload complete! Video ID:", response["id"])
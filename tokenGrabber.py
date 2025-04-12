# get_refresh_token.py
from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)
credentials = flow.run_console()
print("Refresh token:", credentials.refresh_token)

from google_auth_oauthlib.flow import InstalledAppFlow

# Set up OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# Open the authorization URL in the browser and let the user authenticate
credentials = flow.run_local_server(port=0)

# Output the refresh token
print("Refresh token:", credentials.refresh_token)

from __future__ import print_function
import pickle
import os.path
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
# SAMPLE_RANGE_NAME = "Class Data!A2:E"
SAMPLE_SPREADSHEET_ID = "1NuMUwl0KUgD0LkkD3ep3CNuIKqn9jGQKAzyTdG5qNNU"
SAMPLE_RANGE_NAME = "Sheet1!A1:B1"


def get_creds():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds


def get_sheet():
    creds = get_creds()
    service = build("sheets", "v4", credentials=creds)
    return service.spreadsheets()


def append():
    sheet = get_sheet()
    # result = (
    #     sheet.batchUpdate()
    #     .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
    #     .execute()
    # )
    body = {
        # How the input data should be interpreted.
        "value_input_option": "",  # TODO: Update placeholder value.
        # The new values to apply to the spreadsheet.
        "data": [],  # TODO: Update placeholder value.
        # TODO: Add desired entries to the request body.
    }

    request = sheet.values().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body)
    response = request.execute()
    return response


def view():
    sheet = get_sheet()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])
    if not values:
        print("No data found.")
    else:
        print("Name, Major:")
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(row)


if __name__ == "__main__":
    view()

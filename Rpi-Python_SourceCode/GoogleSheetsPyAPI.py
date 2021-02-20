# following tutorial from https://youtu.be/4ssigWmExak 


# un needed imports for now
# -----------------------------------------------------
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# ----------------------------------------------------

from googleapiclient.discovery import build
from google.oauth2 import service_account

def GoogleSheetsInit(svc_act_file_name,spreadsheet_id):
    global sheet
    global sheet_id
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # creds must equal None First Then Assigned the return of the function
    # don't know why yet...
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            svc_act_file_name, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    sheet_id = spreadsheet_id


def GetRange(r):
    global sheet
    global sheet_id
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range=r).execute()
    return (result.get('values', []))

def SetRange(r,v):
    global sheet
    global sheet_id
    request = sheet.values().update(spreadsheetId=sheet_id, 
                                    range=r, 
                                    valueInputOption="USER_ENTERED", 
                                    body={"values":v}).execute()

def AppendRange(r,v):
    global sheet
    global sheet_id
    request = sheet.values().append(spreadsheetId=sheet_id, 
                                    range=r, 
                                    valueInputOption="USER_ENTERED",
                                    insertDataOption="INSERT_ROWS", 
                                    body={"values":v}).execute()


def ClearRange(r):
    global sheet
    global sheet_id
    request = sheet.values().clear(spreadsheetId=sheet_id, 
                                    range=r).execute()


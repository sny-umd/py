
#from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

str_cl_id = 'primary'
strReturn = ''

def main():
    global strReturn
    
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    strReturn += now# + ','
    strReturn += "\r\n"
    dt_time_min = "2020-06-19T00:00:00.000000Z"
    dt_time_min = str(datetime.date.today()) + "T00:00:00.000000Z"
    #print(str(dt_time_min))

    strReturn += "\r\n"



    strReturn += 'shinya umeda'# + ','
    strReturn += "\r\n"

    #print(str_cl_id)
    strReturn += str_cl_id# + ','
    strReturn += "\r\n"

    #print('Getting the upcoming 10 events')
    strReturn += '10events'# + ','
    events_result = service.events().list(calendarId=str_cl_id,
                                          timeMin=dt_time_min,
                                          maxResults=10, 
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    strReturn += "\r\n"

    if not events:
        #print('No upcoming events found.')
        strReturn += 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        #print(start, event['summary'])
        strReturn += start + event['summary']# + ","
        strReturn += "\r\n"

    print(strReturn)


if __name__ == '__main__':
    main()
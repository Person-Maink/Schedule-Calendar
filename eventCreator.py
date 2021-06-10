from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

subjectColor = {"Electronics Engineering": '5',
    "Engineering Mathematics 2": '11',
    "Engineering Chemistry": '7',
    "Engineering Workshop": '4',
    "Communication Skills": '3',
    "Material Science and Engineering": '10',
    "Communication Skills Lab": '9',
    "Engineering Chemistry Lab": '9',
    "Electrical Engineering Lab": '9'}

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main(subjectName, date, startTime, endTime):

    global color
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
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    color = '2'

    event = {
        'summary': subjectName,

        'start': {
            'dateTime': date + 'T' + startTime + '+05:30',
            'timeZone': 'Asia/Calcutta',
        },
        'end': {
            'dateTime': date + 'T' + endTime + '+05:30',
            'timeZone': 'Asia/Calcutta',
        },

        'colorId': subjectColor[subjectName],

        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='c_n6hqe7iuclljn73u36489ese3o@group.calendar.google.com', body=event).execute()
    #print('Event created')


if __name__ == '__main__':  # this is piece of code that runs when the main script being run is this one. If this
    # script is used as a module and imported somewhere else
    main()  # then nothing in this code block is run. during runtime, there is a special variable called Main,
    # which gets assigned to name. Hence, if this is true, then the whole code block above is run. If not (which is
    # the case when this script is being used as a module) then this block is never run.


from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
# from .models import BroadInsightsConditions
from oauth2client.service_account import ServiceAccountCredentials

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
# CLIENT_SECRET_FILE = 'key_file.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

# scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     'key_file.json', scopes=scopes)


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def getData():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    spreadsheetId = '15-1xegxsfH-f_0poJKKboS-F0l3qT44gpc3lTY3yjXo'
    rangeName = 'Class Data!A2:E'
    rangeName = 'Sheet1!A3:P5'
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheetId, ranges=rangeName, valueRenderOption='UNFORMATTED_VALUE').execute()

    values = result['valueRanges'][0]['values']
    print(values)

    # for row in values:
    #     print('inside loop')
    #     # Print columns A and E, which correspond to indices 0 and 4.
    #     obj = BroadInsightsConditions(rule_id=row[0], sub_rule_id=row[1], subject=row[2], versions=row[3],
    #                                   priority=row[4]
    #                                   , rule_title=row[5], derived=row[6], derived_from=row[7], dt_14764=row[8],
    #                                   mt_25196=row[9], mt_26007=row[10], mt_27905=row[11], mt_28065=row[12]
    #                                   , condition_data=row[13], insight=row[14])
    #     obj.save()
    #     print('saved data')



    #
    # values = result.get('values', [])
    # import json
    #
    # print(json.dumps(result,sort_keys=False, indent=4))
    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         print('saved data')
    #         print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    getData()



from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
# from .models import BroadInsightsConditions
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import json
from httplib2 import Http
from .models import BroadInsightsConditions

def data():
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    file_name = os.getcwd() + '/profileadd/key_file.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        file_name, scopes=scopes)

    http_auth = credentials.authorize(Http())

    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = build('sheets', 'v4', http=http_auth,discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '15-1xegxsfH-f_0poJKKboS-F0l3qT44gpc3lTY3yjXo'
    rangeName = 'Sheet1!A2:P10'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName, valueRenderOption= 'UNFORMATTED_VALUE',
        majorDimension='ROWS').execute()
    # print(result)
    print(json.dumps(result, sort_keys=False, indent=4))

    # get number of rows and columns
    result = service.spreadsheets().get(
        spreadsheetId=spreadsheetId, fields='sheets.properties').execute()
    print(json.dumps(result["sheets"][0]["properties"], sort_keys=False, indent=4))
    result_fetched = result["sheets"][0]["properties"]['gridProperties']

    sheet_title = result["sheets"][0]["properties"]['title']
    row_count = result_fetched['rowCount']
    frozen_column_count = result_fetched['frozenColumnCount']
    column_count = result_fetched['columnCount']
    frozen_row_count = result_fetched['frozenRowCount']

    actual_row_count = row_count - frozen_row_count
    actual_column_count = column_count - frozen_column_count

    range_name = sheet_title+'!'+'A'+str(frozen_row_count)+':'+'P'+str(actual_row_count)
    print(range_name)
    if actual_row_count is not 0 or None and actual_column_count is not 0 or None:
        print('hello')


    # values = result['valueRanges'][0]['values']

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
    # values = result['valueRanges'][0]['values']
    # print(values)


    # result = service.spreadsheets().values().batchGet(
    # spreadsheetId=spreadsheetId, ranges=rangeName, valueRenderOption='UNFORMATTED_VALUE').execute()



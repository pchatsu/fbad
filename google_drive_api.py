#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import os
import io

from apiclient import discovery
#from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaIoBaseDownload

import const

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.path.join(const.APP_DIR, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'credential.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        raise ".credentials/ is something wrong. Please execute get_credential.py"
    return credentials

class GoogleDriveApi:
    def __init__(self):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)

    # get video file list
    def sync_video_file_list(self):
        param = {}
        #param['q'] = "'%s' in parents and mimeType contains 'video/'" % folder_id
        param['q'] = "mimeType contains 'video/'"
        return self.sync_all_item_list(param)

    # call list api
    def sync_all_item_list(self, param):
        """
        `param` reference https://developers.google.com/drive/v3/web/search-parameters
        """
        item_list = []
        page_token = None
        while True:
            try:
                if page_token:
                    param['pageToken'] = page_token

                response = self.service.files().list(**param).execute()
                # push file metadata
                item_list += response.get('files', [])
                page_token = response.get('nextPageToken', None)
                if not page_token:
                    break
            except errors.HttpError, error:
                raise Exception('APIリクエストに失敗しました error: %s' % error)
        return item_list

    # call download
    def download_file(self, file_id, local_file_name):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(local_file_name, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            try:
                status, done = downloader.next_chunk()
                print 'Download %d' % int(status.progress() * 100)
            except errors.HttpError, error:
                raise Exception('ダウンロード処理に失敗しました error: %s' % error)

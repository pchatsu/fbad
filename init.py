#!/usr/bin/env python
# -*- coding: utf-8 -*

import argparse
import os
import re
import sys

import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file

import const

"""oauthを発行するために叩くスクリプト
jenkins環境で実行する。
% python init.py --noauth_local_webserver
※ --noauth_local_webserverをつけないと、実行した環境のデフォルトブラウザを実行してしまうので注意
/home/game/git/sg-kaito/dev/tools/master_sync/.credentials に認証情報を保存する。
oauth関連のエラーが出た場合はこのスクリプトで初期化する。
"""

SCOPES           = 'https://www.googleapis.com/auth/drive'
APPLICATION_NAME = 'fbad'

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

credential_dir = os.path.join(const.APP_DIR, '.credentials')

def init_credentials(client_secret_path):
    """Credentialsの初期化

    JSON形式で認証情報を書き込む
    JSONをJenkinsサーバにおけば認証をもらった状態でAPIを叩けるようになる
    """
    credential_path = os.path.join(credential_dir, 'credential.json')

    store = file.Storage(credential_path)
    flow = client.flow_from_clientsecrets(client_secret_path, SCOPES)
    flow.user_agent = APPLICATION_NAME
    credentials = tools.run_flow(flow, store, flags)
    print 'Storing credentials to ' + credential_path
    return

def main():
    """ Input: client_id, client_secret
        Output: JSON (need for google-api-python-client)
    """
    if not os.path.exists(credential_dir):
	print 'mkdir .credentials'
        os.makedirs(credential_dir)
        print 'You should copy client_secret JSON file to .credentials/client_secret.json'
        print 'access to https://console.developers.google.com/apis/credentials'
        return

    client_secret_path = os.path.join(credential_dir, 'client_secret.json')
    if not os.path.exists(client_secret_path):
        print 'You should copy client_secret JSON file to .credentials/client_secret.json'
        print 'access to https://console.developers.google.com/apis/credentials'
        return

    init_credentials(client_secret_path)

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import *
from google_drive_api import *
from datetime import datetime


def register_new_gd_video():
    # DB
    db = DB()

    gd_api = GoogleDriveApi()
    gd_video_list = gd_api.sync_video_file_list()

    new_gd_video_list = []
    # register new video
    for gd_video in gd_video_list:
        # if not exists gd_video
        if not db.select_gd_video(gd_video['id']):
            timestamp = datetime.now().strftime('%s')
            db.insert_gd_video((gd_video['id'], gd_video['name'], timestamp))
            new_gd_video_list.append(gd_video)
            print 'new video id:%s name:%s' % (gd_video['id'], gd_video['name'])

    # commit
    db.commit()

def main():
    register_new_gd_video()

    # TODO account の管理
    #アップの計画を立てる
    # TODO videoのアップ形跡がない場合upload

if __name__ == '__main__':
    main()

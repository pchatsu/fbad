#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

DB_NAME = 'fbad.db'

# siple sql wrapper

class DB:
    def __init__(self):
        self.con = sqlite3.connect(DB_NAME)

    def close(self):
        self.con.close()

    def commit(self):
        self.con.commit()

    def select_gd_video(self, file_id):
        c = self.con.cursor()
        stmt = 'select id from gd_video where id = ?'
        params = (file_id,)
        c.execute(stmt, params)
        return c.fetchone()

    def insert_gd_video(self, gd_video_tuple):
        c = self.con.cursor()
        stmt = 'insert into gd_video values (?, ?, ?)'
        c.execute(stmt, gd_video_tuple)

    def insert_fb_account(self, fb_account_tuple):
        c = self.con.cursor()
        stmt = 'insert into fb_account values (?, ?, ?)'
        c.execute(stmt, fb_account_tuple)

"""
# 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
# executemanyメソッドを実行する
insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
users = [
    (2, 'Shota', 54, 'male'),
    (3, 'Nana', 40, 'female'),
    (4, 'Tooru', 78, 'male'),
    (5, 'Saki', 31, 'female')
]
c.executemany(insert_sql, users)
conn.commit()

select_sql = 'select * from users'
for row in c.execute(select_sql):
    print(row)

conn.close()
"""

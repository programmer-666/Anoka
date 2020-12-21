import sqlite3, os
class Connection_Functions:
    __DBNAME__ = "anoka_.db"
    def __init__(self):
        pass
# CONNECTION FUNCTIONS

class Database_Setup(Connection_Functions):
    def __init__(self):
        print(self.__DBNAME__)
# DATABASE SETUP

import sqlite3, os, hashlib
class Anoka_DB_Transaction_Module:
    __dbname="anoka_.db"
    def __databaseConnect(self,):
        self.__connection = sqlite3.connect(self.__dbname)
        self.__cursor = self.__connection.cursor()
    def __databaseCommit(self):
        self.__connection.commit()
    def __databaseDisconnect(self):
        self.__connection.close()
    def isDatabaseExist(self):
        if [i for i in os.listdir() if i == self.__dbname]:
            return 1
        else:
            return 0
class Anoka_DB_Creating(Anoka_DB_Transaction_Module):
    def __init__(self):
        if not self.isDatabaseExist(): # file control structure [if]
            # TAKING DATABASE NAME
            self._Anoka_DB_Transaction_Module__databaseConnect()
            # CONNECTION AND CURSOR
            usersTableSQL = "CREATE TABLE USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);"
            adminsTableSQL = "CREATE TABLE ADMINS (id_admin INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user));"
            messagesTableSQL = "CREATE TABLE MESSAGES (id_message INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user), message TEXT NOT NULL);"
            #onlinesTableSQL = "CREATE TABLE ONLINES (id_user INT NOT NULL REFERENCES USERS(id_user));"
            self._Anoka_DB_Transaction_Module__cursor.execute(usersTableSQL)
            self._Anoka_DB_Transaction_Module__cursor.execute(adminsTableSQL)
            self._Anoka_DB_Transaction_Module__cursor.execute(messagesTableSQL)
            #self._Anoka_DB_Transaction_Module__cursor.execute(onlinesTableSQL)
            # CREATING TABLES
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO USERS (username, password) VALUES ('programmer-666', '%s')"%hashlib.md5(bytes("qwerty".encode())).hexdigest())
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO USERS (username, password) VALUES ('jPR', '%s')"%hashlib.md5(bytes("jPRSECRET".encode())).hexdigest())
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO USERS (username, password) VALUES ('freeman', '%s')"%hashlib.md5(bytes("heisfree".encode())).hexdigest())
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO USERS (username, password) VALUES ('slayer', '%s')"%hashlib.md5(bytes("slayer".encode())).hexdigest())
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO USERS (username, password) VALUES ('player', '%s')"%hashlib.md5(bytes("qwerty123".encode())).hexdigest())
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO ADMINS (id_user) VALUES (1);")
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (1, 'hello');")
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (2, 'hi, is it working?');")
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (1, 'maybe, im still testing...');")
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (3, 'well');")
            self._Anoka_DB_Transaction_Module__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (4, 'good');")
            # ADDING SOME VALUES
            self._Anoka_DB_Transaction_Module__databaseCommit()
            self._Anoka_DB_Transaction_Module__databaseDisconnect()
            # COMMIT AND CLOSE
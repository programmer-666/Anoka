"""
    NOTLAR
    -BİR KAÇ YENİ MESAJ EKLE
    -MESAJLARIN ÇEKMEK İÇİN FOKNSİYON (TANE VE ÇOKLU)
    -VERİTABANI HAZIR ÇOK KURCALAMA
"""
import sqlite3
import hashlib

class mainClass:
    __ONLINE_USERS  = set()
    __OFFLINE_USERS = set()
    
    def __init__(self):
        #self.createDatabase()# just run one time
        self.getTables()
    def getTables(self):
        self.__databaseConnect()
        # DATABASE CONNECTION
        self.__USERS    = [i for i in self.__cursor.execute("SELECT id_user, username FROM USERS;").fetchall()]
        self.__ADMINS   = [i for i in self.__cursor.execute("SELECT * FROM ADMINS;").fetchall()]
        self.__MESSAGES = [i for i in self.__cursor.execute("SELECT * FROM MESSAGES;").fetchall()]
        # TAKING TABLES
        self.__databaseDisconnect()
    # DATABASE CREATING 
    def createDatabase(self, dbname = "anoka_.db"):
        self.__dbname = dbname
        # TAKING DATABASE NAME
        self.__databaseConnect()
        # CONNECTION AND CURSOR
        usersTableSQL = "CREATE TABLE USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);"
        adminsTableSQL = "CREATE TABLE ADMINS (id_admin INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user));"
        messagesTableSQL = "CREATE TABLE MESSAGES (id_message INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user), message TEXT NOT NULL);"
        self.__cursor.execute(usersTableSQL)
        self.__cursor.execute(adminsTableSQL)
        self.__cursor.execute(messagesTableSQL)
        # CREATING TABLES
        self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('programmer-666', '%s')"%hashlib.md5(bytes("qwerty".encode())).hexdigest())
        self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('jPR', '%s')"%hashlib.md5(bytes("jPRSECRET".encode())).hexdigest())
        self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('freeman', '%s')"%hashlib.md5(bytes("heisfree".encode())).hexdigest())
        self.__cursor.execute("INSERT INTO ADMINS (id_user) VALUES (1);")
        self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (1, 'well, guys hi');")
        # ADDING SOME VALUES
        self.__databaseCommit()
        self.__databaseDisconnect()
        # COMMIT AND CLOSE
    # DATABASE CREATING
    # DATABASE FUNCTIONS
    def __databaseConnect(self, dbname="anoka_.db"):
        self.__dbname = dbname
        self.__connection = sqlite3.connect(self.__dbname)
        self.__cursor = self.__connection.cursor()
    def __databaseCommit(self):
        self.__connection.commit()
    def __databaseDisconnect(self):
        self.__connection.close()
    # DATABASE FUNCTIONS
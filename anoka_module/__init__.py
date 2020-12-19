import sqlite3, hashlib, os
class mainClass:
    #__ONLINE_USERS  = set()
    #__OFFLINE_USERS = set()
    def __init__(self):
        """ INSIDE """
        self.createDatabase()# just run one time
        self.getTables()
        self.showMessages()
    def getTables(self):
        self.__databaseConnect()
        # DATABASE CONNECTION
        self.__USERS    = [i for i in self.__cursor.execute("SELECT id_user, username FROM USERS;").fetchall()]
        self.__ADMINS   = [i for i in self.__cursor.execute("SELECT * FROM ADMINS;").fetchall()]
        self.__MESSAGES = [i for i in self.__cursor.execute("SELECT * FROM MESSAGES;").fetchall()]
        # TAKING TABLES
        #print(self.__USERS, self.__ADMINS, self.__MESSAGES, sep="\n")
        self.__databaseDisconnect()
    # DATABASE CREATING 
    def createDatabase(self, dbname = "anoka_.db"):
        if not self.isDatabaseExist(): # file control structure [if]
            self.__dbname = dbname
            # TAKING DATABASE NAME
            self.__databaseConnect()
            # CONNECTION AND CURSOR
            usersTableSQL = "CREATE TABLE USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);"
            adminsTableSQL = "CREATE TABLE ADMINS (id_admin INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user));"
            messagesTableSQL = "CREATE TABLE MESSAGES (id_message INTEGER PRIMARY KEY AUTOINCREMENT, id_user INT NOT NULL REFERENCES USERS(id_user), message TEXT NOT NULL);"
            #onlinesTableSQL = "CREATE TABLE ONLINES (id_user INT NOT NULL REFERENCES USERS(id_user));"
            self.__cursor.execute(usersTableSQL)
            self.__cursor.execute(adminsTableSQL)
            self.__cursor.execute(messagesTableSQL)
            #self.__cursor.execute(onlinesTableSQL)
            # CREATING TABLES
            self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('programmer-666', '%s')"%hashlib.md5(bytes("qwerty".encode())).hexdigest())
            self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('jPR', '%s')"%hashlib.md5(bytes("jPRSECRET".encode())).hexdigest())
            self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('freeman', '%s')"%hashlib.md5(bytes("heisfree".encode())).hexdigest())
            self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('slayer', '%s')"%hashlib.md5(bytes("slayer".encode())).hexdigest())
            self.__cursor.execute("INSERT INTO USERS (username, password) VALUES ('player', '%s')"%hashlib.md5(bytes("qwerty123".encode())).hexdigest())
            self.__cursor.execute("INSERT INTO ADMINS (id_user) VALUES (1);")
            self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (1, 'hello');")
            self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (2, 'hi, is it working?');")
            self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (1, 'maybe, im still testing...');")
            self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (3, 'well');")
            self.__cursor.execute("INSERT INTO MESSAGES (id_user, message) VALUES (4, 'good');")
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
    def isDatabaseExist(self, dbname="anoka_.db"):
        if [i for i in os.listdir() if i == dbname]:
            return 1
        else:
            return 0
    # DATABASE FUNCTIONS
    # USER FUNCTIONS
    def findUsernameByID(self, idu):
        for i in self.__USERS:
            if int(i[0]) == int(idu):
                return i[1]
                break
    # USER FUNCTIONS
    # MESSAGE FUNCTIONS
    def showMessages(self):
        for i in self.__MESSAGES:
            print(f"[ {self.findUsernameByID(i[1])} ]> {i[2]}")
    # MESSAGE FUNCTIONS
    """ INSIDE """
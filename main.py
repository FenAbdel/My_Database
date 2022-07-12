import json


class database:
    def __init__(self):
        with open("db.json") as f:
            self.db = json.load(f)

    def Jsondump(self):
        with open("db.json", "w+") as of:
            json.dump(self.db, of)

    def createDb(self, command):
        command = command.replace('create db ', '')
        self.db[command] = {}
        self.Jsondump()

    def createTable(self, command, database):
        command = command.replace('create table ', '')
        soket = command.split("(")
        tablename = soket[0].strip()
        fields = soket[1].replace(")", "")
        field = fields.split(",")

        self.db[database][tablename] = {}
        self.db[database][tablename]["name"] = {}
        self.db[database][tablename]["type"] = []
        for i in field:
            i = i.strip()
            splited = i.split(" ")
            self.db[database][tablename]["name"][splited[0].strip()] = []
            self.db[database][tablename]["type"].append(splited[1].strip())
        self.Jsondump()

    def isdbfoundeded(self, command):
        try:
            n = self.db[command]
            return True
        except:
            return False

    def deleteTable(self, command, database):
        command = command.replace("delete table ", "")
        del self.db[database][command]
        self.Jsondump()

    def deleteDb(self, database):
        command = database.replace("delete ", "")
        del self.db[command]
        self.Jsondump()


db = database()

commandlist = int(input("if you need the command list please press 1 : "))
if commandlist == 1:
    print('to create a database :  create db database_name\n'
          'to create table : create table table_name (field_name1 type ,field_name2 type...)\n'
          'to delete table : delete table table_name\n'
          'to delete datable : delete database_name\n'
          'to exit : exit')

database = input('select your database (if isn\'t exit press 0) : ')
if database == "0":
    command = input()
    db.createDb(command)
    database = input("select your database :")

if db.isdbfoundeded(database):
    while True:
        command = input()
        if command == "exit":
            break
        kw = command.split(" ")
        if kw[0] == "create":
            if kw[1] == "table" :
                db.createTable(command, database)
                print("table was created sucessfully")
        elif kw[0] == "delete":
            if kw[1] == "table":
                db.deleteTable(command, database)
                print("table was deleted sucessfully")
            elif len(kw) == 2:
                db.deleteDb(command)
                print("database was deleted sucessfully")

else:
    print("database not founded")


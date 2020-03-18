import json
from datetime import datetime

class Journal:
    def __init__(self, path = 'lifedata.json'):
        self.path = path
        with open(path, 'r') as rawFile:
            openFile = rawFile.read()
            self.str = str(openFile)
            self.journal = json.loads(openFile)

    def getDict(self):
        return self.journal

    def __str__(self):
        return self.str

    def write(self):
        with open(self.path, 'w') as saveFile:
            saveFile.write(json.dumps(self.journal, indent=2))

    def newEntry(self, title, message, write = True):
        entry = {
            str(datetime.now()): {
                'title': title,
                'body': message
            }
        }
        self.journal.update(entry)

        if write == True: self.write()

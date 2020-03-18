import json
from datetime import datetime

class Journal:
    def __init__(self, path = 'lifedata.json'):
        self.path = path
        with open(path) as rawFile:
            self.journal = json.loads(rawFile.read())

    def getData(self):
        return self.journal

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

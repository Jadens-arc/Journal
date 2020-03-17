import json
from datetime import datetime

class Journal:
    def __init__(self, path = 'lifedata.json'):
        self.path = path
        with open(path) as rawFile:
            self.journal = json.loads(rawFile)

    def write(self):
        with open(self.path, 'w') as saveFile:
            saveFile.write(json.dumps(self.journal))

    def newEntry(self, title, message, write = True):
        entry = {
            datetime.now(): {
                'title': title,
                'body': message
            }
        }
        Journal.update(entry)

        if write == True: self.write()

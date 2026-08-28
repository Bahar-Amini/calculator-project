class History:
    def __init__(self, storage):
        self.info = []
        self.storage = storage

    def add(self, expression, result):
        self.info.append({"expression": expression, "result": result})

        self.storage.save(self.info)

    def get_history(self):
        for item in self.storage.load():
            print(item)

    def delete(self):
        self.storage.delete_history()
        self.storage.load()

class History:
    def __init__(self, storage):
        self.storage = storage
        self.operations = self.storage.load()

    def add(self,expression,result):
        self.operations.append({
            "expression" : expression,
            "result": result
        })

        self.storage.save(self.operations)

    def get_history(self):
        return self.operations


        
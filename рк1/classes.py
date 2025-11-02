class Orchestra: #класс "оркестр"
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Musician: #класс "музыкант"
    def __init__(self, id, name, salary, orchestra_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.orchestra_id = orchestra_id

class MusiciansOrchestras: #для множественной связи м:м
    def __init__(self, orchestra_id, musician_id):
        self.orchestra_id = orchestra_id
        self.musician_id = musician_id
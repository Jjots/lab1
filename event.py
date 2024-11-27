class Event:
    def __init__(self, name, date, location, description):
        self.name = name
        self.date = date
        self.location = location
        self.description = description
    
    def get_event_info(self):
        return f"Событие: {self.name}\nДата: {self.date}\nМесто: {self.location}\nОписание: {self.description}"
    
   
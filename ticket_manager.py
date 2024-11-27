from ticket import RegularTicket, VIPTicket  
from booking import Booking  
from exceptions import TicketAlreadyBookedError  

class TicketManager:
    def __init__(self):
        self.events = []
        self.bookings = []
    
    def add_event(self, event): #добавляет событие
        self.events.append(event)
    
    def create_booking(self, tickets): #создает бронирование для билетов
        booking = Booking(tickets)
        self.bookings.append(booking)
    
    def get_all_events(self):
        return [event.get_event_info() for event in self.events]

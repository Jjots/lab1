from abc import ABC, abstractmethod
from exceptions import TicketAlreadyBookedError

class Ticket(ABC):
    def __init__(self, price, event):
        self.price = price
        self.event = event
        self.booking_date = None
    
    @abstractmethod
    def get_ticket_info(self):
        pass
    
    def book_ticket(self): #бронь
        if self.booking_date is not None:
            raise TicketAlreadyBookedError("Билет уже забронирован.")
        self.booking_date = "Текущая дата" 
    
    def cancel_booking(self): # отмена брони
        self.booking_date = None

class RegularTicket(Ticket):
    def get_ticket_info(self):
        return f"Обычный билет на событие: {self.event.name}, Цена: {self.price} руб."

class VIPTicket(Ticket):
    def __init__(self, price, event, privileges):
        super().__init__(price, event)
        self.privileges = privileges
    
    def get_ticket_info(self):
        return f"VIP билет на событие: {self.event.name}, Цена: {self.price} руб., Привилегии: {self.privileges}"

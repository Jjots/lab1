class Booking:
    def __init__(self, tickets):
        self.tickets = tickets
        self.booking_date = "Текущая дата"
        self.status = "Подтверждено"
    
    def cancel_booking(self): #отмена брони билета
        self.status = "Отменено"
        for ticket in self.tickets:
            ticket.cancel_booking()
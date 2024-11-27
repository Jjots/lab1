from ticket import RegularTicket, VIPTicket
from ticket_manager import TicketManager
from event import Event  
from exceptions import TicketAlreadyBookedError
from booking import Booking
import storage


ticket_manager = TicketManager()

event1 = Event(name="Концерт Rammstein", date="30.07.2019", location="Москва", description="имба")
event2 = Event(name="Нашествие", date="10.08.2002", location="Раменское", description="база")

ticket_manager.add_event(event1)
ticket_manager.add_event(event2)

events_data = ticket_manager.get_all_events()
storage.save_to_json("events.json", events_data)

print("Список всех событий:")
for event_info in ticket_manager.get_all_events():
    print(event_info)


# Создание билетов
regular_ticket1 = RegularTicket(price=100000, event=event1)
vip_ticket1 = VIPTicket(price=3000000000, event=event1, privileges="Доступ в VIP-зону")

print("\nИнформация о билетах:")
print(regular_ticket1.get_ticket_info())
print(vip_ticket1.get_ticket_info())

# Создание бронирования
try:
    regular_ticket1.book_ticket()
    print(f"\nБронирование для билета на {regular_ticket1.event.name} успешно создано.")
    
    vip_ticket1.book_ticket()
    print(f"Бронирование для VIP билета на {vip_ticket1.event.name} успешно создано.")
    
    print("\nПопытка повторного бронирования обычного билета:")
    regular_ticket1.book_ticket() 
    
except TicketAlreadyBookedError as e:
    print(f"Ошибка при бронировании билета: {e}")

# Создание бронирования для нескольких билетов
booking = Booking([regular_ticket1, vip_ticket1])
ticket_manager.create_booking([regular_ticket1, vip_ticket1])
print("\nБронирование для нескольких билетов успешно создано.")

# Отмена бронирования
print("\nОтмена бронирования для всех билетов:")
booking.cancel_booking()
print(f"Статус бронирования: {booking.status}")
print(f"Статус обычного билета: {regular_ticket1.booking_date}")
print(f"Статус VIP билета: {vip_ticket1.booking_date}")


for event_info in ticket_manager.get_all_events():
    print("/////////////////")
    print(event_info)



from entity.Venue import Venue
from entity.Customer import Customer
from entity.Event import Event
from entity.Booking import Booking

from dao.VenueDAOImpl import VenueDAOImpl
from dao.CustomerDAOImpl import CustomerDAOImpl
from dao.EventDAOImpl import EventDAOImpl
from dao.BookingDAOImpl import BookingDAOImpl

from exception.EventNotFoundException import EventNotFoundException
from exception.InvalidBookingIDException import InvalidBookingIDException
from exception.NullPointerException import NullPointerException

def main():
    venue_dao = VenueDAOImpl()
    customer_dao = CustomerDAOImpl()
    event_dao = EventDAOImpl()
    booking_dao = BookingDAOImpl()

    while True:
        print("\n--- Ticket Booking System Menu ---")
        print("1. Create Venue")
        print("2. Create Event")
        print("3. Create Customer")
        print("4. Book Tickets")
        print("5. Cancel Booking")
        print("6. View All Events")
        print("7. View All Bookings")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter venue name: ")
                address = input("Enter venue address: ")
                if not name or not address:
                    raise NullPointerException("Venue name or address cannot be empty.")
                venue = Venue(None, name, address)
                venue_dao.insert_venue(venue)
                print("Venue added successfully.")

            elif choice == "2":
                name = input("Enter event name: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                venue_id = int(input("Enter venue ID: "))
                total_seats = int(input("Enter total seats: "))
                price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                event = Event(None, name, date, time, venue_id, total_seats, total_seats, price, event_type)
                event_dao.insert_event(event)
                print("Event added successfully.")

            elif choice == "3":
                name = input("Enter customer name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                if not name or not email or not phone:
                    raise NullPointerException("Customer information cannot be empty.")
                customer = Customer(None, name, email, phone)
                customer_dao.insert_customer(customer)
                print("Customer added successfully.")

            elif choice == "4":
                customer_id = int(input("Enter customer ID: "))
                event_id = int(input("Enter event ID: "))
                num_tickets = int(input("Enter number of tickets to book: "))

                event = event_dao.get_event_by_id(event_id)
                if event is None:
                    raise EventNotFoundException()

                if event.available_seats < num_tickets:
                    print("Not enough tickets available.")
                else:
                    total_cost = num_tickets * event.ticket_price
                    event.available_seats -= num_tickets
                    event_dao.update_event(event)
                    booking = Booking(None, customer_id, event_id, num_tickets, total_cost, None)
                    booking_dao.insert_booking(booking)
                    print(f"Booking successful! Total cost: ₹{total_cost}")

            elif choice == "5":
                booking_id = int(input("Enter Booking ID to cancel: "))
                booking = booking_dao.get_booking_by_id(booking_id)
                if booking is None:
                    raise InvalidBookingIDException()
                event = event_dao.get_event_by_id(booking.event_id)
                event.available_seats += booking.num_tickets
                event_dao.update_event(event)
                booking_dao.delete_booking(booking_id)
                print("Booking cancelled successfully.")

            elif choice == "6":
                events = event_dao.get_all_events()
                for ev in events:
                    ev.display_event_details()

            elif choice == "7":
                bookings = booking_dao.get_all_bookings()
                for b in bookings:
                    b.display_booking_details()

            elif choice == "8":
                print("Exiting Ticket Booking System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except (EventNotFoundException, InvalidBookingIDException, NullPointerException) as e:
            print(f"Error: {e}")

        except ValueError:
            print("Invalid input. Please enter the correct data type.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

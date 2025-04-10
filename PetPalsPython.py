from dao.pet_dao import PetDAO
from dao.donation_dao import DonationDAO
from dao.event_dao import AdoptionEventDAO
from entity.pet import Dog, Cat
from entity.donation import CashDonation, ItemDonation
from util.DBCONNUtil import DBCONNUtil

def main():
    try:
        conn = DBCONNUtil.get_connection()
        if conn is None:
            print("Connection failed. Exiting...")
            return

        pet_dao = PetDAO(conn)
        donation_dao = DonationDAO(conn)
        event_dao = AdoptionEventDAO(conn)

        while True:
            print("\n=== PetPals Adoption System ===")
            print("1. Add a Pet")
            print("2. View Available Pets")
            print("3. Make a Donation")
            print("4. View Adoption Events")
            print("5. Register for Event")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    name = input("Pet Name: ")
                    age = int(input("Age: "))
                    breed = input("Breed: ")
                    pet_type = input("Type (Dog/Cat): ").strip().lower()

                    if pet_type == 'dog':
                        dog_breed = input("Dog Breed: ")
                        pet = Dog(name, age, breed, dog_breed)
                    elif pet_type == 'cat':
                        cat_color = input("Cat Color: ")
                        pet = Cat(name, age, breed, cat_color)
                    else:
                        print("Invalid type. Only Dog or Cat allowed.")
                        continue

                    pet_dao.add_pet(pet)
                except Exception as e:
                    print("Failed to add pet:", e)

            elif choice == '2':
                try:
                    pet_dao.list_available_pets()
                except Exception as e:
                    print("Error listing pets:", e)

            elif choice == '3':
                try:
                    donor_name = input("Donor Name: ")
                    donation_type = input("Donation Type (Cash/Item): ").strip().lower()

                    if donation_type == 'cash':
                        amount = float(input("Amount: "))
                        date = input("Date (YYYY-MM-DD): ")
                        donation = CashDonation(donor_name, amount, date)
                    elif donation_type == 'item':
                        item_type = input("Item Type: ")
                        amount = int(input("Quantity: "))
                        donation = ItemDonation(donor_name, amount, item_type)
                    else:
                        print("Invalid donation type.")
                        continue

                    donation_dao.record_donation(donation)
                except Exception as e:
                    print("Error processing donation:", e)

            elif choice == '4':
                try:
                    event_dao.get_events()
                except Exception as e:
                    print("Error fetching events:", e)

            elif choice == '5':
                try:
                    event_id = int(input("Enter Event ID: "))
                    participant_name = input("Participant Name: ")
                    event_dao.register_participant(event_id, participant_name)
                except Exception as e:
                    print("Error registering participant:", e)

            elif choice == '6':
                print("Thank you for using PetPals. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()

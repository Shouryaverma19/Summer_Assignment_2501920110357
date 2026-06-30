total_seats = int(input("Enter total available seats in the theater/bus: "))
booked_seats = []
choice = 0

while choice != 4:
    print("\n--- Ticket Booking System ---")
    print("1. View Available Seats")
    print("2. Book a Seat")
    print("3. Cancel a Booking")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available seats are:")
        available_found = False
        for seat in range(1, total_seats + 1):
            if seat not in booked_seats:
                print(seat, end=" ")
                available_found = True
        print()
        if not available_found:
            print("House full! No seats available.")
    elif choice == 2:
        seat_to_book = int(input("Enter seat number to book: "))
        if seat_to_book < 1 or seat_to_book > total_seats:
            print("Invalid seat number.")
        elif seat_to_book in booked_seats:
            print("Seat is already booked.")
        else:
            booked_seats.append(seat_to_book)
            print(f"Seat {seat_to_book} booked successfully.")
    elif choice == 3:
        seat_to_cancel = int(input("Enter seat number to cancel booking: "))
        if seat_to_cancel in booked_seats:
            booked_seats.remove(seat_to_cancel)
            print(f"Booking for seat {seat_to_cancel} cancelled successfully.")
        else:
            print("This seat is not currently booked.")
    elif choice == 4:
        print("Exiting Ticket System.")
    else:
        print("Invalid choice.")
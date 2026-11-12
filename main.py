
guests = []
tables = []


def add_guest():
    print("\n--- ADD GUEST ---")

    name = input("Enter guest name: ").strip()

    if not name:
        print("Guest name cannot be empty.")
        return

    group = input("Enter group (Family/Friends): ").strip().lower()

    if group not in ["family", "friends"]:
        print("Please enter Family or Friends.")
        return

    meal = input("Enter meal preference (Veg/Non-Veg): ").strip().lower()

    if meal not in ["veg", "non-veg"]:
        print("Please enter Veg or Non-Veg.")
        return

    guest = {
        "id": len(guests) + 1,
        "name": name,
        "group": group.title(),
        "rsvp": "Pending",
        "meal": meal.title()
    }

    guests.append(guest)
    print("Guest added successfully!")


def view_guests():
    print("\n--- GUEST LIST ---")

    if not guests:
        print("No guests added yet.")
        return

    for guest in guests:
        print("--------------------------------")
        print("ID:", guest["id"])
        print("Name:", guest["name"])
        print("Group:", guest["group"])
        print("RSVP:", guest["rsvp"])
        print("Meal:", guest["meal"])


def update_rsvp():
    print("\n--- UPDATE RSVP ---")

    if not guests:
        print("No guests available.")
        return

    view_guests()

    try:
        guest_id = int(input("\nEnter guest ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for guest in guests:
        if guest["id"] == guest_id:
            print("1. Confirmed")
            print("2. Declined")

            choice = input("Select RSVP status: ").strip()

            if choice == "1":
                guest["rsvp"] = "Confirmed"
                print("RSVP updated to Confirmed.")

            elif choice == "2":
                guest["rsvp"] = "Declined"
                print("RSVP updated to Declined.")

            else:
                print("Invalid choice.")

            return

    print("Guest ID not found.")


def confirmed_headcount():
    print("\n--- CONFIRMED HEADCOUNT ---")

    count = 0

    for guest in guests:
        if guest["rsvp"] == "Confirmed":
            count += 1

    print("Total confirmed guests:", count)


def allocate_tables():
    global tables

    print("\n--- TABLE ALLOCATION ---")

    confirmed_guests = []

    for guest in guests:
        if guest["rsvp"] == "Confirmed":
            confirmed_guests.append(guest)

    if not confirmed_guests:
        print("No confirmed guests available for seating.")
        return

    try:
        capacity = int(input("Enter capacity of each table: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if capacity <= 0:
        print("Table capacity must be greater than zero.")
        return

    tables = []

    groups = ["Family", "Friends"]

    for group in groups:
        group_guests = []

        for guest in confirmed_guests:
            if guest["group"] == group:
                group_guests.append(guest)

        for guest in group_guests:
            if not tables or len(tables[-1]) >= capacity:
                tables.append([])

            if len(tables[-1]) + 1 > capacity:
                tables.append([])

            tables[-1].append(guest)

    print("\nTable allocation completed successfully!")

    for i, table in enumerate(tables):
        print("\nTable", i + 1)
        print("Guests:", len(table), "/", capacity)

        for guest in table:
            print("-", guest["name"], "(", guest["group"], ")")

    print("\nTotal tables required:", len(tables))


def meal_report():
    print("\n--- MEAL PREFERENCE REPORT ---")

    veg = 0
    non_veg = 0

    for guest in guests:
        if guest["rsvp"] == "Confirmed":
            if guest["meal"] == "Veg":
                veg += 1
            elif guest["meal"] == "Non-Veg":
                non_veg += 1

    print("Vegetarian meals required:", veg)
    print("Non-vegetarian meals required:", non_veg)


def seating_chart():
    print("\n--- SEATING CHART ---")

    if not tables:
        print("Please allocate tables first.")
        return

    for i, table in enumerate(tables):
        print("\nTable", i + 1)

        for guest in table:
            print("-", guest["name"], "|", guest["group"])


def main():
    while True:
        print("\n========== GUESTGRID ==========")
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Update RSVP")
        print("4. Show Confirmed Headcount")
        print("5. Allocate Tables")
        print("6. Meal Preference Report")
        print("7. Print Seating Chart")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_guest()

        elif choice == "2":
            view_guests()

        elif choice == "3":
            update_rsvp()

        elif choice == "4":
            confirmed_headcount()

        elif choice == "5":
            allocate_tables()

        elif choice == "6":
            meal_report()

        elif choice == "7":
            seating_chart()

        elif choice == "8":
            print("Thank you for using GuestGrid!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

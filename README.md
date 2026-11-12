# GuestGrid – Event Guest and Table Seating Manager

## About the Project

GuestGrid is a Python-based console application designed to make event guest management easier. It helps event organisers maintain guest details, track RSVP responses, manage meal preferences and arrange guests into tables.

The project reduces manual work and makes event seating and food planning more organised.

## Features

1. **Add Guest:** Add guest details such as name, group and meal preference.
2. **View Guests:** Display the complete list of registered guests.
3. **Update RSVP:** Change a guest's RSVP status to Confirmed or Declined.
4. **Confirmed Headcount:** Calculate the total number of confirmed guests.
5. **Allocate Tables:** Arrange confirmed guests into tables based on table capacity while keeping Family and Friends groups together wherever possible.
6. **Meal Preference Report:** Calculate the number of vegetarian and non-vegetarian meals required.
7. **Print Seating Chart:** Display the final table arrangement.

## Technologies Used

- Python
- Visual Studio Code
- GitHub

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

6. Follow the menu options displayed in the terminal.

## Menu Options

| Option | Function |
|---|---|
| 1 | Add Guest |
| 2 | View Guests |
| 3 | Update RSVP |
| 4 | Show Confirmed Headcount |
| 5 | Allocate Tables |
| 6 | Meal Preference Report |
| 7 | Print Seating Chart |
| 8 | Exit |

## Important Note

Guest information is stored temporarily while the program is running. The information is cleared when the application is closed.

## Conclusion

GuestGrid provides a simple and organised way to manage event guests, food preferences and seating arrangements using Python.

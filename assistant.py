import helper
from address_book import AddressBook, Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *[arg.strip() for arg in args]

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(helper.add_contact(args, book))
        elif command == "change":
            print(helper.change_contact(args, book))
        elif command == "phone":
            print(helper.get_phones_list(args, book))
        elif command == "all":
            print(helper.get_all_contacts(book))
        elif command == "add-birthday":
            print(helper.add_birthday(args, book))
        elif command == "show-birthday":
            print(helper.show_birthday(args, book))
        elif command == "birthdays":
            print(helper.get_upcoming_birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

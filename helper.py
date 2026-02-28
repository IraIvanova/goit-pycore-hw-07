from address_book import AddressBook, Record
from errors_handler import input_error
from exceptions import ContactNotFound, MandatoryArgumentsError


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise MandatoryArgumentsError("Please enter name and phone")

    name, phone, *_ = args
    contact = book.find(name)

    if not contact:
        contact = Record(name)

    contact.add_phone(phone)
    book.add_record(contact)

    return "Contact added."

@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise MandatoryArgumentsError("Please enter name, phone to change and new phone value")

    name, phone_to_edit, new_phone, *_ = args
    contact = book.find(name)

    if not contact:
        raise ContactNotFound("Contact not found")

    contact.edit_phone(phone_to_edit, new_phone)

    return "Contact changed."

@input_error
def get_phones_list(args, book: AddressBook):
    if len(args) < 1:
        raise MandatoryArgumentsError("Please enter name")

    contact = book.find(args[0])

    if not contact:
        raise ContactNotFound("Contact not found")

    return "; ".join(p.value for p in contact.phones)

def get_all_contacts(book: AddressBook):
    return "\n".join(f"{contact}" for contact in book.show_all())

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise MandatoryArgumentsError("Please enter name and date of birthday")

    name, birthday, *_ = args
    contact = book.find(name)

    if not contact:
        raise ContactNotFound("Contact not found")

    contact.add_birthday(birthday)

    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise MandatoryArgumentsError("Please enter name")

    contact = book.find(args[0])

    if not contact:
        raise ContactNotFound("Contact not found")
    elif not contact.birthday:
        return "Birthday is not set for this contact."

    return f"{contact.birthday}"

def get_upcoming_birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()
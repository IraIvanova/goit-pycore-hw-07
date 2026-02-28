from collections import UserDict
from exceptions import PhoneValidationError, ContactNotFound, PhoneNotFound, PhoneAlreadyExists, \
    EmptyName, BirthdayFormatError
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value.strip()
        self.validate()

    def validate(self):
        pass

    def __str__(self):
        return str(self.value)


class Name(Field):
    def validate(self):
        if len(self.value.strip()) == 0:
            raise EmptyName("Name cannot be empty")


class Phone(Field):
    def validate(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise PhoneValidationError(f"Phone number {self.value} is is incorrect! Phone number must be of 10 digits only")


class Birthday(Field):
    def validate(self):
        try:
            datetime.strptime(self.value, '%d.%m.%Y')
        except ValueError:
            raise BirthdayFormatError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if self.find_phone(phone):
            raise PhoneAlreadyExists(f"Phone number {phone} already added")

        self.phones.append(Phone(phone))

    def edit_phone(self, phone_to_edit, new_value):
        if not self.find_phone(phone_to_edit):
            raise PhoneNotFound(f"Phone number {phone_to_edit} not found")
        elif self.find_phone(new_value):
            raise PhoneAlreadyExists(f"New phone number value {new_value} already exists in list")

        for index, phone in enumerate(self.phones):
            if phone_to_edit == phone.value:
                self.phones[index] = Phone(new_value)

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)

        if not phone_obj:
            raise PhoneNotFound(f"Phone number {phone} not found")

        self.phones.remove(phone_obj)

    def find_phone(self, phone):
        phones_list = list(filter(lambda x: x.value == phone, self.phones))

        return phones_list[0] if phones_list else None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_record_string(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def __str__(self):
        return self.get_record_string()


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value.strip()
        self.data[name] = record

    def find(self, name):
        return self.data.get(name.strip())

    def delete(self, name):
        name = name.strip()
        self.validate(name)

        del self.data[name]

    def validate(self, name):
        if not name in self.data:
            raise ContactNotFound("Contact not found")

    def show_all(self):
        return [self.data[contact].get_record_string() for contact in self.data]


    def get_upcoming_birthdays(self):
        today = datetime.today().date()

        upcoming_birthdays = []

        for contact in self.data:
            user = self.data[contact]

            if not user.birthday:
                continue

            birthday_date = datetime.strptime(user.birthday.value, '%d.%m.%Y').date()
            this_year_birthday = birthday_date.replace(year=today.year)

            if this_year_birthday < today:
                this_year_birthday = this_year_birthday.replace(year=today.year + 1)

            if today + timedelta(days=7) >= this_year_birthday >= today:
                congratulation_date = this_year_birthday

                match congratulation_date.weekday():
                    case 5:
                        congratulation_date += timedelta(days=2)
                    case 6:
                        congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {"name": user.name.value, "congratulation_date": congratulation_date.strftime('%d.%m.%Y')})

        return upcoming_birthdays

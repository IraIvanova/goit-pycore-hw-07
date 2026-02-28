class AddressBookError(Exception):
    """Base class for all address book errors."""
    pass

class MandatoryArgumentsError(AddressBookError):
    pass

class EmptyName(AddressBookError):
    pass

class PhoneValidationError(AddressBookError):
    pass

class ContactNotFound(AddressBookError):
    pass

class PhoneNotFound(AddressBookError):
    pass

class PhoneAlreadyExists(AddressBookError):
    pass

class BirthdayFormatError(AddressBookError):
    pass

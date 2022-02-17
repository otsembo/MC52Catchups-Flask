class Contact:
    """
    This class will be used to create objects of contacts
    """

    contact_list = []  # Creates an empty list of contacts that belong to the class

    def __init__(self, first_name, last_name, phone_number, email):
        """
        this method helps us define class properties

        :param first_name:
        :param last_name:
        :param phone_number:
        :param email:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    # Run at this point to create contact

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod
    def find_contact_by_number(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

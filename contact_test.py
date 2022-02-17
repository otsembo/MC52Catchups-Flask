import unittest
from contact import Contact


# import modules

class TestContact(unittest.TestCase):  # Import testcase module to indicate that this class is a testcase

    def setUp(self):  # Initialize values before tests run
        self.new_contact = Contact("First", "Last", 712345678, "first.last@school.com")

    def tearDown(self):  # Method is called after each test case is run
        Contact.contact_list = []

    def test_init(self):
        self.assertEqual(self.new_contact.first_name, "First")

    def test_save_contact(self):  # If you run this before creating the method it will obviously fail.
        # (Comment the  method first to see this in action)
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_save_multiple_contacts(self):
        """ Test multiple contacts saved """
        self.new_contact.save_contact()
        test_contact = Contact("Terrence", "Tao", 712456987, "terrence.tao@math.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        """ Test deleting contact """
        self.new_contact.save_contact()
        test_contact = Contact("Terrence", "Tao", 712456987, "terrence.tao@math.com")
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", 711223344, "test@user.com")  # new contact
        test_contact.save_contact()

        found_contact = Contact.find_contact_by_number(711223344)

        self.assertEqual(found_contact.email, test_contact.email)


if __name__ == '__main__':
    unittest.main()

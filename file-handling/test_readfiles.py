import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    """

    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("test2.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file("test2.txt"))

    def test_nonfile(self):
        """
        Test to confirm that an exeption is raised when a wrong file is inputted
        """
        self.assertEqual(None,readfiles.read_file("tests.txt"))

if __name__ == '__main__':
    unittest.main()
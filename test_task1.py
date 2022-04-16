import unittest
from task1 import has_character, is_valid


class TestHasCharacter(unittest.TestCase):
    def test_empty_password_or_and_empty_part(self):
        self.assertFalse(has_character())

    def test_char_i_in_str_internship(self):
        self.assertFalse(has_character("y", "internship"))

    def test_num_i_in_str_internship(self):
        self.assertFalse(has_character("23", "internship"))

    def test_str_int_in_str_internship(self):
        self.assertTrue(has_character("int", "internship"))

    def test_str_internship_in_str_internship(self):
        self.assertTrue(has_character("internship", "internship"))


class TestIsValid(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid())

    def test_password_of_size_one(self):
        self.assertFalse(is_valid("4"))

    def test_password_of_size_five(self):
        self.assertFalse(is_valid("inter"))

    def test_password_of_size_nine(self):
        self.assertFalse(is_valid("Interns$8"))

    def test_password_of_size_twenty(self):
        self.assertTrue(is_valid("Inte%$rnshi1*2Interns_#"))

    def test_password_of_size_fourteen(self):
        self.assertTrue(is_valid("123*Internship"))

    def test_password_with_no_digit(self):
        self.assertFalse(is_valid("*(InternshipInternship_"))

    def test_password_with_only_digits(self):
        self.assertFalse(is_valid("28372873197391728173191"))

    def test_password_with_no_lowercase(self):
        self.assertFalse(is_valid("#*INTERNSHIP_INTERN$12"))

    def test_password_with_no_uppercase(self):
        self.assertFalse(is_valid("123)internship%^_internship2398"))

    def test_password_without_special_character(self):
        self.assertFalse(is_valid("23inTERnSHIPINTERN091"))

    def test_password_with_only_special_character(self):
        self.assertFalse(is_valid("/_~***&^%$@#''''''///>>>>>/===="))

    def test_valid_password(self):
        self.assertTrue(is_valid("InternshipInternship_87"))
        self.assertTrue(is_valid("2*7_)_InternshipInt34$"))



if __name__ == "__main__":
    unittest.main()

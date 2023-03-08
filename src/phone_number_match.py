import re

class PhoneNumberMatcher():
    global _phone_number_regex

    def __init__(self):
        self._phone_number_regex = re.compile(r'''(
                                                  ^(0{1}\d{9,10})$|
                                                  ^(4{2}\d{9,10})$|
                                                  ^(0{1}\d{3,4})\s(\d{5,6})$|
                                                  ^(4{2}\d{3,4})\s(\d{5,6})$
                                                   )''', re.VERBOSE)
    
    def is_string_uk_phone_number(self,string_to_test):
        string_match =self._phone_number_regex.search(string_to_test)

        return string_match != None

    def format_string_input():
        return
    



test = PhoneNumberMatcher()
if test.is_string_uk_phone_number("09927 1816"):
    print("True")
else:
    print("False")
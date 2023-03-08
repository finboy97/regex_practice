import src.phone_number_match

def test_valid_uk_10_digit_with_space():
    test_str_1="0178 403204"
    test_matcher = src.phone_number_match.PhoneNumberMatcher()
    assert test_matcher.is_string_uk_phone_number(test_str_1) == True

def test_valid_uk_44_beginning():
    test_str_2="441892 874893"
    test_matcher = src.phone_number_match.PhoneNumberMatcher()
    assert test_matcher.is_string_uk_phone_number(test_str_2) == True

def test_invalid_start():
    test_str_3="1688204593"

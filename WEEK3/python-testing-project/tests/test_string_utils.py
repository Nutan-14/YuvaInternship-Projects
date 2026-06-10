from app.string_utils import reverse_string, count_vowels, is_palindrome


def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"


def test_count_vowels():
    assert count_vowels("Education") == 5


def test_is_palindrome_true():
    assert is_palindrome("madam") is True


def test_is_palindrome_false():
    assert is_palindrome("python") is False
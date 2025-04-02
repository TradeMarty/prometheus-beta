import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all complexity requirements."""
    assert validate_password("Strong1Pass!") == True

def test_password_too_short():
    """Test that passwords less than 8 characters are invalid."""
    assert validate_password("Sh0rt!") == False

def test_missing_uppercase():
    """Test password without uppercase letter is invalid."""
    assert validate_password("nouppercase1!") == False

def test_missing_lowercase():
    """Test password without lowercase letter is invalid."""
    assert validate_password("NOLOWERCASE1!") == False

def test_missing_digit():
    """Test password without digit is invalid."""
    assert validate_password("NoDigitPass!") == False

def test_missing_special_char():
    """Test password without special character is invalid."""
    assert validate_password("NoSpecialChar1") == False

def test_multiple_missing_requirements():
    """Test password missing multiple requirements."""
    assert validate_password("short") == False

def test_edge_cases():
    """Test various edge case passwords."""
    test_cases = [
        "",  # Empty string
        "a",  # Single character
        "ABCDEFGH",  # No lowercase, no digit, no special char
        "abcdefgh",  # No uppercase, no digit, no special char
        "12345678",  # No uppercase, no lowercase, no special char
        "!@#$%^&*",  # No uppercase, no lowercase, no digit
    ]
    
    for case in test_cases:
        assert validate_password(case) == False

def test_special_characters():
    """Test various special characters."""
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for char in special_chars:
        password = f"ValidPass1{char}"
        assert validate_password(password) == True
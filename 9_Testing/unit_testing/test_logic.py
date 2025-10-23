import pytest
from logic import loan_eligibility


def test_loan_eligibility():
    assert loan_eligibility(70000, 28, 'employed') == True

def test_under_age_user():
    assert loan_eligibility(70000, 11, 'employed') == False

def test_low_income_user():
    assert loan_eligibility(1900, 30, 'employed') ==  False

def test_unemployed_user():
    assert loan_eligibility(190000, 30, 'unemployeed') == False
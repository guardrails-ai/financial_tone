# to run these, run
# pytest test/test-validator.py
from validator import FinancialTone

validator = FinancialTone()


def test_pass():
    test_output = "Growth is strong and we have plenty of liquidity."
    assert (
        validator.validate(test_output, {"financial_tone": "positive"}).outcome
        == "pass"
    )


def test_fail():
    test_output = (
        "There are doubts about our finances, and we are struggling to stay afloat."
    )
    assert (
        validator.validate(test_output, {"financial_tone": "positive"}).outcome
        == "fail"
    )

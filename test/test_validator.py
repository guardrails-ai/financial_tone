# to run these, run
# pytest test/test-validator.py
from validator import FinancialTone

validator = FinancialTone()

def test_pass():
    test_output = "This is an interesting increase in value."
    assert (
        validator.validate(test_output, {"financial_tone": "positive"}).outcome
        == "pass"
    )


def test_fail():
    test_output = "This is an exciting opportunity."
    assert (
        validator.validate(test_output, {"financial_tone": "positive"}).outcome
        == "fail"
    )

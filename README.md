## Overview

| Developed by | Cartesia AI|
| --- | --- |
| Date of development | Feb 14, 2024 |
| Validator type | Format |
| Blog | - |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator checks an LLM-generated output (in a financial context) for a particular tone.

## Requirements
* Dependencies: `transformers`, `torch`

## Installation

```bash
guardrails hub install hub://cartesia/financial_tone
```

## Usage Examples

### Validating string output via Python

In this example, we use the `financial_tone` validator on any LLM generated text.

```python
# Import Guard and Validator
from guardrails.hub import FinancialTone
from guardrails import Guard

# Use the Guard with the validator
guard = Guard().use(FinancialTone, on_fail="exception")

# Test passing response
guard.validate(
    "Growth is strong and we have plenty of liquidity.",
    metadata={"financial_tone": "positive"}
)

try:
    # Test failing response
    guard.validate(
        "There are doubts about our finances, and we are struggling to stay afloat.",
        metadata={"financial_tone": "positive"}
    )
except Exception as e:
    print(e)
```

## API Reference

**`__init__(self, on_fail="noop")`**
<ul>

Initializes a new instance of the Validator class.

**Parameters:**

- **`on_fail`** *(str, Callable):* The policy to enact when a validator fails. If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.

</ul>

<br>

**`validate(self, value, metadata={}) -> ValidationResult`**

<ul>

Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters:**

- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation.

| Key | Type | Description | Default | Required |
| --- | --- | --- | --- | --- |
| `financial_tone` | string | One of `positive`, `negative`, `neutral`| `neutral` | No |
| `financial_tone_threshold` | float | A float value between 0 and 1 | `0.8` | No |

</ul>

## Overview

| Developed by | Cartesia |
| --- | --- |
| Date of development | Feb 14, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator checks an LLM-generated output (in a financial context) for a particular tone.

## Requirements
- Dependencies: `nltk`, `transformers`

## Installation

```bash
$ guardrails hub install hub://guardrails/financial-tone
```

## Usage Examples

### Validating string output via Python

In this example, we use the `financial-tone` validator on any LLM generated text.

```python
# Import Guard and Validator
from guardrails.hub import FinancialTone
from guardrails import Guard

# Initialize Validator
val = FinancialTone()
val.validate(
    "This is an exciting opportunity to invest.", 
    metadata={"financial_tone": "positive", "financial_tone_threshold": 0.95},
)  # Pass

val.validate(
    "This is going to the floor in the next 3 months.", 
    metadata={"financial_tone": "positive", "financial_tone_threshold": 0.95},
)  # Fail
```

## API Reference

**`__init__(self, on_fail="noop")`**
<ul>

Initializes a new instance of the Validator class.

**Parameters:**

- **`on_fail`** *(str, Callable):* The policy to enact when a validator fails. If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.

</ul>

<br>

**`__call__(self, value, metadata={}) → ValidationOutcome`**

<ul>

Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters:**

- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation. Optionally pass in keys `financial_tone` and `financial_tone_threshold` to customize the validation process. Options for `financial_tone` include `positive`, `negative`, `neutral`. Options for `financial_tone_threshold` include a float value between 0 and 1.

</ul>
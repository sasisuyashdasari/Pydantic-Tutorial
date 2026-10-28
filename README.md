# Pydantic Tutorial

A short, step-by-step introduction to [Pydantic v2](https://docs.pydantic.dev/latest/), built around a single running example: a `Patient` model. Each file adds one concept on top of the previous one, so they are best read and run in order.

## Setup

Requires Python 3.9 or newer.

```bash
pip install -r requirements.txt
```

`email-validator` is needed because the examples use `EmailStr`.

## Lessons

| File | Topic | What it shows |
|------|-------|---------------|
| [1_pydantic_why.py](1_pydantic_why.py) | Why Pydantic | Declaring a model with type hints, `Field` constraints (`gt`, `lt`, `max_length`), `EmailStr`, `AnyUrl`, `strict` mode, and automatic type coercion (`'30'` becomes `30`). |
| [2_field_validator.py](2_field_validator.py) | Field validators | Custom checks with `@field_validator`: restricting email domains, transforming a value (upper-casing the name), and validating age. |
| [3_model_validator.py](3_model_validator.py) | Model validators | `@model_validator(mode='after')` for rules that involve several fields at once, such as requiring an emergency contact for patients over 60. |
| [4_computed_fields.py](4_computed_fields.py) | Computed fields | `@computed_field` for values derived from other fields, such as BMI calculated from weight and height. The value appears in the output but is not an input. |
| [5_nested_models.py](5_nested_models.py) | Nested models | Using one model (`Address`) inside another (`Patient`), and accessing nested data with dot notation. |
| [6_serialization.py](6_serialization.py) | Serialization | Converting a model to a dictionary with `model_dump()`, including excluding a nested field. |

## Running the examples

Run any file from the project folder:

```bash
python 1_pydantic_why.py
```


<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project delves into the critical aspects of securing personal data, covering essential concepts and practical implementations.

## Tasks

### [0. Regex-ing](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x00-personal_data/filtered_logger.py)
Write a function called `filter_datum` that returns the log message obfuscated:

- Arguments:
    - `fields`: a list of strings representing all fields to obfuscate
    - `redaction`: a string representing by what the field will be obfuscated
    - `message`: a string representing the log line
    - `separator`: a string representing by which character is separating all fields in the log line (`message`)
- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

---

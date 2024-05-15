#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated
    Args:
        @fields: The fields that should be obfuscated
        @redaction: A string representing by what the field will be obfuscated
        @message: A string representing the log line
        @separator: The string separator between fields in the log line
    """
    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)

    return message

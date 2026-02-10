"""
DEMO FILE: Bad code examples (intentionally broken for demonstration)

This file contains intentional issues to demonstrate what tooling catches.
DO NOT run pre-commit on this file during demos!

To exclude from pre-commit: git add bad_examples.py --no-verify
"""

# ISSUE: Unused imports (Ruff will catch this)
import sys
import os
from typing import List, Dict
import json


# ISSUE: No type hints (Ty will catch this)
def add(a, b):
    return a+b  # ISSUE: No spaces around operator (Ruff format will fix)


# ISSUE: Using old-style type hints instead of built-in types
def process_items(items: List[str]) -> Dict[str, int]:
    result = {}
    for item in items:
        result[item] = len(item)
    return result


# ISSUE: Function too complex, multiple issues
def bad_function(x):
    # ISSUE: Unnecessary else after return
    if x > 10:
        return "big"
    else:
        return "small"


# ISSUE: Missing docstrings
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


# ISSUE: Bare except (catches everything, bad practice)
def risky_operation():
    try:
        result = 10 / 0
        return result
    except:  # Ruff will flag this as too broad
        return None


# ISSUE: Variable name doesn't follow convention
MyVariable = 42  # Should be my_variable


# ISSUE: Comparison to True/False
def check_status(is_active):
    if is_active == True:  # Should be: if is_active:
        return "active"
    return "inactive"


# ISSUE: Mutable default argument
def append_to_list(item, list=[]):  # Bad! Default list is shared
    list.append(item)
    return list


# ISSUE: String formatting inconsistency
name = "World"
# Mix of f-strings and % formatting:
msg1 = f"Hello {name}"
msg2 = "Hello %s" % name  # Ruff suggests using f-strings


# ISSUE: Unreachable code
def unreachable_example():
    return True
    print("This will never execute")  # Ruff will catch this


# ISSUE: No type hints + incorrect typing
def confusing_function(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    else:
        return None  # What types are valid? Type hints would clarify!


if __name__ == "__main__":
    print("This file has intentional issues for demo purposes!")

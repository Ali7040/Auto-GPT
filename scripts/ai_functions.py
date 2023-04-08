# from typing import List, Optional
# import json
# from config import Config
# from call_ai_function import call_ai_function
# from json_parser import fix_and_parse_json
# cfg = Config()

# # Evaluating code

# def evaluate_code(code: str) -> List[str]:
#     function_string = "def analyze_code(code: str) -> List[str]:"
#     args = [code]
#     description_string = """Analyzes the given code and returns a list of suggestions for improvements."""

#     result_string = call_ai_function(function_string, args, description_string)
    
#     return result_string


# # Improving code

# def improve_code(suggestions: List[str], code: str) -> str:
#     function_string = (
#         "def generate_improved_code(suggestions: List[str], code: str) -> str:"
#     )
#     args = [json.dumps(suggestions), code]
#     description_string = """Improves the provided code based on the suggestions provided, making no other changes."""

#     result_string = call_ai_function(function_string, args, description_string)
#     return result_string


# # Writing tests


# def write_tests(code: str, focus: List[str]) -> str:
#     function_string = (
#         "def create_test_cases(code: str, focus: Optional[str] = None) -> str:"
#     )
#     args = [code, json.dumps(focus)]
#     description_string = """Generates test cases for the existing code, focusing on specific areas if required."""

#     result_string = call_ai_function(function_string, args, description_string)
#     return result_string


from typing import List, Optional
import json
from config import Config
from call_ai_function import call_ai_function
from json_parser import fix_and_parse_json

# Initialize Config object
cfg = Config()

def analyze_code(code: str) -> List[str]:
    """
    Analyzes the given code and returns a list of suggestions for improvements.

    Args:
        code (str): The code to analyze.

    Returns:
        List[str]: A list of suggestions for improving the code.
    """
    function_string = "def analyze_code(code: str) -> List[str]:"
    args = [code]
    description_string = "Analyzes the given code and returns a list of suggestions for improvements."
    result_string = call_ai_function(function_string, args, description_string)
    return result_string


def generate_improved_code(suggestions: List[str], code: str) -> str:
    """
    Improves the provided code based on the suggestions provided, making no other changes.

    Args:
        suggestions (List[str]): A list of suggestions for improving the code.
        code (str): The code to improve.

    Returns:
        str: The improved code.
    """
    function_string = "def generate_improved_code(suggestions: List[str], code: str) -> str:"
    args = [json.dumps(suggestions), code]
    description_string = "Improves the provided code based on the suggestions provided, making no other changes."
    result_string = call_ai_function(function_string, args, description_string)
    return result_string


def create_test_cases(code: str, focus: Optional[str] = None) -> str:
    """
    Generates test cases for the existing code, focusing on specific areas if required.

    Args:
        code (str): The code to generate test cases for.
        focus (Optional[str], optional): A string specifying the areas to focus on. Defaults to None.

    Returns:
        str: The generated test cases.
    """
    function_string = "def create_test_cases(code: str, focus: Optional[str] = None) -> str:"
    args = [code, json.dumps(focus)]
    description_string = "Generates test cases for the existing code, focusing on specific areas if required."
    result_string = call_ai_function(function_string, args, description_string)
    return result_string

import sys
import logging

def error_message_detail(error, error_details: sys.exc_info):
    """
    Extracts detailed information from a Python error and formats it into a string.

    Args:
        error: The error object.
        error_details: The sys.exc_info() tuple containing error information.

    Returns:
        A formatted error message string.
    """

    _, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_line = exc_tb.tb_lineno
    error_message = "An error occurred in Python script: {0} at line {1}:\n{2}".format(
        file_name, error_line, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    A custom exception class that captures error details and provides a formatted message.

    Args:
        error_message: The error message.
        error_details: The sys.exc_info() tuple containing error information.
    """

    def __init__(self, error_message, error_details: sys.exc_info):
        super().__init__(error_message)  # Use super() for constructor chaining
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        """
        Returns the formatted error message.
        """
        return self.error_message
'''
try:
    a=1/10
except Exception as e :
    logging.info("Divide by zERO")  
    raise CustomException(e,sys)  '''
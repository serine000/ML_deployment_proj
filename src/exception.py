import sys


def error_message_detail(error, error_details: sys):
    """Return the exact exception that occured with its location."""

    _, _, exc_tb = error_details.exc_info()
    err_file = exc_tb.tb_frame.f_code.co_filename
    error_message = f"An error occured in file {err_file}, on line {exc_tb.tb_lineno} with an error message {str(error)}"

    return error_message


def CustomException (Exception):
    """Return a custom user specific exception."""

    def __init__(self, error_message, error_details: sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
    

    def __str__():
        return self.error_message

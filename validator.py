from datetime import datetime
import os

from constants import (
    ArgsMessages,
    DateFormatMessages,
)


class Validator:
    """
    Validates the input arguments
    """
    def __init__(self, parser):
        self.parser = parser

    def month_input_validate(self, date):
        """
        Validate Month Input Format That Is Date Type Format Like 2012/4
        Returns Date Type Format Like 2012/4
        """
        try:
            date = datetime.strptime(date, DateFormatMessages.YEAR_MONTH_FORMAT)
        except ValueError:
            self.parser.error(DateFormatMessages.INVALID_MONTH_FORMAT)
        return date

    def year_input_validate(self, date):
        """
        Validate Year Input Format That Is Date Type Format Like 2009
        Returns Date Type Format Like 2009
        """
        try:
            date = datetime.strptime(date, DateFormatMessages.YEAR_FORMAT)
        except ValueError:
            self.parser.error(DateFormatMessages.INVALID_YEAR_FORMAT)
        return date
    
    def path_validate(self, path):
        """
        Check if path of type string exists or not,
        Returns path of type string
        """
        if os.path.exists(path):
            return path
        else:
            self.parser.error(ArgsMessages.INVALID_PATH)


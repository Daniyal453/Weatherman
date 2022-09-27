import argparse
from constants import (
    ArgsMessages,
    HorizontalBarMessages,
    MonthMessages,
    YearMessages,
)
from validator import Validator


class ArgsParser:
    """
    Returns dictionary of input args
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser("WeatherMan")

    def get_input_args(self):
        """
        Returns dictionary of all input arguments
        """
        self.add_args()

        args = self.parser.parse_args()
        month_arg = args.month
        year_arg = args.year
        month_horizontal_bar = args.month_horizontal_bar
        path_to_file = args.path_to_file

        if not any([month_arg, year_arg, month_horizontal_bar]):
            raise Exception(ArgsMessages.PROVIDE_ENOUGH_ARGS)

        return {
            "month": month_arg,
            "year": year_arg,
            "month_temp_with_horizontal_bar": month_horizontal_bar,
            "path_to_file": path_to_file
        }

    def add_args(self):
        """
        Adding Args To Args Parser
        """
        validator = Validator(self.parser)
        self.parser.add_argument(
            "path_to_file",
            help=ArgsMessages.PATH_TO_FILE_ARG_HELP,
            type=validator.path_validate,
        )
        self.parser.add_argument(
            MonthMessages.MONTH_ARG,
            "--month",
            type=validator.month_input_validate,
            help=MonthMessages.MONTH_ARG_HELP
        )
        self.parser.add_argument(
            YearMessages.YEAR_ARG,
            "--year",
            type=validator.year_input_validate,
            help=YearMessages.YEAR_ARG_HELP
        )
        self.parser.add_argument(
            HorizontalBarMessages.HORIZONTAL_BAR_ARG,
            "--month_horizontal_bar",
            type=validator.month_input_validate,
            help=HorizontalBarMessages.HORIZONTAL_BAR_ARG_HELP
        )


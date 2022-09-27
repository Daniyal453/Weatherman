from args_parser import ArgsParser
from constants import (
    ArgsMessages,
    HorizontalBarMessages,
    MonthMessages,
    YearMessages,
)
from weatherman import WeatherMan

if __name__ == "__main__":
    init_args = ArgsParser()
    args = init_args.get_input_args()
    WeatherMan(
        month=args[MonthMessages.MONTH],
        year=args[YearMessages.YEAR],
        month_horizontal_bar=args[HorizontalBarMessages.MONTH_TEMP_WITH_HORIZONTAL_BAR],
        path_to_file=args[ArgsMessages.PATH_TO_FILE]
    ).reading_args()


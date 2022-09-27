class GeneralMessages:
    """
    Contains General Constants For The Whole Project
    """
    RED = "\033[91m+\033[0m"
    BLUE = "\033[94m+\033[0m"
    HEADERS = ["pk", "max_temperature", "mean_temperature",
               "min_temperature", "max_humidity",
               "mean_humidity", "min_humidity"
    ]
    DESCRIPTION_AVG = "{description}: {avg}"
    UTF_8 = "utf-8"


class MonthMessages:
    """
    Contains Constants For Month
    """
    FOR_MONTH = "For Month"
    M_FLAG = "m"
    MONTH = "month"
    NO_MONTH_MESSAGE = "No file found for this month of this year"
    MONTH_ARG = "-a"
    MONTH_ARG_HELP = "For Month: Pass Month And Year Like 2012/4"


class YearMessages:
    """
    Contains Constants For Year
    """
    FOR_YEAR = "For Year"
    Y_FLAG = "y"
    YEAR = "year"
    NO_YEAR_MESSAGE = "No file found for this year"
    YEAR_ARG = "-e"
    YEAR_ARG_HELP = "For Year: Pass Year Like 2012"


class HorizontalBarMessages:
    """
    Contains Constants For Month Horizontal Bars
    """
    FOR_HORIZONTAL_BAR = "For Horizontal Bar"
    M_H_FLAG = "m-h"
    MONTH_TEMP_WITH_HORIZONTAL_BAR = "month_temp_with_horizontal_bar"
    HORIZONTAL_FILE_NAME = "-Horizontal_Bar"
    TWO_HORIZONTAL_BAR_MESSAGE = "{date} {add_sign} {temp}C"
    TWO_HORIZONTAL_BAR_MESSAGE_REPORT = "{date} {add_sign} {temp}C{color}"
    ONE_HORIZONTAL_BAR_MESSAGE = "{name} {max_add_sign}{min_add_sign} {min_temp}C - {max_temp}C"
    HORIZONTAL_BAR_ARG = "-c"
    HORIZONTAL_BAR_ARG_HELP = "For Horizontal Bar Pass Month And Year Like 2012/4"
    FILE_NAME_MESSAGE = "{month_year}{horizontal_bar}"


class DateFormatMessages:
    """
    Contains Constants For Date Format
    """
    YEAR_FORMAT = "%Y"
    YEAR_MONTH_FORMAT = "%Y/%m"
    MONTH_YEAR_FORMAT = "%b-%Y"
    MONTH_FORMAT = "%b"
    DAY_FORMAT = "%d"
    MONTH_DAY_FORMAT = "%b %d"
    YEAR_MONTH_DAY_FORMAT = "%Y-%m-%d"
    INVALID_MONTH_FORMAT = ("Invalid Month Format. Month Should Be Between 1-12."
                            " And Year Should Be In 4 Digits. e.g 2012/4")
    INVALID_YEAR_FORMAT = "Invalid Year Format.It Should Be In 4 Digits. e.g 2012"


class TempMessages:
    """
    Contains Constants For Temperature
    """
    MAX_TEMP_AVG_MESSAGE = "Average Max Temperature For This Month"
    MIN_TEMP_AVG_MESSAGE = "Average Min Temperature For This Month"
    MIN_TEMP_THIS_YEAR = "Min Temperature For This Year"
    MAX_TEMP_THIS_YEAR = "Max Temperature For This Year"
    TOTAL_MAX_TEMP = "total_max_temp"
    TOTAL_MIN_TEMP = "total_min_temp"
    TEMP = "{temp}C on {date}"
    DESCRIPTION_TEMP = "{description}: {temp}"
    TEMP_AVG = "{avg}C"


class HumidityMessages:
    """
    Contains Constant For Humidity
    """
    MEAN_HUMIDITY_AVG_MESSAGE = "Average Mean Humidity For This Month"
    MAX_HUMIDITY_THIS_YEAR = "Max Humidity For This Year"
    HIGHEST_MAX_HUMIDITY = "highest_max_humidity"
    TOTAL_MEAN_HUMIDITY = "total_mean_humidity"
    HUMIDITY = "{max_humidity}% on {date}"
    DESCRIPTION_HUMIDITY = "{description}: {humidity}"
    HUMIDITY_AVG = "{avg}%"


class PdfMessages:
    """
    Contains Constant For Pdf
    """
    PDF_OUTPUT = "{path_to_save}/{file_name}.pdf"
    FONT_ARIAL = "Arial"
    PATH_TO_SAVE_PDF = "./report_results"
    MONTH_DESCRIPTION = ["Average Max Temperature For This Month",
                         "Average Min Temperature For This Month",
                         "Average Mean Humidity For This Month"
    ]
    YEAR_DESCRIPTION = ["Max Temperature For This Year",
                        "Min Temperature For This Year",
                        "Max Humidity For This Year"
    ]
    RED_FLAG = "r"
    BLUE_FLAG = "b"


class ArgsMessages:
    """
    Contains Constant For Arguments Parser
    """
    PROVIDE_ENOUGH_ARGS = ("Please Provide At Least One Optional Argument. E.g\n"
                           "For Year: -e 2012\n"
                           "For Month: -a 2015/3\n"
                           "For Horizontal-Bars: -c 2012/5"
                           )
    PATH_TO_FILE = "path_to_file"
    INVALID_PATH = "Invalid! Path Doesn\'t Exist"
    PATH_TO_FILE_ARG_HELP = "Path to file directory"


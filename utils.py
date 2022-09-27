from constants import (
    DateFormatMessages,
    HorizontalBarMessages,
    MonthMessages,
    YearMessages
)


def make_file_name(args, flag):
    """
    Makes file_name for given flag and args
    """
    if flag == MonthMessages.M_FLAG:
        file_name = args.strftime(
            DateFormatMessages.MONTH_YEAR_FORMAT
        )
        return file_name

    elif flag == YearMessages.Y_FLAG:
        file_name = args.strftime(DateFormatMessages.YEAR_FORMAT)
        return file_name

    elif flag == HorizontalBarMessages.M_H_FLAG:
        file_name = HorizontalBarMessages.FILE_NAME_MESSAGE.format(
            month_year=args.strftime(DateFormatMessages.MONTH_YEAR_FORMAT),
            horizontal_bar=HorizontalBarMessages.HORIZONTAL_FILE_NAME
        )
        return file_name


def convert_str_to_int_or_float(number):
    """
    Takes Str and return int or float according to string value
    """
    if number.isdigit():
        return int(number)
    else:
        return float(number)


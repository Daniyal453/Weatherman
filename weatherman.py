from calculator import Calculator
from constants import (
    HorizontalBarMessages,
    MonthMessages,
    PdfMessages,
    YearMessages,
)
from reader import DataReader
from report_generator import PdfMaker
from utils import make_file_name


class WeatherMan:
    """
    Start Weatherman Project
    """
    def __init__(self, month, year, month_horizontal_bar, path_to_file):
        self.month_args = month
        self.year_args = year
        self.month_horizontal_bar = month_horizontal_bar
        self.path_to_file = path_to_file

    def reading_args(self):
        """
        Reading Arguments And Sharing With Other Modules
        """
        if self.month_args:
            print(MonthMessages.FOR_MONTH)
            calculator_obj = self.get_calculator_obj(
                self.month_args,
                MonthMessages.MONTH
            )
            calculator_obj.show_avg_max_min_temp_mean_humidity()
            avg_result_output = calculator_obj.get_avg_max_min_temp_mean_humidity()
            self.make_pdf(
                avg_result_output.values(),
                self.month_args,
                MonthMessages.M_FLAG,
            )

        if self.month_horizontal_bar:
            print(HorizontalBarMessages.FOR_HORIZONTAL_BAR)
            calculator_obj = self.get_calculator_obj(
                self.month_horizontal_bar,
                HorizontalBarMessages.MONTH_TEMP_WITH_HORIZONTAL_BAR
            )
            horizontal_bar_output = calculator_obj.show_month_max_min_temp_in_two_horizontal_bars()
            self.make_pdf(
                horizontal_bar_output,
                self.month_horizontal_bar,
                HorizontalBarMessages.M_H_FLAG,
            )

        if self.year_args:
            print(YearMessages.FOR_YEAR)
            calculator_obj = self.get_calculator_obj(
                self.year_args,
                YearMessages.YEAR
            )
            year_result_output = calculator_obj.show_max_min_temp_max_humidity()
            self.make_pdf(
                year_result_output.values(),
                self.year_args,
                YearMessages.Y_FLAG,
            )

    def get_calculator_obj(self, args, flag):
        """
        Takes args and flag,
        Returns Calculator Class Object
        """
        data_reader_obj = DataReader(
            args,
            self.path_to_file,
            flag
        )
        weather_reading_list = data_reader_obj.read_files()
        if weather_reading_list:
            calculator_obj = Calculator(weather_reading_list)
            return calculator_obj

    def make_pdf(self, output, args, flag):
        """
        Make Pdf For Month, Year And Horizontal Bars
        """
        file_name = make_file_name(
            args=args,
            flag=flag
        )
        init_pdf = PdfMaker(output, file_name)

        if flag == HorizontalBarMessages.M_H_FLAG:
            init_pdf.bar_pdf_maker()
        else:
            if flag == MonthMessages.M_FLAG:
                init_pdf.pdf_maker(PdfMessages.MONTH_DESCRIPTION)
            else:
                init_pdf.pdf_maker(PdfMessages.YEAR_DESCRIPTION)


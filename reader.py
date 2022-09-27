import csv
from datetime import datetime
import os

from constants import (
    DateFormatMessages,
    GeneralMessages,
    HorizontalBarMessages,
    MonthMessages,
    YearMessages,
)
from weather_reading import WeatherReading


class DataReader:
    """
    This class will read files from file directory and returns the data in list of class objects
    """

    def __init__(self, input_args, path_to_file, flag):
        self.input_args = input_args
        self.path_to_file = path_to_file
        self.flag = flag
        self.file_data = []

    def file_parser(self):
        """
        Return list of file names for specific year or month
        """
        file_names = []
        year = self.input_args.strftime(DateFormatMessages.YEAR_FORMAT)

        for files in os.listdir(self.path_to_file):
            if year in files:
                if self.flag == YearMessages.YEAR:
                    file_names.append(files)

                elif self.flag == MonthMessages.MONTH:
                    month = self.input_args.strftime(DateFormatMessages.MONTH_FORMAT)
                    if month in files:
                        file_names.append(files)

                elif self.flag == HorizontalBarMessages.MONTH_TEMP_WITH_HORIZONTAL_BAR:
                    month = self.input_args.strftime(DateFormatMessages.MONTH_FORMAT)
                    if month in files:
                        file_names.append(files)
        return file_names

    def file_checker(self):
        """
        Checks length of file names
        """
        if len(self.file_parser()) == 0:
            if self.flag == MonthMessages.MONTH:
                raise Exception(MonthMessages.NO_MONTH_MESSAGE)
            if self.flag == YearMessages.YEAR:
                raise Exception(YearMessages.NO_YEAR_MESSAGE)
            if self.flag == HorizontalBarMessages.MONTH_TEMP_WITH_HORIZONTAL_BAR:
                raise Exception(MonthMessages.NO_MONTH_MESSAGE)

    def read_files(self):
        """
        Takes args and file_path,
        returns data for particular year or month
        """
        file_names = self.file_parser()
        self.file_checker()
        if file_names:
            for files in file_names:
                file = open(
                    os.path.join(self.path_to_file, files),
                    encoding=GeneralMessages.UTF_8
                )
                read = csv.DictReader(file)
                file_headers = read.fieldnames
                for data in read:
                    date_format = datetime.strptime(
                        data[file_headers[0]], DateFormatMessages.YEAR_MONTH_DAY_FORMAT)
                    check_all_fields = all(
                        [
                            data["Max TemperatureC"], data["Mean TemperatureC"],
                            data["Min TemperatureC"], data["Max Humidity"],
                            data[" Mean Humidity"], data[" Min Humidity"]
                        ]
                    )
                    if check_all_fields:
                        weather_reading_objects = WeatherReading(
                            max_temp=data["Max TemperatureC"],
                            min_temp=data["Min TemperatureC"],
                            mean_temp=data["Mean TemperatureC"],
                            max_humidity=data["Max Humidity"],
                            min_humidity=data[" Min Humidity"],
                            mean_humidity=data[" Mean Humidity"],
                            date=date_format,
                        )
                        self.file_data.append(weather_reading_objects)
                file.close()

            return self.file_data


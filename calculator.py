from operator import attrgetter

from constants import (
    DateFormatMessages,
    GeneralMessages,
    HorizontalBarMessages,
    HumidityMessages,
    PdfMessages,
    TempMessages,
)


class Calculator:
    """
    This class contains multiple methods like avg methods, month temp in horizontal bars etc
    """
    def __init__(self, weather_reading_list):
        self.weather_reading_list = weather_reading_list

    def __get_high_max_temp(self):
        """
        Return maximum temperature of type int or float
        """
        high_max_temp = max(
            self.weather_reading_list,
            key=attrgetter("max_temperature")
        )
        high_temp = TempMessages.TEMP.format(
            temp=high_max_temp.max_temperature,
            date=self.convert_date_format_to_month_day(high_max_temp.date)
        )

        return high_temp

    def __get_low_min_temp(self):
        """
        Returns minimum temperature of type int or float
        """
        low_min_temp = min(
            self.weather_reading_list,
            key=attrgetter("min_temperature")
        )
        low_temp = TempMessages.TEMP.format(
            temp=low_min_temp.min_temperature,
            date=self.convert_date_format_to_month_day(low_min_temp.date)
        )

        return low_temp

    def __get_high_max_humidity(self):
        """
        Return maximum humidity of type int or float
        """
        high_max_humidity = max(
            self.weather_reading_list,
            key=attrgetter("max_humidity")
        )
        high_humidity = HumidityMessages.HUMIDITY.format(
            max_humidity=high_max_humidity.max_humidity,
            date=self.convert_date_format_to_month_day(high_max_humidity.date)
        )

        return high_humidity

    def show_max_min_temp_max_humidity(self):
        """
        Returns dictionary of maximum temp, minimum temp and max humidity for the whole year
        """
        print(TempMessages.DESCRIPTION_TEMP.format(
            description=TempMessages.MAX_TEMP_THIS_YEAR,
            temp=self.__get_high_max_temp())
        )
        print(TempMessages.DESCRIPTION_TEMP.format(
            description=TempMessages.MIN_TEMP_THIS_YEAR,
            temp=self.__get_low_min_temp())
        )
        print(HumidityMessages.DESCRIPTION_HUMIDITY.format(
            description=HumidityMessages.MAX_HUMIDITY_THIS_YEAR,
            humidity=self.__get_high_max_humidity())
        )

        return {
            "max_temp_this_year": self.__get_high_max_temp(),
            "min_temp_this_year": self.__get_low_min_temp(),
            "max_humidity_this_year": self.__get_high_max_humidity()
        }

    def convert_date_format_to_month_day(self, date):
        """
        Will convert date format from 2017-3-12 to Mar 12
        """
        new_date = date.strftime(DateFormatMessages.MONTH_DAY_FORMAT)
        return new_date

    def __get_avg_max_temp(self):
        """
        Returns Avg Of Maximum Temperature Of Type int or float
        """
        total = self.__calc_total_max_min_temp_max_humidity()
        avg_max_temp = TempMessages.TEMP_AVG.format(
            avg=total[TempMessages.TOTAL_MAX_TEMP] // len(self.weather_reading_list),
        )

        return avg_max_temp

    def __get_avg_min_temp(self):
        """
        Returns Avg Of Minimum Temperature Of Type int or float
        """
        total = self.__calc_total_max_min_temp_max_humidity()
        avg_min_temp = TempMessages.TEMP_AVG.format(
            avg=total[TempMessages.TOTAL_MIN_TEMP] // len(self.weather_reading_list),
        )

        return avg_min_temp

    def __get_avg_mean_humidity(self):
        """
        Returns Avg Of Mean Humidity Of Type int or float
        """
        total = self.__calc_total_max_min_temp_max_humidity()
        avg_mean_humidity = HumidityMessages.HUMIDITY_AVG.format(
            avg=total[HumidityMessages.TOTAL_MEAN_HUMIDITY] // len(self.weather_reading_list),
        )

        return avg_mean_humidity

    def __calc_total_max_min_temp_max_humidity(self):
        """
        Returns Dictionary of Total Sum Of Max,Min Temp And Mean Humidity
        """
        total_max_temp = 0.0
        total_min_temp = 0.0
        total_mean_humidity = 0.0

        for data in self.weather_reading_list:
            total_max_temp += data.max_temperature
            total_min_temp += data.min_temperature
            total_mean_humidity += data.mean_humidity

        return {
            "total_max_temp": total_max_temp,
            "total_min_temp": total_min_temp,
            "total_mean_humidity": total_mean_humidity
        }

    def show_avg_max_min_temp_mean_humidity(self):
        """
        Returns Dictionary of Avg Of Maximum Minimum Temperature And Mean Humidity
        """
        print(GeneralMessages.DESCRIPTION_AVG.format(
            description=TempMessages.MAX_TEMP_AVG_MESSAGE,
            avg=self.__get_avg_max_temp())
        )
        print(GeneralMessages.DESCRIPTION_AVG.format(
            description=TempMessages.MIN_TEMP_AVG_MESSAGE,
            avg=self.__get_avg_min_temp())
        )
        print(GeneralMessages.DESCRIPTION_AVG.format(
            description=HumidityMessages.MEAN_HUMIDITY_AVG_MESSAGE,
            avg=self.__get_avg_mean_humidity())
        )

    def get_avg_max_min_temp_mean_humidity(self):
        """
        Returns Dictionary Of Avg Max Min Temperature And Mean Humidity
        """
        return {
            "max_avg_temp": self.__get_avg_max_temp(),
            "min_avg_temp": self.__get_avg_min_temp(),
            "mean_avg_humidity": self.__get_avg_mean_humidity()
        }

    def show_month_max_min_temp_in_two_horizontal_bars(self):
        """
        Prints Month Max Min Temperature With Max In Red And Min In Blue
        """
        monthly = self.__get_monthly_info()
        for monthly_horizontal_bar in monthly["monthly_temp_in_two_horizontal_bars"]:
            print(monthly_horizontal_bar)

        return monthly["monthly_temp_report_data"]

    def show_month_max_min_temp_in_one_horizontal_bar(self):
        """
        Prints Highest Lowest Temp In One Line With Read And Blue Respectively
        """
        monthly = self.__get_monthly_info()
        for monthly_horizontal_bars in monthly["monthly_temp_in_two_horizontal_bar"]:
            print(monthly_horizontal_bars)

        return monthly["monthly_temp_in_two_horizontal_bar"]

    def __get_monthly_info(self):
        """
        Returns list of max,min temp in separate lines with add(+) operator ,
        And list of max,min temp in one line with add(+) operator
        """
        monthly_temp_in_two_horizontal_bars = []
        monthly_temp_in_one_horizontal_bar = []
        monthly_temp_in_two_horizontal_bars_report = []

        for weather_readings in self.weather_reading_list:
            date = weather_readings.date.strftime(DateFormatMessages.DAY_FORMAT)
            monthly_temp_in_two_horizontal_bars.append(
                self.two_horizontal_bar(
                    date,
                    weather_readings.max_temperature,
                    GeneralMessages.RED
                )
            )
            monthly_temp_in_two_horizontal_bars.append(
                self.two_horizontal_bar(
                    date,
                    weather_readings.min_temperature,
                    GeneralMessages.BLUE
                )
            )
            monthly_temp_in_two_horizontal_bars_report.append(
                self.two_horizontal_bar_report(
                    date,
                    weather_readings.max_temperature,
                    PdfMessages.RED_FLAG
                )
            )
            monthly_temp_in_two_horizontal_bars_report.append(
                self.two_horizontal_bar_report(
                    date,
                    weather_readings.min_temperature,
                    PdfMessages.BLUE_FLAG
                )
            )
            monthly_temp_in_one_horizontal_bar.append(
                HorizontalBarMessages.ONE_HORIZONTAL_BAR_MESSAGE.format(
                    name=date,
                    max_add_sign=(GeneralMessages.RED * int(weather_readings.min_temperature)),
                    min_add_sign=(GeneralMessages.BLUE * int(weather_readings.max_temperature)),
                    min_temp=str(weather_readings.min_temperature),
                    max_temp=str(weather_readings.max_temperature)
                )
            )

        return {
            "monthly_temp_in_one_horizontal_bar": monthly_temp_in_one_horizontal_bar,
            "monthly_temp_in_two_horizontal_bars": monthly_temp_in_two_horizontal_bars,
            "monthly_temp_report_data": monthly_temp_in_two_horizontal_bars_report
        }

    def two_horizontal_bar(self, date, weather_readings, color):
        """
        Returns String For Two Horizontal Bar Like,
        "01 ++++++ 12C" Max Temp
        "01 ++++ 6C" Min Temp
        """
        return HorizontalBarMessages.TWO_HORIZONTAL_BAR_MESSAGE.format(
            date=date,
            add_sign=(color * int(weather_readings)),
            temp=str(weather_readings),
        )

    def two_horizontal_bar_report(self, date, weather_readings, flag):
        """
        Returns String For Two Horizontal Bar With Flag Like,
        "01 ++++++ 12C r" Max Temp
        "01 ++++ 6C b" Min Temp
        """
        return HorizontalBarMessages.TWO_HORIZONTAL_BAR_MESSAGE_REPORT.format(
            date=date,
            add_sign=("+" * int(weather_readings)),
            temp=str(weather_readings),
            color=flag
        )

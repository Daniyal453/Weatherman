from utils import convert_str_to_int_or_float


class WeatherReading:
    """
    This class works as a data structure for each day weather reading.
    It stores the record for each day weather.
    """
    def __init__(self, date, max_temp,
                 min_temp, mean_temp, max_humidity,
                 min_humidity, mean_humidity):

        self.date = date
        self.max_temperature = convert_str_to_int_or_float(max_temp)
        self.min_temperature = convert_str_to_int_or_float(min_temp)
        self.mean_temperature = convert_str_to_int_or_float(mean_temp)
        self.max_humidity = convert_str_to_int_or_float(max_humidity)
        self.min_humidity = convert_str_to_int_or_float(min_humidity)
        self.mean_humidity = convert_str_to_int_or_float(mean_humidity)


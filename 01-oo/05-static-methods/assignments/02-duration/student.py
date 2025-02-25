class Duration:
    def __init__(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
    
    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds, seconds / 60, seconds / 3600)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60, minutes, minutes / 60)
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600, hours * 60, hours)
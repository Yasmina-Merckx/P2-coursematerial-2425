class LengthConverter:
    def __init__(self):
        self.__meter = 0
        self.__feet = 0
        self.__inch = 0

    @property
    def meter(self):
        return self.__meter
    
    @meter.setter
    def meter(self, value):
        self.__meter = value
        self.__feet = self.__meter * 3.28084
        self.__inch = self.meter * 39.3701
    
    @property
    def feet(self):
        return self.__feet

    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meter = self.__feet / 3.28084
        self.__inch = self.__feet * 12
    
    @property
    def inch(self):
        return self.__inch

    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__feet = self.__inch / 12
        self.__meter = self.inch / 39.3701
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.__weight = weight_in_kg
        self.__height = height_in_m
        self.bmi = self.calculate_bmi(self.__weight, self.__height)
        self.category = self.find_category(self.bmi)

    def calculate_bmi(self, weight, height):
        return weight / height**2
    
    def find_category(self, bmi):
        if bmi <= 25:
            if bmi < 18.5:
                return "underweight"
            return "normal"
        return "overweight"

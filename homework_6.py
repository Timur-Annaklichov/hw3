class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    
    def __str__(self):
        return f"{self.value} {self.unit}"
    
    def convert_to(self, target_unit):
        if self.unit == target_unit:
            return self.value
        
        conversions = {
            "mm": {"cm": 0.1, "m": 0.001, "km": 0.000001},
            "cm": {"mm": 10, "m": 0.01, "km": 0.00001},
            "m": {"mm": 1000, "cm": 100, "km": 0.001},
            "km": {"mm": 1000000, "cm": 100000, "m": 1000}
        }
        
        return self.value * conversions[self.unit][target_unit]
    
    def __add__(self, other):
        value_in_my_units = other.convert_to(self.unit)
        return Distance(self.value + value_in_my_units, self.unit)
    
    def __sub__(self, other):
        value_in_my_units = other.convert_to(self.unit)
        return Distance(self.value - value_in_my_units, self.unit)

d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(150, "cm")

print(d1)
print(d2)
print(d3)

result1 = d1 + d2
print(f"10m + 2km = {result1}")

result2 = d2 - d1
print(f"2km - 10m = {result2}")

result3 = d1 + d3
print(f"10m + 150cm = {result3}")

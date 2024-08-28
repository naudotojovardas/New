# Create a class ImperialToMetric that facilitates the conversion of measurements from the Imperial system to the Metric system.
#  This class should include static methods for converting common Imperial units such as inches, feet, miles, pounds, and gallons
#  to their Metric counterparts—centimeters, meters, kilometers, kilograms, and liters, respectively.
# Inches to Centimeters:
# Method Name: inches_to_centimeters
# Parameter: inches (float)
# Returns: Equivalent length in centimeters (float), rounded to two decimal places.
# Feet to Meters:
# Method Name: feet_to_meters
# Parameter: feet (float)
# Returns: Equivalent length in meters (float), rounded to two decimal places.
# Miles to Kilometers:
# Method Name: miles_to_kilometers
# Parameter: miles (float)
# Returns: Equivalent distance in kilometers (float), rounded to two decimal places.
# Pounds to Kilograms:
# Method Name: pounds_to_kilograms
# Parameter: pounds (float)
# Returns: Equivalent weight in kilograms (float), rounded to two decimal places.
# Gallons to Liters:
# Method Name: gallons_to_liters
# Parameter: gallons (float)
# Returns: Equivalent volume in liters (float), rounded to two decimal places.

class ImperialToMetric:
    @staticmethod
    def inches_to_centimeters(inches) -> float:
        return round(inches * 2.54, 2)

    @staticmethod
    def feet_to_meters(feet) -> float:
        return round(feet * 0.3048, 2)

    @staticmethod
    def miles_to_kilometers(miles) -> float:
        return round(miles * 1.60934, 2)

    @staticmethod
    def pounds_to_kilograms(pounds) -> float:
        return round(pounds * 0.453592, 2)

    @staticmethod
    def gallons_to_liters(gallons) -> float:
        return round(gallons * 3.78541, 2)
    
def main():
    print(ImperialToMetric.inches_to_centimeters(1))
    print(ImperialToMetric.feet_to_meters(1))
    print(ImperialToMetric.miles_to_kilometers(1))
    print(ImperialToMetric.pounds_to_kilograms(1))
    print(ImperialToMetric.gallons_to_liters(1))

main()
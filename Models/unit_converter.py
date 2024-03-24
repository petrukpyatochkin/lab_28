class UnitConverter:
    # Length conversion factors
    METER_TO_FEET = 3.28084
    FEET_TO_METER = 1 / METER_TO_FEET

    # Weight conversion factors
    KILOGRAM_TO_POUND = 2.20462
    POUND_TO_KILOGRAM = 1 / KILOGRAM_TO_POUND

    # Volume conversion factors
    LITER_TO_GALLON = 0.264172
    GALLON_TO_LITER = 1 / LITER_TO_GALLON

    @staticmethod
    def meters_to_feet(meters):
        return meters * UnitConverter.METER_TO_FEET

    @staticmethod
    def feet_to_meters(feet):
        return feet * UnitConverter.FEET_TO_METER

    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * UnitConverter.KILOGRAM_TO_POUND

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * UnitConverter.POUND_TO_KILOGRAM

    @staticmethod
    def liters_to_gallons(liters):
        return liters * UnitConverter.LITER_TO_GALLON

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * UnitConverter.GALLON_TO_LITER



class UnitConverter:
    def __init__(self):
        # Base unit for length is meters
        self.length_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.34,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }
        
        # Base unit for weight is grams
        self.weight_factors = {
            'grams': 1.0,
            'kilograms': 1000.0,
            'milligrams': 0.001,
            'pounds': 453.592,
            'ounces': 28.3495
        }

    def convert_length(self, value, from_unit, to_unit):
        from_unit, to_unit = from_unit.lower(), to_unit.lower()
        if from_unit not in self.length_factors or to_unit not in self.length_factors:
            return "Invalid unit"
        
        # Convert to base unit (meters), then to target unit
        base_value = value * self.length_factors[from_unit]
        result = base_value / self.length_factors[to_unit]
        return round(result, 4)

    def convert_weight(self, value, from_unit, to_unit):
        from_unit, to_unit = from_unit.lower(), to_unit.lower()
        if from_unit not in self.weight_factors or to_unit not in self.weight_factors:
            return "Invalid unit"
            
        # Convert to base unit (grams), then to target unit
        base_value = value * self.weight_factors[from_unit]
        result = base_value / self.weight_factors[to_unit]
        return round(result, 4)

    def convert_temperature(self, value, from_unit, to_unit):
        from_unit, to_unit = from_unit.lower(), to_unit.lower()
        if from_unit == to_unit:
            return round(value, 4)
            
        # Convert to base unit (Celsius) first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5.0/9.0
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        elif from_unit == 'celsius':
            celsius = value
        else:
            return "Invalid unit"
            
        # Convert from Celsius to target unit
        if to_unit == 'fahrenheit':
            result = (celsius * 9.0/5.0) + 32
        elif to_unit == 'kelvin':
            result = celsius + 273.15
        elif to_unit == 'celsius':
            result = celsius
        else:
            return "Invalid unit"
            
        return round(result, 4)
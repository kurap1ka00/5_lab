def roman_to_arabic(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    prev_value = 0

    for numeral in roman_numeral:
        value = roman_dict[numeral]
        if value > prev_value:
            arabic_numeral += value - 2 * prev_value
        else:
            arabic_numeral += value
        prev_value = value

    return arabic_numeral

arabic_result = roman_to_arabic("IV")
print(arabic_result)

arabic_result = roman_to_arabic("III")
print(arabic_result)  
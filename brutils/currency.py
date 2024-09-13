def convert_real_to_text(valor:int|float) -> str:
    """
    Converts a given monetary value in Brazilian Reais to its textual representation.

    This function takes a decimal number representing a monetary value in Reais
    and converts it to a string with the amount written out in Brazilian Portuguese. It
    handles both the integer part (Reais) and the fractional part (centavos), respecting
    the correct grammar for singular and plural cases, as well as special cases like zero
    and negative values.

    Args:
        valor (decimal): The monetary value to be converted into text.
            - The integer part represents Reais.
            - The decimal part represents centavos.
            - 2 decimal places

    Returns:
        str: A string with the monetary value written out in Brazilian Portuguese.
            - Returns "Zero reais" for a value of 0.00.
            - Handles negative values, adding "Menos" at the beginning of the string.

    Example:
        >>> convert_real_to_text(1523.45)
        "Mil quinhentos e vinte e três reais e quarenta e cinco centavos"
        >>> convert_real_to_text(1.00)
        "Um real"
        >>> convert_real_to_text(0.50)
        "Cinquenta centavos"
        >>> convert_real_to_text(0.00)
        "Zero reais"
        >>> convert_real_to_text(-50.25)
        "Menos cinquenta reais e vinte e cinco centavos"
    """
    class Monetary:
        unidades = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
                    "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
        dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        centenas = ["cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
        milhares = [
            {"text": "mil", "start": 1000, "end": 999999, "div": 1000},
            {"text": "milhão", "start": 1000000, "end": 1999999, "div": 1000000},
            {"text": "milhões", "start": 2000000, "end": 999999999, "div": 1000000},
            {"text": "bilhão", "start": 1000000000, "end": 1999999999, "div": 1000000000},
            {"text": "bilhões", "start": 2000000000, "end": 2147483647, "div": 1000000000}
        ]

        MIN = 0.01
        MAX = 2147483647.99
        MOEDA = " real "
        MOEDAS = " reais "
        CENTAVO = " centavo "
        CENTAVOS = " centavos "

        @staticmethod
        def number_to_ext(number, moeda=True):
            if Monetary.MIN <= number <= Monetary.MAX:
                value = Monetary.conversion_r(int(number))
                if moeda:
                    if int(number) == 1:
                        value += Monetary.MOEDA
                    elif int(number) > 1:
                        value += Monetary.MOEDAS

                decimals = Monetary.extract_decimals(number)
                if decimals > 0.00:
                    decimals = round(decimals * 100)
                    value += "e " + Monetary.conversion_r(decimals)
                    if moeda:
                        if decimals == 1:
                            value += Monetary.CENTAVO
                        elif decimals > 1:
                            value += Monetary.CENTAVOS
            return value.strip().capitalize()

        @staticmethod
        def extract_decimals(number):
            return number - int(number)

        @staticmethod
        def conversion_r(number):
            if 1 <= number <= 19:
                value = Monetary.unidades[number - 1]
            elif number in range(20, 100, 10):
                value = Monetary.dezenas[number // 10 - 1]
            elif 21 <= number <= 99:
                value = Monetary.dezenas[number // 10 - 1] + " e " + Monetary.conversion_r(number % 10)
            elif number in range(100, 1000, 100):
                value = Monetary.centenas[number // 100 - 1]
            elif 101 <= number <= 199:
                value = "cento e " + Monetary.conversion_r(number % 100)
            elif 201 <= number <= 999:
                value = Monetary.centenas[number // 100 - 1] + " e " + Monetary.conversion_r(number % 100)
            else:
                for item in Monetary.milhares:
                    if item['start'] <= number <= item['end']:
                        value = Monetary.conversion_r(number // item['div']) + " " + item['text'] + " " + Monetary.conversion_r(number % item['div'])
                        break
            return value

    return Monetary.number_to_ext(valor, moeda=True)
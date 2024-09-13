from unittest import TestCase
from brutils.currency import convert_real_to_text

class TestCurrency(TestCase):
    def test_convert_real_to_text(self):
        self.assertEqual(convert_real_to_text(0.00), "Zero reais")
        self.assertEqual(convert_real_to_text(0.01), "Um centavo")
        self.assertEqual(convert_real_to_text(0.50), "Cinquenta centavos")
        self.assertEqual(convert_real_to_text(1.00), "Um real")
        self.assertEqual(convert_real_to_text(-50.25), "Menos cinquenta reais e vinte e cinco centavos")
        self.assertEqual(convert_real_to_text(1523.45), "Mil quinhentos e vinte e três reais e quarenta e cinco centavos")
        self.assertEqual(convert_real_to_text(1000000.00), "Um milhão de reais")
        self.assertEqual(convert_real_to_text(2000000.00), "Dois milhões de reais")
        self.assertEqual(convert_real_to_text(1000000000.00), "Um bilhão de reais")
        self.assertEqual(convert_real_to_text(2000000000.00), "Dois bilhões de reais")
        self.assertEqual(convert_real_to_text(1000000000000.00), "Um trilhão de reais")
        self.assertEqual(convert_real_to_text(2000000000000.00), "Dois trilhões de reais")
        self.assertEqual(convert_real_to_text(1000000.45), "Um milhão de reais e quarenta e cinco centavos")
        self.assertEqual(convert_real_to_text(2000000000.99), "Dois bilhões de reais e noventa e nove centavos")
        self.assertEqual(convert_real_to_text(1234567890.50), "Um bilhão duzentos e trinta e quatro milhões quinhentos e sessenta e sete mil oitocentos e noventa reais e cinquenta centavos")

        # Valores próximos a zero
        self.assertEqual(convert_real_to_text(0.001), "Zero reais")
        self.assertEqual(convert_real_to_text(0.009), "Zero reais")

        # Valores negativos em milhões
        self.assertEqual(convert_real_to_text(-1000000.00), "Menos um milhão de reais")
        self.assertEqual(convert_real_to_text(-2000000.50), "Menos dois milhões de reais e cinquenta centavos")

        # Valores grandes com centavos
        self.assertEqual(convert_real_to_text(1000000000.01), "Um bilhão de reais e um centavo")
        self.assertEqual(convert_real_to_text(1000000000.99), "Um bilhão de reais e noventa e nove centavos")

        # implementar mais casos de teste aqui
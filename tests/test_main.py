import unittest
from model import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        """Цей метод викликається перед кожним тестом."""
        self.analyzer = TextAnalyzer()

    def test_analyze(self):
        """Перевіряємо, чи правильно працює метод analyze."""
        result = self.analyzer.analyze("hello world hello")
        expected = {"hello": 2, "world": 1}
        self.assertEqual(result, expected, "Частотний аналіз працює неправильно")

    def test_empty_text(self):
        """Перевіряємо, чи метод повертає порожній словник для порожнього тексту."""
        result = self.analyzer.analyze("")
        expected = {}
        self.assertEqual(result, expected, "Порожній текст повинен повертати порожній словник")

    def test_punctuation(self):
        """Перевіряємо, чи правильно метод ігнорує пунктуацію."""
        result = self.analyzer.analyze("hello, world! hello.")
        expected = {"hello": 2, "world": 1}
        self.assertEqual(result, expected, "Пунктуація має бути проігнорована")

if __name__ == "__main__":
    unittest.main()


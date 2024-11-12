class TextAnalyzer:
    def analyze(self, text):
        words = text.lower().split()
        frequency = {}
        for word in words:
            word = word.strip(".,!?;:")
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency
class Random_data:
    def __init__(self, text, value, timestamp):
        self.text = text
        self.value = value
        self.timestamp = timestamp
    def to_dict(self):
        return {
            'label': self.text,
            'value': self.value,
            'timestamp': self.timestamp
        }
    def __str__(self):
        return f'Text: {self.text} Value: {self.value} Time: {self.timestamp}'
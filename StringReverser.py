class StringReverser:
    def __init__(self, text: str):
        self.text = text

    def reverse_string(self):
        return self.text[::-1]


reverser = StringReverser("سلام دنیا")
reversed_str = reverser.reverse_string()
print(reversed_str)

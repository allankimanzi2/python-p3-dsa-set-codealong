class MySet:
    def __init__(self, enumerable=None):
        self.dictionary = {}
        if enumerable is not None:
            for value in enumerable:
                self.add(value)

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}
        return self

    def __str__(self):
        return f"MySet: {{{', '.join(map(str, self.dictionary.keys()))}}}"

class lenghtIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word_length = len(self.words[self.index])
            self.index += 1
            return word_length
        else:
            raise StopIteration

slyovechki = ["IT Step", "Christmass", "cherry", "minione"]
iterator = lenghtIterator(slyovechki)
ac = 1
for length in iterator:
    print('довжина елементу номер', ac,':',length)
    ac +=1

class AlphabetSequence:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __getitem__(self, index):
        
        if isinstance(index, int):
            return self.letters[index]
        raise TypeError("Index must be an integer")


alphabet = AlphabetSequence()


print(alphabet[0])  
print(alphabet[5])  

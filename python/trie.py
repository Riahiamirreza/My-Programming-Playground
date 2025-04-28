
class Char:
    def __init__(self, string: str):
        self.value = string[0]
        self.children = []
        if len(string) > 1:
            self.children.append(Char(string[1:]))
    def __repr__(self):
        return f'<`{self.value}`>'

class Trie:
    def __init__(self):
        self.chars = []

    def insert(self, word: str):
        chars = self.chars
        for idx, c in enumerate(word):
            if matched:=list(filter(lambda i: i.value == c, chars)):
                matched = matched[0]
                chars = matched.children
                continue
            else:
                partial_word = word[idx:]
                chars.append(Char(partial_word))
                return

    def exists(self, word: str):
        chars = self.chars
        for c in word:
            if matched:=list(filter(lambda i: i.value == c, chars)):
                chars = matched[0].children
                continue
            else:
                return False
        else:
            return True


    def __repr__(self):
        return f'<chars: {self.chars}>'


if __name__ == '__main__':
    words = [
            "car",
            "cat",
            "Casper",
            "apple",
            "app",
            "banana",
            "cycle",
            "student",
            "smart",
            "small"
    ]
    
    t = Trie()

    for w in words:
        t.insert(w)


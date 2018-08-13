class Trie:
    def __init__(self):
        self.trie = {}
        self.size = 0

    def add(self, word):
        p = self.trie
        word = word.strip()
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        if word != '':
            p[''] = ''
    def search(self, word):
        p = self.trie
        word = word.lstrip()
        for c in word:
            if c not in p:
                return False
            p = p[c]
        if '' in p:
            return True
        return False
    def startWith(self, word):
        p = self.trie
        word = word.lstrip()
        for c in word:
            if c not in p:
                return False
            p = p[c]
        return True

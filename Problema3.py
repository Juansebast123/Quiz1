class FuncionAutocomp:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class AutocompTrie:
    def __init__(self):
        self.root = FuncionAutocomp()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = FuncionAutocomp()
            current = current.children[letter]
        current.is_end_of_word = True

    def autocomplete(self, prefix):
        current = self.root
        results = []

        for letter in prefix:
            if letter not in current.children:
                return []   
            current = current.children[letter]

        self._dfs(current, prefix, results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end_of_word:
            results.append(path)
        for letter, next_node in node.children.items():
            self._dfs(next_node, path + letter, results)


trie = AutocompTrie()

palabras = ["sebastian", "secador", "seco", "carpeta", "cargo", "carpintero"]
for palabra in palabras:
    trie.insert(palabra)

print(trie.autocomplete("se"))
print(trie.autocomplete("car"))   
print(trie.autocomplete("lo"))    

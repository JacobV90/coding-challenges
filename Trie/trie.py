import sys

class Trie:
    def __init__(self):
        self.root = {}
        
    def __str__(self):
        words = []
        def _helper(letter, node, word):
            word += letter
            if "-" + word in node[letter]:
                words.append(word)
            node = node[letter]
            for letter in node.keys():
                _helper(letter, node, word)
                
        for letter in self.root.keys():
            _helper(letter, self.root, "")
        return ", ".join(words)
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['-' + word] = {}
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "-" + word in node
            
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True
        

if __name__ == "__main__":
  words = sys.argv[1:] if len(sys.argv) > 1 else ["app", "apple", "bear", "bet"]
  trie = Trie()
  for word in words:
    print(f"Inserting {word}")
    trie.insert(word)
  print(f"Trie contains -> {trie}")
  for word in words:
    print(f"Searching for {word}: {trie.search(word)}")

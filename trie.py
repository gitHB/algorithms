class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print("Добавлена нода: " + word)

    def search_node(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end_of_word else None

    def display(self, node=None, word=''):
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print("В дереве есть: " + word)
        for char, next_node in node.children.items():
            self.display(next_node, word + char)

# Пример использования
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("cat")
trie.insert("car")
trie.insert("dog")
trie.display()
node = trie.search_node("hello")
print("Found" if node else "Not Found")
node = trie.search_node("helloo")
print("Found" if node else "Not Found")
trie.delete("hello")
trie.delete("world")
trie.display()
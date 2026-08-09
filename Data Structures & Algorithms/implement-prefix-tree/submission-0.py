class Node:
    
    def __init__(self, character: str, is_word_end: bool):
        self.character = character
        self.is_word_end = is_word_end
        self.children = dict()

class PrefixTree:

    def __init__(self):
        self.root = Node("root", False)

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character in current.children:
                current = current.children[character]
            else:
                current.children[character] = Node(character, False)
                current = current.children[character]
        
        current.is_word_end = True


    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in current.children:
                return False
            
            current = current.children[character]
        
        return current.is_word_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False
            
            current = current.children[character]
        
        return True
        
        
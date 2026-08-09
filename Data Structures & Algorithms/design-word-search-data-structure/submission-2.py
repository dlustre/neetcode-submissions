class Node:

    def __init__(self, char: str, is_end: bool):
        self.char = char
        self.is_end = is_end
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root = Node("root", False)

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = Node(char, False)
                current = current.children[char]

        current.is_end = True

    def search(self, word: str) -> bool:
        def helper(index: int, node: Node) -> bool:
            print(f"helper({index}, {node.char}), searching for {word[index:]} starting at node {node.char}")
            helper_current = node

            for i, char in enumerate(word[index:]):
                if char == ".":
                    for child in helper_current.children.values():
                        if helper(index + i + 1, child):
                            return True
                    else:
                        return False

                else:
                    if char not in helper_current.children:
                        return False
                    else:
                        helper_current = helper_current.children[char]
            
            return helper_current.is_end

        return helper(0, self.root)

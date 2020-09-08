class TrieNode:
    def __init__(self,val=None,nextlist=[],isWord=False):
        self.val=val
        self.next={i.val:i for i in nextlist}  #nextlist是TrieNode（前缀树结点）的链表
        self.isWord=isWord

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node=TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp=self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i]=TrieNode(i)
            tmp=tmp.next[i]
        tmp.isWord=True
        
        


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp=self.node
        for i in word:
            if i not in tmp.next:
                return False
            else:
                tmp=tmp.next[i]
        return tmp.isWord



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp=self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp=tmp.next[i]
        return True




# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.search('app')
param_4 = obj.startsWith('app')
print(param_2,param_3,param_4)
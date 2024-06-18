# 官方解答 利用字典树
# defaultdict 会在你试图访问一个尚未存在的键时，自动为你创建这个键，并赋予一个默认值，而不需要你事先检查这个键是否存在。
from collections import defaultdict

# Trie 和 Tree 是有区别的，字典树(前缀树) 和 树
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        """
        将给定的单词插入到字典树中。

        插入过程中，如果遇到某个字符对应的子节点不存在，则会创建该子节点。
        如果单词不存在于字典树中，将会标记该节点为一个单词的结尾。

        参数:
        word (str): 需要插入的单词。
        """
        # 从根节点开始，逐字符遍历单词
        cur = self
        for c in word:
            # 如果当前字符的孩子节点不存在，则创建该节点
            cur = cur.children[c]
        # 标记当前节点为一个完整单词的结尾
        cur.is_word = True
        # 保存完整的单词到节点
        cur.word = word



class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 构建字典树
        trie = Trie()
        for word in words:
            trie.insert(word)

        # 深度优先搜索函数
        def dfs(now, i1, j1):
            """
            深度优先搜索函数，用于在字典树中查找所有可能的单词。

            :param now: 当前节点，表示正在搜索的单词的前缀。
            :param i1: 当前处理的字母在棋盘上的行索引。
            :param j1: 当前处理的字母在棋盘上的列索引。
            """
            # 如果当前字母不在当前节点的子节点中，则返回，不继续搜索
            if board[i1][j1] not in now.children:
                return

            # 获取当前处理的字母
            ch = board[i1][j1]

            # 更新当前节点为下一个字母的节点，如果该节点是一个完整的单词，则将其添加到答案集合中
            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            # 标记当前字母为已访问，避免重复访问
            board[i1][j1] = "#"
            # 遍历四个可能的方向，继续深度优先搜索
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                # 如果新位置有效，则继续搜索
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            # 回溯，恢复当前字母的原始状态
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])

        # 遍历棋盘，对于每个字母，进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

sol = Solution()
print(sol.findWords(board, words))
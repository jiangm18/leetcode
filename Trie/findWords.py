from Trie import Trie

def findWords(board, words):
    res = []
    if words == None or len(words) == 0:
        return res
    trie = Trie()
    for word in words:
        trie.add(word)
    m = len(board)
    n = len(board[0])
    visited = []
    for i in range(m):
        visited.append([])
        for j in range(n):
            visited[i].append(False)
    for i in range(m):
        for j in range(n):
            dfs(board, visited, "", i, j, trie, res)
    return res

def dfs(board, visited, strc, i, j, trie, res):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return
    if visited[i][j]:
        return
    strc = strc + board[i][j]
    if not trie.startWith(strc):
        return
    if trie.search(strc):
        res.append(strc)
    visited[i][j] = True
    dfs(board, visited, strc, i-1, j, trie, res)
    dfs(board, visited, strc, i+1, j, trie, res)
    dfs(board, visited, strc, i, j-1, trie, res)
    dfs(board, visited, strc, i, j+1, trie, res)
    visited[i][j] = False

print findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"])
    
    

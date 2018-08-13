def letterCombinations(digits):
    res = []
    if digits == None or len(digits) == 0:
        return res
    dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    letterCombinationsDFS(digits, dic, 0, "", res)
    return res

def letterCombinationsDFS(digits, dic, level, out, res):
    if(level == len(digits)):
        res.append(out)
    else:
        str = dic[digits[level]]
        for i in range(len(str)):
            out = out + str[i]
            letterCombinationsDFS(digits, dic, level+1, out, res)
            out = out[0:len(out)-1]
    
print(letterCombinations("34"))

def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        temp = []
        if digits == None or len(digits) == 0:
            return res
        kb = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        for num in digits:
            temp.append(kb[num])
        count = 1
        for str in temp:
            count = count * len(str)
        time = count/len(temp[0])
        for ch in temp[0]:
            for _ in range(time):
                res.append(ch)
        for i in range(1,len(temp)):
            time = time/len(temp[i])
            k = 0
            while(k<count):
                for ch in temp[i]:
                    for _ in range(time):
                        res[k] = res[k] + ch
                        k = k + 1
        return res

print(letterCombinations("22"))

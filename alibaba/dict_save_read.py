dict_name = {'mean':1, 'std':2}
f = open('temp.txt','w')
f.write(str(dict_name))
f.close()

f = open('temp.txt','r')
a = f.read()
dict_name = eval(a)
f.close()
print dict_name['mean'], dict_name['std']

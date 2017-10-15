import re
'''
match(pattern,string,flags=0)   从头开始查找
search(pattern,string,flags=0)  查找任意位置
findall(pattern,string,flags=0) 查找全部
sub(pattern,repl,string,count=0,flags=0)
	替换, repl可以为函数或字符串
split(pattern,string,maxsplit=0,flags)
	分割字符串
'''
str1="Abacadefa123"
pa=re.compile(r"a",re.I)#1. generate pattern
ma=pa.match(str1)#2. generate match
print(ma.group())#3. check result



ma2=re.match(r"A",str1)
print(ma2.group())

info =re.sub(r'\d+','456',str1)
print(info)


def add1(match):
	val=match.group()
	num=int(val)+1
	return str(num)
	
su=re.sub(r'\d+',add1,str1)
print(su)

sp=re.split(r'a',str1)
print(sp)

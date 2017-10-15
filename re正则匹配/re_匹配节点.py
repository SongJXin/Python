import re


'''
\<number>  引用编号为num的分组匹配到的字符串


'''


ma=re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
print(ma.group())
'''
(?P<name>)  分组起一个别名
(?P=name)   引用别名为name的分组匹配字符串
'''
ma2=re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>')
print(ma2.group())

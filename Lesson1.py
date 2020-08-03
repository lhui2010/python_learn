# Lesson1

print("Hello world")

# Calculation

2 + 2
50 - 5 * 6

"""
division always returns a floating point number
"""

(50 - 5 * 6) / 4
8 / 5

"""
floor division discards the fractional part
"""

17 // 3

"""
the % operator returns the remainder of the division
"""

17 % 3

5 ** 3


# Compare operator

5 == 3

5 != 3

5>=3

5 <= 3

not (5 < 3)

5>=3 and 5 <3

5>=3 or 5 <3


#Variables and Assignment (变量与赋值）
width = 20

width

height = 5 * 9

#Print area size
width * height

#Print perimeter (打印周长)
print ( 2 * (width + height))

#Change variable values (变量值的操作)
width = 20 * width
width *= 20
width += 20

#Which is correct?
name=“ABC”
name_class=123
name_class_3=0x12213F
3_name=“BGH”
int nameA=“BCE”

#Reserved words
import keyword
keyword.kwlist
print('{0: <80}'.format(str(keyword.kwlist), width=80))

import builtins
dir(builtins)

"""
String variables: '', "", and '''
"""

'spam eggs'

# use \' to escape the single quote...
'doesn\'t'

# ...or use double quotes instead
"doesn't"

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

"""
Escape Character (转义字符）
"""

# here \n means newline!
print('C:\some\name')

# note the r before the quote
print(r'C:\some\name')

"""
Operator for string object
"""
'Py'+'thon'

'Py' 'thon'

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

s = 'supercalifragilisticexpialidocious'

len(s)

"""
Exercise:
Coin a SSR sequence with length of 30 nt and repetitive unit of "ATG"
合成一段长度为30nt、重复单元为ATG的微卫星序列：
ATGATGATGATG。。。
"""

word = 'Python'
# character in position 0
word[0]
# character in position 5
word[5]
# slice(切片). character in position 2, 3, 4. Left closed, right open
word[2:5]

"""
Exercise:
print last 6 characters of variable danwei
打印 danwei 变量的最后6个字符
danwei='Kunming Institute of Botany'
"""


a='abc'
b=123
print(a+b)
print(a+str(b))

danwei='Kunming Institute of Botany'
print(danwei.title())
print(danwei.upper())
print(danwei.lower())

danwei='\tKunming Institute of Botany\n'
print(danwei.rstrip() + danwei.rstrip())
print(danwei.lstrip() + danwei.lstrip() )
print(danwei.strip() + danwei.strip() )

#替换掉字符内的空格
print(danwei.replace(' ', ''))

"""
Get Help
"""

import builtins
help(builtins)

"""
Exercise
danwei=‘Kunming Institute of Botany’
>>>type(danwei)
str
>>>help(str)
class str(object)
|  Create a new string object from the given object. If encoding or
>>>dir(str)
'capitalize',
 'casefold',
"""

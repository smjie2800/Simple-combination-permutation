#!/usr/bin/python3
"""
Python中单行注释以 # 开头
多行注释可以用多个 # 号，还有 \''' 和 \"""
"""

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python!")


"""
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
"""
if True:
    print("True")
else:
    print("False")
print("not in else")


"""
python保留字保留字即关键字:['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
import keyword
print(keyword.kwlist)


"""
多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
"""
total: int = 1 + \
            2 + \
            3
print(total)

strings = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(strings)


"""
标准数据类型
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）


数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True，Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，
但可以通过 is 来判断类型。float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j， complex(1,2)
"""
a = b = c = 1
aa, bb, cc = 1, 2, "runoob"
integer: int = 1
boo: bool = False
flo: float = 1.23
comNum: complex = 1 + 2j
comNum1: complex = complex(2, 2)
print(a, b, c, aa, bb, cc, integer, boo, flo, comNum, comNum1)
print(isinstance(integer, int), issubclass(bool, int), bool == 1, bool == 0, True+1, False+1, 1 is True, 0 is False)


"""
数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数， 
在混合计算时，Python会把整型转换成为浮点数
"""
print(2/4, 2//4, 2.5+4)


"""定义类"""


class A:
    pass


class B(A):
    pass


"""
isinstance 和 type 的区别在于
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型
"""
print(isinstance(A(), A), type(A()) == A, isinstance(B(), A), type(B()) == A)


'''
字符串(String)
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号(\''' 或 \""")可以指定一个多行字符串。
转义符 \。
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
            可以由多行组成"""
print(word, sentence, paragraph)

string = '123456789'
print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始后的所有字符
print(string[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(string * 2)  # 输出字符串两次
print(string + '你好')  # 连接字符串

print('------------------------------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


"""
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]，变量[头下标:尾下标:步长]
索引值以 0 为开始值，-1 为从末尾的开始位置
加号 + 是列表连接运算符，星号 * 是重复操作
与Python字符串不一样的是，列表中的元素是可以改变的
"""
list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
tinyList = [123, 'runoob']

print(list1)             # 输出完整列表
print(list1[0])          # 输出列表第一个元素
print(list1[1:3])        # 从第二个开始输出到第三个元素
print(list1[2:])         # 输出从第三个元素开始的所有元素
print(tinyList * 2)     # 输出两次列表
print(list1 + tinyList)  # 连接列表


index = [i for i in range(5)]
print(index)

intList = [1, 2, 3, 4, 5, 6]
intList[0] = 9
intList[2:5] = [13, 14, 15]
print(intList)
intList[2:5] = []   # 将对应的元素值设置为 []
print(intList)

# 以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
letters = ['r', 'u', 'n', 'o', 'o', 'b']
print(letters[1:4:2])
# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：


"""定义函数"""


def reverse_words(word_str):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    words = word_str.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    words = words[-1::-1]

    # 重新组合字符串
    output = ' '.join(words)

    return output


print(reverse_words('I like runoob'))


"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同。
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
"""
tuple1 = ('abcd', 786 , 2.23, 'runoob', 70.2)
tinyTuple = (123, 'runoob')

print(tuple1)              # 输出完整元组
print(tuple1[0])           # 输出元组的第一个元素
print(tuple1[1:3])         # 输出从第二个元素开始到第三个元素
print(tuple1[2:])          # 输出从第三个元素开始的所有元素
print(tinyTuple * 2)      # 输出两次元组
print(tuple1 + tinyTuple)  # 连接元组

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
# tup[0] = 11  修改元组元素的操作是非法的

tup1 = ()     # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号


"""
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
"""
sites = {'Google', 'Taobao', 'Runoob', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典,字典类型也有一些内置的函数，例如 clear()、keys()、values() 等
"""
dicti = {}
dicti['one'] = "1 - 菜鸟教程"
dicti[2] = "2 - 菜鸟工具"

tinyDicti = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dicti['one'])        # 输出键为 'one' 的值
print(dicti[2])            # 输出键为 2 的值
print(tinyDicti)           # 输出完整的字典
print(tinyDicti.keys())    # 输出所有键
print(tinyDicti.values())  # 输出所有值

print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x**2 for x in (2, 4, 6)})   # 该代码使用的是字典推导式
print(dict(Runoob=1, Google=2, Taobao=3))


"""
Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

函数	 描述
int(x [,base])  将x转换为一个整数
float(x)  将x转换到一个浮点数
complex(real [,imag])  创建一个复数
str(x)  将对象 x 转换为字符串
repr(x)  将对象 x 转换为表达式字符串
eval(str)  用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)  将序列 s 转换为一个元组
list(s)  将序列 s 转换为一个列表
set(s)  转换为可变集合
dict(d)  创建一个字典。d 必须是一个 (key, value)元组序列。
frozenset(s)  转换为不可变集合
chr(x)  将一个整数转换为一个字符
ord(x)  将一个字符转换为它的整数值
hex(x)  将一个整数转换为一个十六进制字符串
oct(x)  将一个整数转换为一个八进制字符串

Python 数据类型转换可以分为两种：
隐式类型转换 - 自动完成
显式类型转换 - 需要使用类型函数来转换

隐式类型转换
在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失
"""
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))
print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

num_int = 123
num_str = "456"
print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))

# print(num_int + num_str)  TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Python 为这些类型的情况提供了一种解决方案，称为显式转换
x = int(1)    # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3
print(x, y, z)

x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2")  # w 输出结果为 4.2
print(x, y, z, w)

x = str("s1")  # x 输出结果为 's1'
y = str(2)     # y 输出结果为 '2'
z = str(3.0)   # z 输出结果为 '3.0'
print(x, y, z)

num_int = 123
num_str = "456"
print("num_int 数据类型为:", type(num_int))
print("类型转换前，num_str 数据类型为:", type(num_str))
num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:", type(num_str))

num_sum = num_int + num_str
print("num_int 与 num_str 相加结果为:", num_sum)
print("sum 数据类型为:", type(num_sum))

"""
空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行，Python 解释器运行也不会出错。但是空行的作
用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""


"""
等待用户输入
执行下面的程序在按回车键后就会等待用户输入
"""
input("\n\n按下 enter 键后退出。")


"""
同一行显示多条语句
Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
"""
import sys; x = 'runoob'; sys.stdout.write(x + '\n')


"""
多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
"""
if len(string) > 10:
    print(string + "'s length > 10")
elif 10 >= len(string) > 6:
    print(string + "'s length <= 10 and > 6")
else:
    print(string + "'s length <= 6")


"""
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
"""
x = "a"
y = "b"
# 换行输出
print(x)
print(y)
print('---------')
# 不换行输出
print(x, end=" ")
print(y, end="")
print()


"""
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
import sys   # 导入 sys 模块
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import path   # 导入 sys 模块的 argv,path 成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

"""
Python 推导式
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
Python 支持各种数据结构的推导式
列表(list)推导式
字典(dict)推导式
集合(set)推导式
元组(tuple)推导式


列表推导式格式为：
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
或者 
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。
"""
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper()for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

"""
字典推导基本格式：
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""
listDemo = ['Google', 'Runoob', 'Taobao']
newDict = {key: len(key) for key in listDemo}
print(newDict)

dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

"""
集合推导式基本格式：
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
setNew = {i**2 for i in (1, 2, 3)}
print(setNew)
notIn = {x for x in 'abracadabra' if x not in 'abc'}
print(notIn)

"""
元组推导式基本格式：
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，
另外元组推导式返回的结果是一个生成器对象
"""
tupNew = (x for x in range(1, 10))
print(tupNew)  # 返回的是生成器对象
print(tuple(tupNew))       # 使用 tuple() 函数，可以直接将生成器对象转换成元组

"""
Python运算符


Python算术运算符
以下假设变量 a=10，变量 b=21：
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 向下取接近商的整数	>>> 9//24>>> -9//2-5

Python比较运算符
所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
以下假设变量a为10，变量b为20：
运算符	描述	实例
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。

Python赋值运算符
以下假设变量a为10，变量b为20：
运算符	描述	实例
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
:=	海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。	 
     在这个示例中，赋值表达式可以避免调用 len() 两次:
     if (n := len(a)) > 10: 
        print(f"List is too long ({n} elements, expected <= 10)")
        
Python位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13二进制格式如下：a = 0011 1100, b = 0000 1101
运算符	描述	实例
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 
    输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 
    输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数    

Python逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	逻辑表达式	描述	实例
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False   

Python成员运算符
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
运算符	描述	实例
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True 
"""
a = 10
b = 20
list1 = [1, 2, 3, 4, 5]

if a in list1:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if b not in list1:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if a in list1:
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

"""
Python身份运算符
身份运算符用于比较两个对象的存储单元
运算符	描述	实例
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(x) != id(y)。
            如果引用的不是同一个对象则返回结果 True，否则返回 False。
            
注： id() 函数用于获取对象内存地址

is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
"""
a = 20
b = 20

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

"""
Python运算符优先级
以下表格列出了从最高到最低优先级的所有运算符：
运算符	描述
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，求余数和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
== !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符, and 拥有更高优先级
"""



























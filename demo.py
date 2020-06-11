 print('hello world!')

a=float(input('请输入：'))
b=float(input('请输入:'))
# print('输出结果为:' , a+b)
a="你哈后啊"
print(len(a))


a=input('请输入一段内容:')
b=input('输入第二行文字:')
print('两段内容长度为：',len(a)+len(b))
a = (1,2,3,4,'hahha','喜喜','hahha','很爱很爱你',True,False)
# print(a[-6])
# print(a[0:6])
# print(a[7:9])
# print(a.index('hahha'))
# print(a.count('喜喜' ))
# b = (a,'haha','喜喜')
# print(b[0][3])


a = [1,2,3,4,'hahha','喜喜','hahha','很爱很爱你',True,False]
# a.append('append')
# a.append('apepend0)
# print(a)
a.insert(0,'insert')
print(a)
# 元组一旦写好不再修改，而数组是可以修改的
print(a.pop(2)) #类似剪切的作用
b = a.pop(2)
c = a.pop(2)
print(b+c)
print(b)
print(a)
# a.clear()
print(a)
key = ['你还好吗','请说话']
a.extend(a+key)
print(a)
a.remove('喜喜')
print(a)

xx = [0,False,1,True]
a =xx.count(0)
print(a)
"""
python的语法的一部分!
所用的方法都是小括号结尾的，比如：print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""
"""
字典的特点
1、字典中的值是没有顺序的 。
2、字典的结构必须是键值对的结构。 key:Value
3、字典都是通过key来取value
"""
a = {"name":"张三",0:"好爱好爱你","age":24}
取值

print(a["name"])

# 新增
a["high"] = "183"
print(a)
# 修改
a[0] = "想你的夜"
print(a)
# get
# pop 
# update
b = a.get("name")
print(b)
b = a.pop("name")
print(b)
print(a)
a.update(sex="femal")
print(a)
print("--------------------------------")
print(a.get("name"))
print(a["name"])


del a["name"]
print(a)
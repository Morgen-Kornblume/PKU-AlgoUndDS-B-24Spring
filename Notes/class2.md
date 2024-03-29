# Class 2

## 高阶函数

Python3 吸收了 FP 的特性，加入了“高阶函数”这一特性，使得函数的参数和返回值也可以是一些函数。

## 闭包

闭包就是一些带有自由变量的函数，这些自由变量是在函数定义的时候绑定的，而不是在调用的时候绑定的。

例如：

```python
def outer(x):
    def inner(y):
        nonlocal x
        x += 1
        return x + y
    return inner
    # 闭包中的 x 是自由变量

f = outer(10)
print(f(2)) # 13
print(f(2)) # 14
g = outer(20)
print(g(2)) # 23
print(g(2)) # 24
```

闭包实际上是另一种形式的高阶函数。

闭包内的自由变量还可以在后期调用中被修改。

## 等号和比较问题

### 等号

`x == y` 是比较 x 和 y 的值是否相等，解释器会把它先变成 `x.__eq__(y)`，然后再调用。

如果 `x.__eq__(y)` 返回 `NotImplemented`，那么解释器会尝试调用 `y.__eq__(x)`。

如果 `y.__eq__(x)` 也返回 `NotImplemented`，那么解释器会报出 `RuntimeError`。

### 不等号

同理，不等号也是自定义类的方法（成员函数），默认为 `None`，通过重写可以使得它们有自定义的行为，并且可以使用不等号来比较。

但是，和 `Haskell` 不同的是，`Python` 中的不等号并不是全序关系，比如定义小于号时，不等号并不会自动定义大于号。

sort 函数中的 key 参数可以接受一个函数，这个函数的返回值会被用来排序，其默认使用小于号来比较。


## 类

### 继承与派生

Python 中所有的类都是从 `object` 类派生出来的，因而自动继承了 `object` 类的所有方法。

这些继承来的方法包括：`__new__`、`__init__`、`__del__`、`__str__`、`__repr__`、`__eq__`、`__ne__`、`__lt__`、`__le__`、`__gt__`、`__ge__`、`__hash__`、`__call__`、`__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__iter__`、`__next__`、`__contains__`、`__add__`、`__sub__`、`__mul__`、`__truediv__`、`__floordiv__`、`__mod__`、`__pow__`、`__lshift__`、`__rshift__`、`__and__`、`__or__`、`__xor__`、`__neg__`、`__pos__`、`__abs__`、`__invert__`、`__complex__`、`__int__`、`__float__`、`__index__`、`__round__`、`__trunc__`、`__floor__`、`__ceil__`、`__enter__`、`__exit__`、`__await__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__await__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__await__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__await__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__await__`、`__aiter__`、`__anext__`、`__aenter__`、`__aexit__`、`__await__`、`__aiter__`、`__anext`

可以用 `dir` 函数来查看一个对象的所有方法。

可以注意到的是，这些方法都有双下划线开头和结尾，这是 Python 中的一种约定，表示这些方法是特殊方法，不应该直接调用。

### 静态属性和静态方法

静态属性和静态方法是类的属性和方法，不依赖于类的实例，而是依赖于类本身。

也就是说，它会被所有类的实例对象所共享。

静态方法也不是作用在某个具体的实例对象上的，而是作用在类本身上的，也正因如此，静态方法中不能使用 `self` 关键字。

定义静态方法时，需要在方法的上一行加上 `@staticmethod`。

这是一个装饰器，它会把下面的方法包装成一个静态方法。

静态属性和静态方法都可以通过类名来访问。

### 自定义类（对象）作为字典的键或集合的元素

默认情况下是可以的，但是键值是对象的内存地址（id），而非其内部的值，所以意义并不是很大。

如果想要自定义类作为字典的键或集合的元素，需要重写 `__hash__` 和 `__eq__` 方法。

在Python中，每个对象默认都有__hash__和__eq__方法。这两个方法的默认行为如下：

- __hash__方法：对于不可变的内置类型（如int、float、str、tuple），__hash__方法会返回一个哈希值。对于自定义的类，如果你没有重写__hash__方法，那么这个类的实例的哈希值默认是基于其id的，也就是基于这个对象在内存中的地址。如果一个类定义了__eq__方法并且没有定义__hash__方法，那么这个类的实例将是不可哈希的，也就是说，你不能使用这个类的实例作为字典的键或集合的元素。

- __eq__方法：对于大多数对象，__eq__方法会比较两个对象的id，也就是比较两个对象是否是同一个对象。对于一些内置类型（如list、tuple、str），__eq__方法会比较两个对象的值。对于自定义的类，如果你没有重写__eq__方法，那么这个方法的默认行为是比较两个对象的id。

这是一个例子：

```python
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()

print(hash(obj1))  # 输出: 8739823 (这个值在你的机器上可能会不同)
print(obj1 == obj2)  # 输出: False
```

在这个例子中，我们创建了一个名为MyClass的类，然后创建了这个类的两个实例obj1和obj2。hash(obj1)返回obj1的哈希值，obj1 == obj2比较obj1和obj2是否是同一个对象。

### 迭代器

类如果实现了 `__iter__` 和 `__next__` 方法，那么它就是一个迭代器。

`__iter__` 方法返回一个迭代器对象，`__next__` 方法返回迭代器的下一个元素。

`__iter__` 方法返回的迭代器对象也可以是类的实例对象本身。

比如说你写了一个链表类，你可以让 `__iter__` 方法返回链表的头节点，然后 `__next__` 方法返回当前节点的值，并把当前节点指向下一个节点。

实际上，用 for 循环遍历一个对象时，解释器会自动调用 `__iter__` 方法，然后调用 `__next__` 方法，直到 `__next__` 方法抛出 `StopIteration` 异常，捕获异常，然后 break。这是一个 while 循环的过程，所以说，for 循环的本质是一个 while 循环。


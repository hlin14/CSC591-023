import re,traceback

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f


#================test case================
@O.k
def test_5():
    #Whitespace Formatting
    two_plus_three = 2 + \
                    3
    assert two_plus_three == 5

@O.k
def test_6():
    #Modules
    from collections import defaultdict
    my_defaultdict = defaultdict()
    assert my_defaultdict == {}

@O.k
def test_7():
    #Arithmetic
    assert 5 / 2 == 2.5

@O.k
def test_8():
    #Functions
    def test(x):
        return x * 2
    assert test(4) == 8

@O.k
def test_9():
    #Strings
    not_tab_string = r"\t" + r"\t"
    assert len(not_tab_string) == 4

@O.k
def test_10():
    #Exceptions
    try:
       print(100 // 0)
    except ZeroDivisionError:
       error = "cann't divide by zero"
    assert error == "cann't divide by zero"

@O.k
def test_11():
    #List
    a = [1, 2, 3]
    b = [3, 2, 1]
    assert a + b == [1, 2, 3, 3, 2, 1]

@O.k
def test_12():
    #unpack List
    _, y, _=[1, 2, 3]
    assert  y == 2

@O.k
def test_13():
    #tuple
    my_tuple = (1, 2)
    assert my_tuple[0] == 1

@O.k
def test_14():
    #Dictionaries
    my_dict = {1: "a", 2: "b", 3: "c"}
    assert list(my_dict.values()) == ["a", "b", "c"] and list(my_dict.keys()) == [1, 2, 3]

@O.k
def test_15():
    #Default Dictionaries
    from collections import defaultdict
    my_defaultdict = defaultdict(int)
    assert my_defaultdict[0] == 0

@O.k
def test_16():
    #counters
    from collections import Counter
    s = "12332"
    counter_for_s = Counter(s)
    assert counter_for_s["2"] == 2

@O.k
def test_17():
    #set
    my_list = [1, 2, 3, 2]
    my_set = set(my_list)
    assert len(my_set) == 3

@O.k
def test_18():
    #Control Flow
    x = 0
    for i in range(10):
        x += 1
    assert x == 10

@O.k
def test_19():
    #Truthiness
    x = []
    assert False == bool([])

@O.k
def test_20():
    #Truthiness
    x = []
    assert all([x]) == False
    assert all([]) == True

@O.k
def test_22():
    #Sorting
    x = [10, 24, 22, 52]
    assert sorted(x, reverse = True) == [52, 24, 22, 10]

@O.k
def test_23():
    #List Comprehensions
    a = [0 for x in range(10)]
    b = [y * y for y in range(10)]
    assert len(a) == 10 and b == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

@O.k
def test_24():
    #Generators and Iterators
    def my_generator():
        for i in range(3):
            yield i
    f = my_generator()
    assert next(f) == 0
    assert next(f) == 1
    assert next(f) == 2

@O.k
def test_25():
    #Randomness
    import random
    random.seed(5)
    a = random.random()
    random.seed(5)
    b = random.random()

    c = random.choice([1, 2, 3])

    d = random.randrange(10)

    assert a == b and c in [1, 2, 3] and d <= 9

@O.k
def test_26():
    #Regular Expressions
    s = "hello! how are you?"
    r1 = re.findall(r"\w+",s)
    assert list(r1) == ['hello', 'how', 'are', 'you']

@O.k
def test_27():
    #Object-Oriented Programming
    class dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    my_dog = dog("hee", 2)
    assert my_dog.name == 'hee' and my_dog.age == 2

@O.k
def test_28():
    #Functional Tools - map
    def test(x):
        return x * x
    a = map(test, [1, 2, 3])
    assert list(a) == [1, 4, 9]

@O.k
def test_29():
    #Functional Tools - filter
    def is_odd(x):
        return x % 2 != 0
    a = [1, 2, 3, 4]
    b = filter(is_odd, a)
    assert list(b) == [1, 3]

@O.k
def test_30():
    #enumerate
    a = ['a', 'b', 'c', 'd']
    b = []
    for i, item in enumerate(a):
        b.append(i)
    assert b == [0, 1, 2, 3]

@O.k
def test_31():
    #zip and Argument Unpacking
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    c = list(zip(a, b))
    d, e = zip(*c)
    assert c == [(1, 'a'), (2, 'b'), (3, 'c')] and d == (1, 2, 3) and e == ('a', 'b', 'c')

@O.k
def test_32():
    #args and kwargs
    def test(*args, **kwargs):
        return (args, kwargs)
    assert test(1, 2, 3, msg1 = "hi", msg2 = "how are you") == ((1, 2, 3), {'msg1': 'hi', 'msg2': 'how are you'})

if __name__== "__main__":
  O.report()
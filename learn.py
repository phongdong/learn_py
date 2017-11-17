
import datetime
import random

def age():
    name = input('Give me your name: ')
    age = input('Give me your age: ')
    age = int(age)
    now = datetime.datetime.now()
    year = now.year + (100 - age)

    print("Hello " + name + ", you will be 100 years old in the year " + str(year))

def lessthanten(mylist):
    number = input('Please give me a number: ')
    while(number.isnumeric() == False):
        number = input('please give a real number: ')
    number = int(number)
    mylist = [x for x in mylist if x <= number]


def divisor():
    number = input('Please give me a number: ')
    while(not number.isnumeric()):
        number = input('Please provide a real number: ')
    number = int(number)
    list = range(1,number+1)
    list = [x for x in list if number % x == 0]
    return list

def mergeTrees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None: 
        return t1
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1

def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums)-1, 2):
        sum += min(nums[i], nums[i+1])
    return sum

def arrayPairSum2(nums):
    return sum(sorted(nums)[::2])

def listOverlap(lista, listb):
    common_l = []
    for x in lista:
        if x in listb and x not in common_l:
            common_l.append(x)
    return common_l

def listOverlap2():
    lista = random.sample(range(100), random.randrange(1, 20))
    listb = random.sample(range(100), random.randrange(1, 20))
    print('lista: ', lista)
    print('listb: ', listb)
    lista = [x for x in lista if x in listb]
    return lista

def palindrome():
    words = input('Give word(s): ')
    if words == words[::-1]:
        message = 'palindrome'
    else: 
        message = 'not palindrome'
    return message

def palindrome2():
    words = input('Give word(s): ')
    x = ''
    message = ''
    for i in range(0, len(words)):
        x += words[len(words)-1-i]
    if x == words:
        message = 'palindrome'
    else:
        message = 'not palindrome'
    return message




if __name__ == '__main__':
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1,4, 6,3,2, 5]
    list3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(lessthanten(list))
    # print(divisor())
    # arrayPairSum2(list2)
    # print(list[::-1])

    # testing listOverlap def
    # print('common list: ', listOverlap2())

    # testing palindrome def
    print(palindrome2())





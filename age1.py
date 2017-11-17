def pairArray(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums) - 1, 2):
        sum += min(nums[i], nums[i+1])
    return sum

def pairArray2(nums):
    return sum(sorted(nums)[::2])

def mergeTrees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1

def lessthanTen(nums):
    number = input('Give a number: ')

    while (not number.isnumeric()):
        number = input('Please give a real number: ')
    nums = [x for x in nums if x < int(number)]
    return nums

def divisor():
    num = input('Give me a number: ')
    while not num.isnumeric():
        num = input('Please give a real number: ')
    num = int(num)
    list = []
    for i in range(1, num+1):
        if(num%i==0):
            list.append(i)
    return list

def divisor2():
    num = input('Give me a number: ')
    while not num.isnumeric():
        num = input('Please give a real number: ')
    num = int(num)
    list = range(1, num + 1)
    list = [x for x in list if num % x == 0]
    return list
    


if __name__ == '__main__':
    nums = [1,4,3,2]
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # print(pairArray(nums))
    # print(pairArray2(nums))
    # print(lessthanTen(a))
    print(divisor2())


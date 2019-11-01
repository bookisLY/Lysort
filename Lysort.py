# encoding: utf-8
# module_sort
# by bookist 0.1.0
# no doc
import time
import random
import sys
import copy

# 解锁最大递归数，防止快速排序溢出
sys.setrecursionlimit(1000000)


class Rand_Iter(object):
    """
    DATE:2019/10/31
    version:0.10

    this function can create a range(start,stop,number)
    interable containter.
    get_iter: can fill data in turple or list ...
    get_list: return a list

    """

    def __init__(self, start=None, stop=None, num=None):
        self.start = start
        self.stop = stop
        self.num = num
        self.list = []

    def get_iter(self):
        try:
            while self.num > 0:
                rand = random.randint(self.start, self.stop)
                yield rand
                self.num -= 1
        except Exception:
            raise TypeError('Rand_Iter need three arguments to get a iterable object')

    def get_list(self, iter=None):
        self.list = []
        if iter:
            self.iter = iter
        else:
            self.iter = self.get_iter()

        if self.iter is not None:
            for val in self.iter:
                self.list.append(val)
            print("list created :", self.list)
        return self.list

    def tuple_create(self, list):
        tuple_ = tuple(list)
        print("tuple created :", tuple_)
        return tuple_

    def get_tuple(self, list=None):
        if not list:
            return self.tuple_create(self.list)
        return self.tuple_create(list)


class Lysort():
    """
    DATA:2019/10/13
    version:1.0

    This class provide six sorts function to sort data
    and will print time cost, data will be return,
    and alter a sorted list 
    test functions
    
    """

    def __init__(self, data=None):
        self.data = data

    def __call__(self):
        return "My name is sort, my data: "

    # 封装并将其包装为内置调用
    def time_test(func):
        def wrapper(self, *args, **kwargs):
            time_start = time.time()
            loading = func(self, *args, **kwargs)
            time_cost = time.time() - time_start
            print(func.__name__ + " cost time : " + str((time_cost)))
            return loading

        return wrapper

    @classmethod
    @time_test
    def bubble_sort(self, data):  # 冒泡排序
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    @classmethod
    @time_test
    def insert_sort(self, data):  # 插入排序
        for i in range(1, len(data)):
            insert_value = data[i]
            j = i
            while j > 0 and data[j - 1] > insert_value:
                data[j] = data[j - 1]
                j -= 1
            data[j] = insert_value
        return data

    @classmethod
    @time_test
    def selection_sort(self, data):  # 选择排序
        for i in range(0, len(data)):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
        return data

    @classmethod
    def sub_sort(cls, low, high, data):  # 快速排序分部一
        key = data[low]
        while low < high:
            while low < high and data[high] >= key:
                high -= 1
            data[low] = data[high]
            while low < high and data[low] < key:
                low += 1
            data[high] = data[low]
        data[low] = key
        return low

    @classmethod
    def quick_sort_step(cls, low, high, data):  # #快排分部二
        # low: the first element index
        # high: the end element index

        if low < high:
            key = cls.sub_sort(low, high, data)
            cls.quick_sort_step(low, key - 1, data)
            cls.quick_sort_step(key + 1, high, data)
        return data

    @classmethod
    @time_test
    def quick_sort(cls, low, high, data):
        # low = 0, high = len(list) - 1
        list = cls.quick_sort_step(low, high, data)
        return list

    @classmethod
    def merge_sort_step(cls, list):

        if len(list) <= 1:
            return list
        num = len(list) // 2
        left = cls.merge_sort_step(list[:num])
        right = cls.merge_sort_step(list[num:])
        return cls.merge(left, right)  # 合并

    @classmethod
    def merge(cls, left, right):
        left_index, right_index = 0, 0
        array = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                array.append(left[left_index])
                left_index += 1
            else:
                array.append(right[right_index])
                right_index += 1
        array += left[left_index:]
        array += right[right_index:]
        return array

    @classmethod
    @time_test
    def merge_sort(cls, list):
        list = cls.merge_sort_step(list)
        return list

    @classmethod
    def heap_ify(cls, list, size, root):  # 堆,一次向下重建
        # size = len(list)
        if root > size:
            return
        left = 2 * root + 1
        right = 2 * root + 2
        max = root
        if left < size and list[left] > list[root]:
            max = left
        if right < size and list[right] > list[max]:
            max = right
        if root != max:
            list[root], list[max] = list[max], list[root]
            cls.heap_ify(list, size, max)

    @classmethod
    def build_heap(cls, list, size):  # 创建大顶堆
        # size  = len(list) - 2
        root = size - 1 // 2
        for i in range(root, -1, -1):
            cls.heap_ify(list, size + 1, i)

    @classmethod
    def heap_sort(cls, list, size):  # 大顶堆排序
        # size = len(list) - 1
        cls.build_heap(list, size - 1)
        time_ = time.time()
        for i in range(size, -1, -1):
            list[0], list[i] = list[i], list[0]
            cls.heap_ify(list, i, 0)
        print(time.time() - time_)
        return list



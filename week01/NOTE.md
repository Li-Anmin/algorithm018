学习笔记

- 栈和队列
****
    #python
    class Stack:
        def __init__(self):
			self.items = ['x', 'y']
		def  push(self, item):
			self.items.append(item)
		def pop(self):
			self.items.pop()
		def length(self):
			return len(self.items)

	class Queus:
		def __init__(self):
			self.queue=[]
		def enqueque(self, item):
			self.queque.append(item)
		def dequeue(self):
			if len(self.queque) < 1:
				return None
			reture self.queue.pop(0)
		def size(self):
			return len(self.queque)
****
- 数组和链表
****
    Java,C++: int a[100];
	Python:   list=[]
****
- 跳表核心思想
****
1. 空间换时间
2. 升维
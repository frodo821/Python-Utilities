#-*-coding:utf-8;-*-
#スタック用のlistオブジェクトラッパークラス

class Stack:
    #T スタックに入れたいオブジェクトの型
    #Pythonでジェネリック擬き
    def __init__(self, T):
        self.__stack = list()
        self.TYPE = T
    def __add__(self, other):
        if type(other) is self.TYPE:
            self.PUSH(other)
            return self
        elif type(elem) is not self.TYPE:
            raise TypeError("Item being not initial type cannot be pushed into stack.")
        elif self.GetType() is not elem.GetType():
            raise TypeError("Item being not initial type cannot be pushed into stack.")
        elif type(other) is type(self):
            co = other.Copy()
            while co.HasItem():
                self.PUSH(co.POP())
            return self
        else:
            raise TypeError("Don't support between those types.")
    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        cs = self.Copy()
        co = other.Copy()
        if not cs.GetItemCount() == co.GetItemCount():
            return False
        while cs.HasItem():
            if not cs.POP() == co.POP():
                return False
        return True
    def __ne__(self, other):
        return not self == other
    def __iter__(self):
        yield from self.__stack
    def __len__(self):
        return len(self.__stack)
    def __iadd__(self, elem):
        if type(elem) is self.TYPE:
            self.PUSH(elem)
            return self
        elif type(elem) is not self.TYPE:
            raise TypeError("Item being not initial type cannot be pushed into stack.")
        elif self.GetType() is not elem.GetType():
            raise TypeError("Item being not initial type cannot be pushed into stack.")
        elif type(elem) is type(self):
            ce = elem.Copy()
            while ce.HasItem():
                self.PUSH(ce.POP())
            return self
        else:
            raise TypeError("Don't support between those types.")
    def PUSH(self, item):
        if type(item) is self.TYPE:
            self.__stack.append(item)
        else:
            raise TypeError("Item being not initial type cannot be pushed into stack.")
    def POP(self):
        if self.HasItem():
            return self.__stack.pop()
        raise ReferenceError("Cannot pop from this stack, because this has no item.")
    def ROLL(self):
        self.__stack.insert(0, self.__stack.pop())
    def Copy(self):
        cp = Stack(self.TYPE)
        #参照回避 listのコンストラクタを呼んで参照を分ける
        cp.__stack = list(self.__stack)
        return cp
    def HasItem(self):
        return not len(self.__stack) == 0
    def GetType(self):
        return self.TYPE
    def GetItemCount(self):
        return len(self)

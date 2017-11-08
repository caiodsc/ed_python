class Pilha:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if not self.empty():
            self.stack.pop(len(self.stack) -1)

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if(len(self.stack) == 0):
            return True
        return False

    def length(self):
        return len(self.stack)
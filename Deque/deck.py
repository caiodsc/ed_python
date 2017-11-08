class Deck:

    def __init__(self):
        self.deck = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deck.insert(0,e)
        self.len += 1

    def push_back(self, e):
        #self.deck.insert(self.len, e)
        self.deck.append(e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deck.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            #self.deck.pop(self.len -1)
            self.deck.pop()
            self.len -=1

    def front(self):
        if not self.empty():
            return self.deck[0]
        return None

    def back(self):
        if not self.empty():
            #return self.deck[self.len -1]
            return self.deck[-1]
        return None


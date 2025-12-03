class LockPosition:
    def __init__(self):
        self.position = 50
        self.password_count = 0
    
    def to_string(self):
        return f"\t Pos={self.position} -- Password={self.password_count}"

    def increase(self, num):
        while num > 99:
            self.password_count += 1
            num -= 100
        
        if num == 0:
            return
        
        self.position += num

        if self.position > 99:
            self.password_count += 1
            self.position -= 100

    
    def decrease(self, num):
        while num > 99:
            self.password_count += 1
            num -= 100
        
        if num == 0:
            return

        if self.position == 0:
            self.password_count -= 1
        
        self.position -= num

        if self.position == 0:
            self.password_count += 1

        if self.position < 0:
            self.password_count += 1
            self.position += 100

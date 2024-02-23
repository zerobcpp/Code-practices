class obj:
    def __init__(self, n):
        self.n = n
    
    def __repr__(self) -> str:
        return f'name = {self.n}'


if __name__ == '__main__':
    a = obj('zerr')
    print(a)
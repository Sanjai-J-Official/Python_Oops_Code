class iteror:
    def __iter__(self):
        self.a=1
        return self.a

    def __next__(self):
        x=self.a
        self.a=self.a+1
        return x

iter=iteror() 

    

        
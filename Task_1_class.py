class C1:
    @staticmethod
    def reverse(inp):
        i=inp
        rev=0
        while i>0:
            ld=i%10
            rev=rev*10+ld
            i//=10
        print("this is rev num:",rev)
class C2:
    pass

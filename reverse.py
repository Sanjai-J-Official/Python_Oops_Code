def rev(st):
    return " ".join(st.split()[::-1])
st1='hello world'
st2=st1.split()[::-1]
print(st2)

print(rev("Hello world"))
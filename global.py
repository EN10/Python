globe = 5

def val():
    globe = 7

def ref():
    global globe 
    globe = 7

print(globe)
val()
print(globe)
ref()
print(globe)

# python golbal.py
# 5
# 5
# 7

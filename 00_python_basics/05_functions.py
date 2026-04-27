import random
def max_min(mlist):
    minimum = mlist[0]
    for num in mlist:
        if num < minimum:
            minimum=num
    return minimum

def getValues():
    mlist = random.sample(range(0,100), k=8)
    print(mlist)
    result = max_min(mlist)
    print(f"min value is {result}")

getValues()
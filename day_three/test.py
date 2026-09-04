def findnumber(num):
    if (num>0):
        return "POSSITIVE"
    elif(num<0):
        return "NEGATIVE"
    else:
        return "ZERO"

out=findnumber(10)
print(out)
def oddoreven(numlist):
    output=[]
    for i in numlist:
        if(i%2==0):
            output.append(i)
    return output
numlist=[10, 15, 22, 31, 40]
output=oddoreven(numlist)
print(output)

def find_max(*numbers):
    max=0
    for i in numbers:
        if(i>max):
            max=i
    return max

re=find_max(10, 45, 23, 89, 12)
print(re)


def show_student(**details):
    for key,value in details.items():
        print(f"{key} : {value}")

show_student(
    name="Yousaf",
    age=22,
    course="Python",
    city="Malappuram",
    email="test@gmail.com"
)



import random
pos_int=[1,2,3,4,5,6,7,8,9]
A=[1,2,4,3]
B=[1,3,2,3]
c=[]
def solution(A,B):
    while len(A)==len(B):
        C = random.sample((A+B), len(A))
        print(C)
        for i in pos_int:
            if i in C:
                pass
            else:
                print(int(i))
                break
        break    
    else:
        print("Both list must be of the same size.")
#solution(A,B)
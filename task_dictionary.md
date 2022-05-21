```python
def student(dic):
    for k,v in dic.items() :
        avge={}
        avge[k]=sum (v)/len (v)
        if avge[k]>= 50 :
            print ( avge)
            return ('pass')
        elif avge[k]< 50 :
            print ( avge)
            return ("fail") 
stud ={}
a = int(input("Enter number of student: "))
for i in range(a):
    k = input("Enter student name : ")
    v = []
    n = int(input("Enter number of score : "))
    for i in range(0, n):
        ele = int(input())
        v.append(ele)
    stud.update({k:v})
student(stud)
```


```python

```


```python

```

import random
class_jurnal={}
school_jurnal=[]

i=0
d=0
for i in range(11):
    j=random.randint(0,2)
    if j==0:
        class_char='а'
    if j==1:
        class_char='б'
    if j==2:
        class_char='в'    
        school_class=str(i+1)+ class_char
    scores=[]
    for i in range(10):
        scores.insert(i, random.randint(2,5))         
    class_jurnal={'school_class': school_class, 'scores':scores } 
   
    school_jurnal.insert(i,class_jurnal)
print(school_jurnal)
#print(len(school_jurnal))
   
classroom_sum = []
#slasses = slice(0, None, 1)
classroom_sum.append(sum(school_jurnal[0::1]['scores']) / len(school_jurnal[0::1]['scores']))  
print(classroom_sum) 
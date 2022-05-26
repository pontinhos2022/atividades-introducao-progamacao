VET=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,1,24,25,26,27,28,29,30
    ,31,32,1,34,35,36,37,38,39,40,41,42,43,44,45,1,47,48,49,50]
for num in VET:
    if VET.count(num)>1:
         print(f'O número {num} se repete {VET.count(num)} vezes nas posições {VET.index(1)}, {VET.index(1,1)},'
               f' {VET.index(1,23)}, {VET.index(1,33)}')
         break
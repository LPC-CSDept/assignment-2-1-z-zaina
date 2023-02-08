   
numM = int(input()) # input () returns string value. Need to change it to INT value. 
#Num = int(numM)
numF = input()

Total = numM + numF
percM = numM / (numM + numF) * 100
percF = numF / (numM + numF) * 100 


# output 
Print (‘Total”  ‘ , numM + numF )
Print ( ‘Number of males and females’ , numM, numF )
#Print ( ‘ percentage of males and females ‘ , percM , percF )
Print (f ‘ percentage of amles and females: {percM: . 2f} {percF: . 2f }. )

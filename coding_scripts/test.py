




def main():

    def func(ls) :
        ls.remove(1)

    
    myls=[1,2,3,2]

    func(myls)

    print (myls)
        


    



    
 

   
# def main ():
    
#     A = [1,5,6,14,15]

#     A.sort() #ascending
  
#     if len(A)> 4 :
#         MIO= min([   abs(A[3] -A[len(A)-1]),    abs( A[0] - A[len(A)-4] ),    abs(A[1]- A[len(A)-3] ),    abs(  A[2]- A[len(A)-2] )    ] )    
#     else:
#         # making the 3 changes will always give me the diff equal to 0
#         MIO= 0


#     print(MIO)

if __name__ == '__main__' :
    main()

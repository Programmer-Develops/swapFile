def SwapFileData():
     swap1 = input("Enter 1st file name to Swap:-  ")
     swap2 = input("Enter 2nd file name to Swap:-  ")
     
     with open(swap1, 'r') as a:
         data_a = a.read()
     
     with open(swap2, 'r') as b:
         data_b = b.read()

     with open(swap1, 'w') as a:
         a.write(data_b)

     with open(swap2, 'w') as b:
         b.write(data_a)

     print(swap1)
     print(swap2)

SwapFileData()
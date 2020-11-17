


def SwapFileData ():
    file1name = input('Enter name of file 1: ')
    file2name = input('Enter name of file 2: ')    
    with open(file1name,'r') as a:
        data_a = a.read()
    with open(file2name,'r') as b:
        data_b = b.read() 
    with open(file1name,'w') as a:
        a.write(data_b)
    with open(file2name,'w') as b:
        b.write(data_a)    
    
   

SwapFileData()  
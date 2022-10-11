import numpy as np
def create_matrix(mc):
    print("\nARRAY"+str(mc)+"Elements:")
    array=map(int,input().split())
    array=np.array(list(array))
    print("\n ARRAY"+str(mc)+"ROW COLUMN:")
    row,column=map(int,input().split())
    if(len(array)!=(row*column)):
        print("\n Row and column size not match with total elements!!retry")
        return create_matrix(mc)
    array=array.reshape(row,column)
    print("\n ARRAY"+str(mc))
    print(array)
    return array
x,y=np.linalg.eig(create_matrix(1))
print("\n E-value")
print(x)
print("\n E_vector")
print(y)

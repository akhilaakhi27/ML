import numpy as np
def create_matrix(mc):
    print("\n ARRAY"+str(mc)+"Elements:")
    array=map(int,input().split())
    array=np.array(list(array))
    print("\n ARRAY"+str(mc)+",ROW COLUMN:")
    row,column=map(int,input().split())
    if(len(array)!=(row*column)):
        print("\n Row and column size not match with total elements!!retry")
        return create_matrix(mc)
    array=array.reshape(row,column)
    print("\n ARRAY"+str(mc))
    print(array)
    return array
arr1=create_matrix(1)
arr2=create_matrix(2)
if(arr1.shape==arr2.shape):
    print("\n Dot product")
    print(np.dot(arr1,arr2))
else:
     print("\n Dimensions not matching")


# Series = Column = Vector
# Pandas will generate an index if we don't pass it one.


import pandas as pd

# lists and dics
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
dict1 = {'Name': 'Zara', 'Age': 7, 'Grade': 'First', 'Hair':'Blong', 'Gender':'f'}
dict2 = {'jill':1, 'don':2, 'rob':3, 'sonia':4, 'matt':5, 'dyl':6}



serlist = pd.Series(list2)
# print(serlist)
serdic = pd.Series(dict2)
# print(serdic)



print(serlist[serlist > 2])



# print(serlist[serlist.isnull()])


import pandas as pd
import numpy as np

detail = pd.read_excel('output.xlsx',sheetname=1)
print(detail.shape)
result = pd.pivot_table(detail,index=['score','sex'],aggfunc=np.mean)
print(result)

''''
           age
score sex     
60    女     25
      男     50
90    女     60

'''

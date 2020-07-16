from pandas import read_excel
from multi_density import create_multi_density

data = read_excel('example1.xlsx')
create_multi_density(data,list(data.columns),"density_1")

data = read_excel('example2.xlsx')
create_multi_density(data,'one',"density_2")

data = read_excel('example3.xlsx')
create_multi_density(data,['field_1','field_2'],"density_3")

data = read_excel('example4.xlsx')
create_multi_density(data,['a','b','c','d','e'],"density_4")
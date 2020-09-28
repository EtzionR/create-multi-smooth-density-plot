# create-multi-smooth-density-plot
Gets a  dataframe with several of numeric columns and creates plot that compares the smooth density curves of every selected column.

## introduction
The short and simple code allows a comparison between the smooth density of a large number of columns. Each density is displayed in a different color and conveniently. The code is very simple to run and all you have to do is import it (instructions below). example of one output:

![example](https://github.com/EtzionData/create-multi-smooth-density-plot/blob/master/Output/density_1.png)

## libraries
The code uses the following libraries in Python:

**matplotlib**

**seaborn**

**pandas**

## application
An application of the code is attached to this page under the name: 

[**"implementation.ipynb"**](https://github.com/EtzionData/create-multi-smooth-density-plot/blob/master/implementation.ipynb)
the examples outputs are also attached here.

## Using the code
To use this code, you just need to import it as follows:
``` sh
# import
from multi_density import create_multi_density
from pandas import read_csv

# define variables
data = read_excel(r'path\file.csv')
fields=['a','b','c','d','e','f','g']
names ="my_plot"     # you not need to add ".png"

# application
create_multi_density(data,fields,names)

```

When the variables displayed are:

**data:** pandas dataframe object.

**field:** simple list that contain strings. each one of them is column name inside **"data"** that you want to display its smooth density.

**name:** string which represents the filename of the GIF you want to save

## License
MIT © [Etzion Harari](https://github.com/EtzionData)


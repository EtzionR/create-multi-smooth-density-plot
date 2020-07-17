# create-multi-smooth-density-plot
Gets a  dataframe with several of numeric columns and creates plot that compares the smooth density curves of every selected column.

## introduction
problem
nulti color
simple small
comfterable

3D plots are a significant tool for performing data visualization. At the same time, the main problem with these plots, is that they are usually limited to a very specific angle, and present a three-dimensional reality in a two-dimensional format. Also, standard 3D display methods are usually more complex and sometimes even require complex software and additional installations for those viewing the information.

In order to overcome these gaps, the code here is designed to create GIFs from 3D data. The simple code allows you to enter a pandas dataframe object, and create a GIF output. The code allows the creation of a three-dimensional output that scans the data from any direction and creates for the viewer a feeling that it is indeed a three-dimensional display.

Also, since the output is based on a GIF file, it can be shared with people who do not have any sophisticated software. You can even transfer it via your mobile phone or share it on social networks.

## libraries
The code uses the following libraries in Python:

**matplotlib**

**seaborn**

**pandas**

## application
An application of the code is attached to this page under the name: 

**"implementation.py"** 
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



# Create by Etzion Harari
# https://github.com/EtzionR

# Load libraries:
import matplotlib.pyplot as plt
import seaborn as sns

COLORS = ['red', 'blue', 'green', 'gold', 'purple',
          'lime', 'tomato', 'navy', 'teal', 'maroon']

def create_multi_density(data,fields,name):
    """
    create plot which compare the density of the input fields
    :param data: pandas dataframe
    :param fields: dataframe fields name to plot thier density
    :param name: plot name and filename for the output
    """
    if type(fields)==type(''): fields=[fields]
    plt.figure(figsize=(8, 4))
    for f in range(len(fields)):
        clm = list(data[fields[f]])
        sns.kdeplot(clm, color=COLORS[f%len(COLORS)], label=fields[f])
    plt.title(name)
    plt.xlabel('values of: '+', '.join(fields))
    plt.ylabel('density')
    plt.legend(loc='upper left')
    plt.savefig(name+'.png')
    plt.show()
 
# License
# MIT © Etzion Harari

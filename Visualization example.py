import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import CheckButtons
fig,ax = plt.subplots()
df = sns.load_dataset('iris')
print(df)

df_setosa = df.query(('species=="setosa"')).sort_values(['sepal_length'])
df_versicolor = df.query(('species=="versicolor"')).sort_values(['sepal_length'])
df_virginica = df.query(('species=="virginica"')).sort_values(['sepal_length'])

l0, = ax.plot(df_setosa['sepal_length'],df_setosa['sepal_width'],label='setosa')
l1, = ax.plot(df_versicolor['sepal_length'],df_versicolor['sepal_width'],label='versicolor')
l2, = ax.plot(df_virginica['sepal_length'],df_virginica['sepal_width'],label='virginica')

ax.legend()
checkbox_x_position = 0.05
checkbox_y_position = 0.04
checkbox_width = 0.2
checkbox_height = 0.15
rax = plt.axes([checkbox_x_position,checkbox_y_position,checkbox_width,checkbox_height])
check = CheckButtons(rax,labels=['setosa','versicolor','virginica'],actives=[True,True,True])
def check_box_clicked(label):
    if label == 'setosa':
        l0.set_visible(not l0.get_visible())
    elif label == 'versicolor':
        l1.set_visible(not l1.get_visible())
    else:
        l2.set_visible(not l2.get_visible())
    plt.draw()
check.on_clicked(check_box_clicked)
plt.show()
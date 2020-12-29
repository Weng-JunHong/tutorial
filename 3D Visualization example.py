import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = sns.load_dataset('iris')
df_setosa = df.query('species=="setosa"')
df_versicolor = df.query('species=="versicolor"')
df_virginica = df.query('species=="virginica"')

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')

ax.scatter(df_setosa['sepal_length'],df_setosa['sepal_width'],label='setosa')
ax.scatter(df_versicolor['sepal_length'],df_versicolor['sepal_width'],label='versicolor')
ax.scatter(df_virginica['sepal_length'],df_virginica['sepal_width'],label='virginica')

ax.legend()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\python\elcand.csv',names=['c0','c1','c2','c3','c4','c5','name','c7','gender','birthYear',
                                                'c10','c11','c12','c13','elected','c15'])
df['age'] = 99-df.birthYear
s = df.age.value_counts().sort_index()

plt.title('Age distribution chart of elector ')
plt.xlabel('Years')
plt.ylabel('member')

plt.bar(s.index,s)
plt.show()

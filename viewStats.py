import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
with open("view2D.dat") as f:
    data = f.readlines()
sns.set()
data = [obs[1:] for obs in data if obs[0]=='#']


def to_int(S):
    S = S.apply(lambda x:int(x))
    return S

data = [i.split() for i in data[1:]]
df = pd.DataFrame(data,columns=['Iterations','Health','Exposed',
'Infected','Immune','Severe Infected','Dead'])

df = df.apply(lambda x: to_int(x))

ax = plt.gca()
for i in df.columns[1:]:
    df.plot(x='Iterations',y=i,ax=ax)

plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.ylabel('People')
plt.title('Pandemic curse')

plt.savefig("states.png",bbox_inches='tight')
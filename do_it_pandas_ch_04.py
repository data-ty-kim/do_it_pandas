# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% 04-1 Load Dataset
anscombe = sns.load_dataset("anscombe")
print(anscombe)
print(type(anscombe))

# %% 
dataset_1 = anscombe[anscombe['dataset'] == 'I']
plt.plot(dataset_1['x'], dataset_1['y'], 'o')

# %% Split Dataset and Make Figure
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

# %% Add Plot
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

fig

# %% Set Plot Title
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

fig

# %% Set Figure Title
fig.suptitle("Anscombe Data")

fig

# %% Tune Layout
fig.tight_layout()

fig

# %%

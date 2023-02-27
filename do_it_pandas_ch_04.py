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

# %% 04-2
# Draw a Basic Plot - Histogram
tips = sns.load_dataset("tips")
print(tips.head())
print(type(tips))

fig =plt.figure()
axes1 = fig.add_subplot(1,1,1)
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

fig

# %%
# Draw a Basic Plot - Scatter Plot
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

# %%
# Draw a Basic Plot - Box Plot
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1,1,1)
axes1.boxplot([tips[tips['sex'] == 'Female']['tip'],
               tips[tips['sex'] == 'Male']['tip']],
              labels = ['Female', 'Male'])
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')

# %%
# Add a New Feature
def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1
    
tips['sex_color'] = tips['sex'].apply(recode_sex)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(
    x=tips['total_bill'], 
    y=tips['tip'],
    s=tips['size']*10,      # s means the size of dots
    c=tips['sex_color'],    # c means the color of dots
    alpha=0.5)              # alpha indicates transparency
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

# %% 04-3 about Seaborn Library
# Seaborn Histogram
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')

# %%
# UserWarning: 
# `distplot` is a deprecated function 
# and will be removed in seaborn v0.14.0.
# Please adapt your code to use 
# `displot` (a figure-level function with similar flexibility) 
sns.displot(data=tips, x="total_bill", kde=True)

# %%
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], kde=False)
ax.set_title('Total Bill Histogram')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')

# %%
# UserWarning: 
# `distplot` is a deprecated function 
# and will be removed in seaborn v0.14.0.
# Please adapt your code to use 
# `histplot` (an axes-level function for histograms).

# displot
sns.displot(data=tips, x="total_bill")
# or histplot
sns.histplot(data=tips, x="total_bill")

# %%

ax = sns.displot(data=tips, x="total_bill", kind="kde")
ax.fig.suptitle('Total Bill Density')
ax.set(xlabel='Total Bill',
       ylabel='Unit Probability')

# %%
plt.subplots(1,1)
plt.subplot(1,1,1)
a = sns.displot(data=tips, x="total_bill", kind="kde")

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

# %% UserWarning Occured
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], hist=False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')

# %% UserWarning Occured
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], rug=True)
ax.set_title('Total Bill Histogram with Density and Rug Plot')
ax.set_xlabel('Total Bill')

# %% Count Plot
ax = plt.subplots()
ax = sns.countplot(x='day', data=tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')

# %% Regression Plot
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt

# %% Scatterplot
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt

# %% jointplot: plot with scatter and histogram
joint = sns.jointplot(x='total_bill', y='tip', data=tips)
joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip',
                   fontsize=10, y=1.03)
joint

# %% jointplot: hexbin
hexbin = sns.jointplot(x='total_bill', y='tip', 
                       data=tips, kind='hex')
hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip',
                    fontsize=10, y=1.03)

# %% kdeplot
ax = plt.subplots()
ax = sns.kdeplot(data=tips,
                 x='total_bill',
                 y='tip',
                 fill=True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('tip')

# %% bar plot
ax = plt.subplots()
ax = sns.barplot(x='time', y='total_bill', data=tips)
ax.set_title('Bar plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')

# %% box plot
ax = plt.subplots()
ax = sns.boxplot(x='time', y='total_bill', data=tips)
ax.set_title('Boxplot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

# %% violin plot: to express the variance of the distribution
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', data=tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

# %% pair plot
fig = sns.pairplot(tips)
fig

# %% map_upper, map_lower
pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
plt.show()

# %% Draw a Multivariable Graph
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill',
                    hue='sex', data=tips, split=True)

# %% linear model plot
scatter =  sns.lmplot(x='total_bill', y='tip', data=tips, 
                      hue='sex', fit_reg=False)

# %%
fig = sns.pairplot(tips, hue='sex')

# %%
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
#                      fit_reg=False, hue='sex',
#                     #  scatter_kws={'s': tips['size']*10}
#                      )

sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='sex', size='size')

# %%
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='sex', size=tips['size'].mul(20))

# %%
sns.relplot(data=tips, kind='scatter',
            x='total_bill', y='tip', hue='sex', size='size')

# %%
sns.relplot(data=tips, kind='scatter',
            x='total_bill', y='tip', hue='sex', 
            size=tips['size'].mul(20))

# %% 4 data in 1 plot
anscombe_plot = sns.lmplot(x='x', y='y', 
                           data=anscombe, fit_reg=False)

# %% 4 data in 4 plots
anscombe_plot = sns.lmplot(x='x', y='y',
                           data=anscombe, fit_reg=False,
                           col='dataset',
                           col_wrap=2       # max number of cols
                           )

# %% Using FacetGrid
facet = sns.FacetGrid(tips, col='time')
facet.map(sns.distplot, 'total_bill', rug=True)

# %%
facet = sns.FacetGrid(tips, col='day', hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()

# %%
facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')

# %% 04-4
ax = plt.subplots()
ax = tips['total_bill'].plot.hist()

# %%
fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(
    alpha=0.5, bins=20, ax=ax
    )

# %%
ax = plt.subplots()
ax = tips['tip'].plot.kde()

# %%
fig, ax = plt.subplots()
ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax)

# %%
fig, ax = plt.subplots()
ax = tips.plot.hexbin(x='total_bill', y='tip', ax=ax)

# %%
fig, ax = plt.subplots()
ax = tips.plot.hexbin(x='total_bill', y='tip', gridsize=10, ax=ax)

# %%
fig, ax = plt.subplots()
ax = tips.plot.box(ax=ax)

# %% 04-5 Set Graph Style 
# before adjust
fig, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill',
                    hue='sex', data=tips, split=True)

# %%
# after adjust
sns.set_style('whitegrid')
fig, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', 
                    hue='sex', data=tips, split=True)

# %% using for-loop 
fig = plt.figure()

seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(x='time', y='total_bill', 
                                data=tips, ax=ax)
        violin.set_title(style)

fig.tight_layout()

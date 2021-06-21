import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

sns.set(style='ticks', font_scale=1.2)

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

%matplotlib inline


def sort_plot_by_mean(df, by, column, rot=0):
    df2 = pd.DataFrame({col:vals[column] for col, vals in df.groupby(by)})
    meds = df2.mean().sort_values(ascending=False)
    return meds


def exampple_boxplot():
  sns.boxplot(data=df_to_plot[df_to_plot['Label'] == 'female'],
              x='Similarity to First Component',
              y='Seeds',
              hue='Test',
              palette=sns.set_palette(sns.color_palette(['#a1d99b', '#e5f5e0'])),
              showfliers=False,
              ax=ax,
              order=sort_by_mean(df_to_plot, 
                                 by=['Seeds'], 
                                 column='Similarity to First Component').index.values)

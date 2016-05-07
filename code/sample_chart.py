import pandas as pd
import matplotlib.pyplot as plt
#pd.set_option('display.mpl_style', None)


repo_df = pd.read_csv('../input/FRB_Z1_cleaned.csv', parse_dates=['date'], dayfirst=False, index_col='date')

#now it's in trillions
repo = pd.Series(repo_df['all_asset'])/1000000

plt.figure(figsize=(7, 3))
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Repo", fontsize=10)
plt.ylabel("Trillion $", fontsize=10)
plt.grid(True)
plt.plot(repo.index.values,repo, color="#3F5D7D")
plt.savefig('../img/sample.pdf', bbox_inches="tight")

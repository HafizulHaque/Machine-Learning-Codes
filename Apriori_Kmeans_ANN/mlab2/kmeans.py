import pandas as pd
import os, sys
from sklearn.cluster import KMeans
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from userkmean import userKmeans1
from userkmean2 import userKmeans2
import seaborn as sns

sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=0.5)

fname = os.path.join(sys.path[0], "wine.xlsx")

df1 = pd.read_excel(fname, sheet_name='wine')
df = df1.values.tolist()
#print(df1.head())
# print(df.shape)
#for row in df:
#    print(row)
# print(df.info())

km = KMeans(n_clusters=5, init='random')
y_km = km.fit_predict(df)

print("User Function (Updating takes place after all iterations)")
u1_km = userKmeans1(df, nok=5, run=20)
#print("User Function (Updating takes place after each iteration)")
#u2_km = userKmeans2(df, nok=5, run=20)

colors_palete = {0: "red", 1: "green", 2: "blue", 3: "black", 4: "yellow"}
colors1 = [colors_palete[c] for c in y_km]
colors2 = [colors_palete[c] for c in u1_km]
#colors3 = [colors_palete[c] for c in u2_km]

# scatter_matrix(df,alpha = 0.4,figsize = (130,130),color = colors,diagonal='kde')

# plt.show()

fig = plt.figure(figsize=(18, 18))
ax1 = fig.add_subplot(211)
ax1.title.set_text("Using Scikit-learn classifier")
ax2 = fig.add_subplot(212)
ax2.title.set_text("Using user function (Update after all iterations)")
#ax3 = fig.add_subplot(313)
#ax3.title.set_text("Using user function (Update after each iteration)")

pca = PCA(n_components=2)
pca_2d = pca.fit_transform(df1)

# tsne = TSNE(random_state=123,n_components=3).fit_transform(df1)
# pca_2d = tsne

ax1.scatter(pca_2d[:, 0], pca_2d[:, 1], c=colors1, s=50)
ax2.scatter(pca_2d[:, 0], pca_2d[:, 1], c=colors2, s=50)
#ax3.scatter(pca_2d[:, 0], pca_2d[:, 1], c=colors3, s=50)

ax1.set_xticks([])
ax2.set_xticks([])
#ax3.set_xticks([])

plt.show()

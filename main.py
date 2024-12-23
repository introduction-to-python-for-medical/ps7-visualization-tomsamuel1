import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)

features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[2], features[4], features[6], features[7]]
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

reference_feature = selected_features[1]
reference_feature
y = df[reference_feature]
x = df[selected_features[0]]
plt.scatter(x, y)
plt.xlabel(selected_features[0])
plt.ylabel(reference_feature)
plt.show()

reference_feature = selected_features[1]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()

reference_feature = selected_features[0]  
comparison_feature = selected_features[1]  


plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)


plt.savefig('correlation_plot.png')

plt.show()

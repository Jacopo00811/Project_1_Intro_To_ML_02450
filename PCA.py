from scipy.linalg import svd
import matplotlib.pyplot as plt
from ExtractData import *
from sklearn.preprocessing import normalize, scale
from mpl_toolkits.mplot3d import Axes3D


X = X.copy()
N = X.shape[0]
X_PCA=X[:, 2:-1]
Y = normalize(X_PCA)
Y = scale(X_PCA)
U, S, Vh = svd(Y, full_matrices=False)
V = Vh.T
rho = (S * S) / (S * S).sum()
threshold = 0.9



# # Plot variance explained
# plt.figure()
# plt.plot(range(1, len(rho) + 1), rho, "x-")
# plt.plot(range(1, len(rho) + 1), np.cumsum(rho), "o-")
# plt.plot([1, len(rho)], [threshold, threshold], "k--")
# plt.xlabel("Principal component", fontweight="bold")
# plt.ylabel("Variance explained", fontweight="bold")
# plt.legend(["Individual", "Cumulative", "Threshold"])
# plt.grid()
# plt.title("Variance explained by principal components", fontsize=20, fontweight="bold", color="red")
# plt.show()


def plot_PCA(y, C, Z, i, j):
    _ = plt.figure()
    plt.title("Sport car data: PCA", fontweight="bold", fontsize=20, color="red")
# Z = array(Z)
    for c in range(C):
    # select indices belonging to class c:
        class_mask = y == c
        plt.plot(Z[class_mask, i], Z[class_mask, j], "o", alpha=0.5)
    plt.legend(Countries)
    plt.xlabel("PC{0}".format(i + 1), fontweight="bold")
    plt.ylabel("PC{0}".format(j + 1), fontweight="bold")

    plt.show()


y = np.array([CountriesDict[cl] for cl in Country])
N = len(y)
M = len(attributes)
C = len(Countries)
# Project the centered data onto principal component space
Z = Y @ V
# Indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA1 vs PCA2 of the data
# plot_PCA(y, C, Z, i, j)


# Plot PCA2 vs PCA3 of the data
i += 1
j += 1
# plot_PCA(y, C, Z, i, j)


# Plot PCA1 vs PCA3 of the data
i -= 1
# plot_PCA(y, C, Z, i, j)


# Plot 3D PCA1 vs PCA2 vs PCA3 of the data
ind = [0, 1, 2]
colors = [
    "blue",   
    "green", 
    "red",    
    "orange", 
    "purple",
    "cyan",   
    "magenta",
    "yellow", 
    "brown",  
    "pink"   
]
f = plt.figure()
ax = f.add_subplot(111, projection="3d")  # Here the mpl_toolkits is used
for c in range(C):
    class_mask = y == c
    s = ax.scatter(
        Z[class_mask, ind[0]], Z[class_mask, ind[1]], Z[class_mask, ind[2]], c=colors[c]
    )
plt.legend(Countries, loc='upper left', bbox_to_anchor=(1, 1))
ax.view_init(30, 220)
ax.set_xlabel("PCA1", fontweight="bold")
ax.set_ylabel("PCA2", fontweight="bold")
ax.set_zlabel("PCA3", fontweight="bold")
plt.title("Sport car data: PCA", fontweight="bold", fontsize=20, color="red")
plt.show()


# Plot PCA
# N, M = X_PCA.shape
# pcs = [0, 1, 2]
# legendStrs = ['PC' + str(e+1) for e in pcs]
# c = ['r', 'g', 'b']
# bw = 0.2
# r = np.arange(1, M+1)
# for i in pcs:    
#     plt.bar(r+i*bw, V[:,i], width=bw)
# plt.xticks(r+bw, attributes[3:-1])
# plt.xlabel('Attributes', fontweight="bold")
# plt.ylabel('Component coefficients', fontweight="bold")
# plt.legend(legendStrs)
# plt.grid()
# plt.title('PCA Component Coefficients', fontweight="bold", fontsize=20, color="red")
# plt.show()
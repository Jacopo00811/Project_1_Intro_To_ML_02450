from ExtractData import *
import matplotlib.pyplot as plt


X = X[:, 2:-1].copy()

# Normalize the data with added checks to prevent NaN values
X_mean = X.mean(0)
X_std = X.std(0)

# Add a small epsilon to avoid division by zero
X_std[X_std == 0] = 1e-6

X = (X - X_mean) / X_std

# Check and handle NaNs or infinite values
X = np.nan_to_num(X)

print(f"The used data matrix has shape: {X.shape}")
attributes = attributes[3:-1]
print(f"The used attributes are: {attributes}")
y = np.array([CountriesDict[cl] for cl in Country])

N = len(y)
M = len(attributes)
C = len(Countries)

num_bins = 20 

# # Histograms of the data
# plt.figure(figsize=(8, 7))
# u = np.floor(np.sqrt(M))
# v = np.ceil(float(M) / u)
# for i in range(M):
#     plt.subplot(int(u), int(v), i + 1)
#     plt.hist(X[:, i], color=(0.2, 0.8 - i * 0.2, 0.4), bins=num_bins)
#     plt.xlabel(attributes[i], fontweight="bold")
#     plt.ylim(0, N / 2)
# plt.suptitle("Histograms of the values", fontsize=20, fontweight="bold", color="red")
# plt.show() 




# # Boxplot of the data
# plt.boxplot(X)
# plt.xticks(range(1, 6), attributes)
# plt.title("Sport car dataset - boxplot", fontsize=20, fontweight="bold", color="red")
# plt.show()


# # Boxplots per county 
# plt.figure(figsize=(25, 6)) 
# for c in range(C):
#     plt.subplot(1, C, c + 1)  
#     class_mask = y == c  # Binary mask to extract elements of class c

#     if np.sum(class_mask) == 0:
#         print(f"No data for class {Countries[c]}")
#         continue

#     plt.boxplot(X[class_mask, :])
#     plt.title("Class: " + Countries[c], fontweight="bold")
#     plt.xticks(range(1, len(attributes) + 1), [a[:7] for a in attributes], rotation=45)  # Set x-tick labels

#     y_up = X[class_mask].max() + (X[class_mask].max() - X[class_mask].min()) * 0.1
#     y_down = X[class_mask].min() - (X[class_mask].max() - X[class_mask].min()) * 0.1

#     plt.ylim(y_down, y_up)  # Set y limits based on class data
# plt.suptitle("Boxplots of the data for each country", fontsize=20, fontweight="bold", color="red")
# plt.tight_layout() 
# plt.show()


# # Scatter plot grid
# plt.figure(figsize=(12, 10))
# for m1 in range(M):
#     for m2 in range(M):
#         plt.subplot(M, M, m1 * M + m2 + 1)
#         for c in range(C):
#             class_mask = y == c
#             plt.plot(np.array(X[class_mask, m2]), np.array(X[class_mask, m1]), ".")
#             if m1 == M - 1:
#                 plt.xlabel(attributes[m2])
#             else:
#                 plt.xticks([])
#             if m2 == 0:
#                 plt.ylabel(attributes[m1])
#             else:
#                 plt.yticks([])
#             # plt.ylim(0,X.max()*1.1)
#             # plt.xlim(0,X.max()*1.1)
# plt.legend(Countries, loc='upper left', bbox_to_anchor=(1, 1)) 
# plt.suptitle("Scatter plot grid of the data", fontsize=20, fontweight="bold", color="red")
# plt.show()

# Calculate the number of car per each country
country_count = np.zeros(C)
for i in range(C):
    country_count[i] = np.sum(y == i)
print(f"Number of cars per country: {country_count}")

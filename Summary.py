from scipy import stats
from ExtractData import *

# Find mean, mode, median, variance, standard deviation, max and min, percentiles for each attribute
mean = np.mean(X, axis=0)
mode = stats.mode(X, axis=0)[0]
median = np.median(X, axis=0)
variance = np.var(X, axis=0)
std = np.std(X, axis=0)
max_val = np.max(X, axis=0)
min_val = np.min(X, axis=0)
percentiles = np.percentile(X, [25, 75], axis=0)

attributes = np.asarray(df.columns)
print(attributes)
# Creating the table
statistics_table = {
    "Attribute": [attributes[i] for i in range(X.shape[1])],
    "Mean": mean.round(3),
    "Mode": mode.round(3),
    "Median": median.round(3),
    "Variance": variance.round(3),
    "Std Dev": std.round(3),
    "Max": max_val.round(3),
    "Min": min_val.round(3),
    "25th Percentile": percentiles[0].round(3),
    "75th Percentile": percentiles[1].round(3),
}

df_statistics = pd.DataFrame(statistics_table)
# print(df_statistics)

latex_table = df_statistics.to_latex(index=False, header=attributes, escape=False, float_format="%.3f")
print(latex_table)
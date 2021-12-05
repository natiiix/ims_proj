import pandas as pd
import pingouin as pg
from scipy import stats

print("Ukol 1:")
df_ukol1 = pd.read_excel("ukol1.xlsx")
X = df_ukol1["X [ms]"]
Y = df_ukol1["Y[ms]"]

# print(stats.normaltest(X))
# print(stats.normaltest(Y))

for alt in ["two-sided", "less", "greater"]:
    mwr = stats.mannwhitneyu(X, Y, alternative=alt)
    print(alt, mwr)


print("Ukol 2:")
df_ukol2 = pd.read_excel("ukol2.xlsx")

ukol2_melt = pd.melt(df_ukol2, id_vars=["cas"], value_vars=["ticho", "hudba", "hluk", "krik"])
ukol2_melt.columns = ["cas", "hlucnost", "hodnota"]
ukol2_melt.dropna(inplace=True)
ukol2_melt.reset_index(inplace=True)

print(pg.anova(data=ukol2_melt, dv="hodnota", between=["cas", "hlucnost"], effsize="n2", ss_type=2))

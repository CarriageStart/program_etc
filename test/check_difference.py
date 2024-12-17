import numpy as np
import pandas as pd


from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

from matplotlib impoort pyplort as plt
import seaborn as sns


def skew(x):
    return stats.skew(x)

def kurtosis(x):
    return stats.kurtosis(x)

df_f_oneway = pd.read_csv("dat.csv")
print(df_f_oneway.head())
print(df_f_oneway.info())
print(df_f_oneway.isnull().sum())
print(df_f_oneway['type'].value_counts())
print(df_f_oneway.describe())

df_one_anova = df_f_oneway.drop("machine", axis=1)
type1 = df_one_anova[df_one_anova["type"]==1]["defRate"]
type2 = df_one_anova[df_one_anova["type"]==2]["defRate"]
type3 = df_one_anova[df_one_anova["type"]==3]["defRate"]
type4 = df_one_anova[df_one_anova["type"]==4]["defRate"]

levene = stats.levene(type1, type2, type3, type4)
print("Statistics : %.3f \n p-value : %.3f" % (levene))

levene = stats.levene(type1, type2, type3, type4, center="mean")
print("Statistics : %.3f \n p-value : %.3f" % (levene))

fligner = stats.fligner(type1, type2, type3, type4)
print("Statistics : %.3f \n p-value : %.3f" % (fligner))

bartlett = stats.bartlett(type1, type2, type3, type4)
print("Statistics : %.3f \n p-value : %.3f" % (bartlett))

oneway_anova_result = stats.f_oneway(type1, type2, type3, type4)
print(oneway_anova_result)
print("Statistics : %.3f \n p-value : %.3f" % (oneway_anova_result[0], oneway_anova_result[1]))
if oneway_anova_result[1] < 0.05:
    print("Different Distribution!")





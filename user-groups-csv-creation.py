import pandas as pd

alg_csv = "data/alg-total-grades-per-user.csv"
under_alg_csv = "data/under-alg-total-grades-per-user.csv"

alg_df = pd.read_csv(alg_csv)
under_alg_df = pd.read_csv(under_alg_csv)

##################################################################
alg_group_5 = alg_df[alg_df.final >= 0.9]
alg_group_4 = alg_df[(alg_df.final >= 0.8) & (alg_df.final < 0.9)] 
alg_group_3 = alg_df[(alg_df.final >= 0.65) & (alg_df.final < 0.8)] 
alg_group_2 = alg_df[(alg_df.final >= 0.5) & (alg_df.final < 0.65)]

alg_group_5.to_csv("data/alg_group_5.csv", index=False)
alg_group_4.to_csv("data/alg_group_4.csv", index=False)
alg_group_3.to_csv("data/alg_group_3.csv", index=False)
alg_group_2.to_csv("data/alg_group_2.csv", index=False)

###################################################################
under_alg_group_5 = under_alg_df[under_alg_df.final >= 0.9]
under_alg_group_4 = under_alg_df[(under_alg_df.final >= 0.8) & (under_alg_df.final < 0.9)] 
under_alg_group_3 = under_alg_df[(under_alg_df.final >= 0.65) & (under_alg_df.final < 0.8)] 
under_alg_group_2 = under_alg_df[(under_alg_df.final >= 0.5) & (under_alg_df.final < 0.65)]

under_alg_group_5.to_csv("data/under_alg_group_5.csv", index=False)
under_alg_group_4.to_csv("data/under_alg_group_4.csv", index=False)
under_alg_group_3.to_csv("data/under_alg_group_3.csv", index=False)
under_alg_group_2.to_csv("data/under_alg_group_2.csv", index=False)

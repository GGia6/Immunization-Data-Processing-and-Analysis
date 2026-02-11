#Gianna Gatling xfj5db
import pandas as pd
from final_project import ImmunizationData

data = ImmunizationData("vaccine_data.csv")

BCG_2019 = data.make_subset(vaccine=["BCG"], year=["2019"])
regions = list(BCG_2019['Region'])
percentages = list(BCG_2019['Percentage'])
BCG_2019_series = pd.Series(percentages, index=regions)
data.make_plot(BCG_2019_series, title="BCG Vaccine Coverage in 2019 by Region", bar=True)

DTP1_EAPR = data.make_subset(region=["East_Asia_and_Pacific"], vaccine=["DTP1"])
years = list(DTP1_EAPR['Year'])
percentages = list(DTP1_EAPR['Percentage'])
DTP1_EAPR_series = pd.Series(percentages, index=years)
data.make_plot(DTP1_EAPR_series, title="DTP1 Vaccinations in East Asia and Pacific Region", bar=False)

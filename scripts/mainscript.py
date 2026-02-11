#Gianna Gatling xfj5db
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ImmunizationData:
    def __init__(self, file_path):
        self.__df = pd.read_csv(file_path, header=None)
        self.__clean_data()

    def __clean_data(self):
        self.__df.columns = ['Region', 'Vaccine', 'Year', 'Percentage']
        new_regions = []
        for i in range(len(self.__df)):
            region = self.__df.loc[i, 'Region']
            region = region.strip()
            region = region.replace('&', 'and')
            region = region.replace(' ', '_')
            new_regions.append(region)
        self.__df['Region'] = new_regions
        years = []
        for i in range(len(self.__df)):
            years.append(str(self.__df.loc[i, 'Year']))
        self.__df['Year'] = years
        vaccine_dict = {
            'BCG': 'Tuberculosis',
            'DTP1': 'Diphtheria, Tetanus, Pertussis',
            'DTP3': 'Diphtheria, Tetanus, Pertussis',
            'MCV1': 'Meningococcal Disease',
            'MCV2': 'Meningococcal Disease',
            'HEPB3': 'Hepatitis B',
            'HEPBB': 'Hepatitis B',
            'HIB1': 'Haemophilus Influenza',
            'HIB3': 'Haemophilus Influenza',
            'IPV1': 'Polio',
            'IPV3': 'Polio',
            'POL3': 'Polio',
            'PCV3': 'Pneumococcal Disease',
            'RCV1': 'Rubella',
            'ROTAC': 'Rotavirus',
            'YFV': 'Yellow Fever Virus'
        }

        self.__df['Description'] = self.__df['Vaccine'].replace(vaccine_dict)

    def make_subset(self, region=None, vaccine=None, year=None):
        df = self.__df
        if region != None:
            df = df[df['Region'].isin(region)]
        if vaccine != None:
            df = df[df['Vaccine'].isin(vaccine)]
        if year != None:
            df = df[df['Year'].isin(year)]
        return df.copy()

    import seaborn as sns
    import matplotlib.pyplot as plt

    def make_plot(self, series_object, title='', bar=True):
        df = series_object.reset_index()
        df.columns = ['Index', 'Percentage']
        if bar:
            sns.barplot(x=df['Index'], y=df['Percentage'])
        else:
            sns.lineplot(x=df['Index'], y=df['Percentage'])
        plt.title(title)
        plt.xlabel('Index')
        plt.ylabel('Percentage')
        plt.show()

    def __str__(self):
        rows = str(len(self.__df))
        cols = str(len(self.__df.columns))
        return "This instance of class ImmunizationData has " + rows + " rows and " + cols + " columns."

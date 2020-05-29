import sys
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from FileLoader import FileLoader


class Komparator():
    def __init__(self, df):
        self.df = df

    def feature(self, data, name, col):
        if name == 'drop':
            # threshold = 0.7
            # Dropping columns with missing value rate higher than threshold
            # data = data[data.columns[data.isnull().mean() < threshold]]
            # Dropping rows with missing value rate higher than threshold
            # data = data.loc[data.isnull().mean(axis=1) < threshold]
            # Dropping row with missing value for the given column
            data = data[data[col].notnull()]
        if name == 'numinputzero':
            # Filling all missing values with 0
            data = data.fillna(0)
        if name == 'numinputmedian':
            # Filling missing values with medians of the columns
            data = data.fillna(data.median())
        if name == 'catinput':
            # Max fill function for categorical columns
            data[col].fillna(data[col].value_counts().idxmax(), inplace=True)
        return data

    def compare_box_plots(self, categorical_var, numerical_var):
        plt.close('all')
        hweight = self.df.copy()
        for cat in categorical_var:
            hweight = self.feature(hweight, 'drop', cat)
        # hweight = self.feature(hweight, 'drop', 'Height')
        # hweight = self.feature(hweight, features, 'Weight')
        # hweight = self.feature(hweight, features, 'Height')
        hweight.boxplot(column=numerical_var, by=categorical_var)
        plt.show()

    def density(self, categorical_var, numerical_var):
        plt.close('all')
        fig = plt.figure()
        x = 1
        for categorical in categorical_var:
            col_value = self.df[categorical].values.ravel()
            for cat in pandas.unique(col_value):
                hweight = self.df.copy()
                hweight = hweight[hweight[categorical_var] == cat]
                fig.add_subplot(1, len(pandas.unique(pandas.unique(col_value))), x)
                for num in numerical_var:
                    hweight = self.feature(hweight, 'drop', num)
                    sns.distplot(hweight[num],
                                 hist=False, label=num, axlabel=cat)
                x += 1
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        plt.close('all')
        fig = plt.figure()
        x = 1
        col_value = self.df[categorical_var].values.ravel()
        for cat in pandas.unique(pandas.unique(col_value)):
            hweight = self.df.copy()
            hweight = hweight[hweight[categorical_var] == cat]
            fig.add_subplot(1, len(pandas.unique(pandas.unique(col_value))), x)
            plt.ylabel = cat
            for num in numerical_var:
                hweight = self.feature(hweight, 'drop', num)
                plt.hist(hweight[num], label=num)
                plt.xlabel = num
            x += 1
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    komp = Komparator(data)
    komp.compare_box_plots(['Sex', 'Season'], 'Height')
    # komp.density(['Sex', 'Season'], 'Height')
    # komp.compare_histograms(['Sex', 'Season'], 'Height')
    pass

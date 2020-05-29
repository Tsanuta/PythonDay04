
from FileLoader import FileLoader
import sys
import pandas
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib():
    def feature(self, data, name, col):
        if name == 'drop':
            # threshold = 0.7
            # Dropping columns with missing value rate higher than threshold
            # data = data[data.columns[data.isnull().mean() < threshold]]
            # Dropping rows with missing value rate higher than threshold
            # data = data.loc[data.isnull().mean(axis=1) < threshold]
            # Dropping row with missing value for the given column
            data = data[data[col].isnull() == 0]
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

    def histogram(self, data, features='drop'):
        plt.close('all')
        # age = data.copy()
        # age = self.feature(age, features, 'Age')
        # age.hist(column='Age')
        # height = data.copy()
        # height = self.feature(height, features, 'Height')
        hweight = data.copy()
        hweight = self.feature(hweight, features, 'Weight')
        hweight = self.feature(hweight, features, 'Height')
        # height.hist(column='Height')
        # weight = data.copy()
        # weight = self.feature(weight, features, 'Weight')
        hweight.hist(column=['Weight', 'Height'])
        # year = data.copy()
        # year = self.feature(year, features, 'Year')
        # year.hist(column='Year')
        plt.show()

    def density(self, data, features='drop'):
        plt.close('all')
        # age = data.copy()
        # age = self.feature(age, features, 'Age')
        # sns.distplot(age['Age'], hist=False, label='Age')
        weight = data.copy()
        weight = self.feature(weight, features, 'Weight')
        sns.distplot(weight['Weight'], hist=False, label='Weight')
        height = data.copy()
        height = self.feature(height, features, 'Height')
        sns.distplot(height['Height'], hist=False, label='Height')
        # year = data.copy()
        # year = self.feature(year, features, 'Year')
        # sns.distplot(year['Year'], hist=False, label='Year')
        plt.show()

    def pair_plot(self, data, features='drop'):
        plt.close('all')
        hweight = data.copy()
        hweight = self.feature(hweight, features, 'Weight')
        hweight = self.feature(hweight, features, 'Height')
        sns.pairplot(hweight, vars=['Weight', 'Height'])
        plt.show()

    def box_plot(self, data, features='drop'):
        plt.close('all')
        hweight = data.copy()
        hweight = self.feature(hweight, features, 'Weight')
        hweight = self.feature(hweight, features, 'Height')
        hweight.boxplot(column=['Weight', 'Height'])
        # height = data.copy()
        # height.boxplot(column='Height')
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    mpl = MyPlotLib()
    mpl.histogram(data)
    mpl.density(data)
    mpl.pair_plot(data)
    mpl.box_plot(data)
    pass

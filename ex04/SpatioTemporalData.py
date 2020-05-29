from FileLoader import FileLoader
import sys
import pandas


class SpatioTemporalData():
    def __init__(self, df):
        self.df = df

    def when(self, location):
        when = []
        years = self.df[self.df['City'] == location]
        years = years.drop_duplicates(subset='Year')
        for index, row in years.iterrows():
            when.append(int(row['Year']))
        print(when)
        pass

    def where(self, date):
        where = []
        city = self.df[self.df['Year'] == date]
        city = city.drop_duplicates(subset='City')
        for index, row in city.iterrows():
            where.append(str(row['City']))
        print(where)
        pass


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    sp = SpatioTemporalData(data)
    sp.where(1896)
    sp.when('Athina')
    sp.when('Paris')
    pass

import sys
from FileLoader import FileLoader
import pandas


def youngestFellah(data_frame, year):
    # male = data_frame.query('Sex == M' and 'Year ==@ year')
    male = data_frame[(data_frame['Sex'] == 'M') &
                      (data_frame['Year'] == year)]
    male = male.nsmallest(1, 'Age')
    female = data_frame[(data_frame['Sex'] == 'F') &
                        (data_frame['Year'] == year)]
    # female = data_frame.query('Sex == F' and 'Year ==@ year')
    female = female.nsmallest(1, 'Age')
    youngest = {'Female': float(female['Age']), 'Male': float(male['Age'])}
    print(youngest)


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    youngestFellah(data, 2004)
    pass

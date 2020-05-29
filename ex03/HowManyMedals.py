from FileLoader import FileLoader
import sys
import pandas


def howManyMedals(df, name):
    participant = df[df['Name'] == name]
    medals = {}
    years = participant.drop_duplicates(subset='Year')
    for index, row in years.iterrows():
        medals[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
    for index, row in participant.iterrows():
        if row['Medal'] == 'Gold':
            medals[row['Year']]['G'] += 1
        if row['Medal'] == 'Silver':
            medals[row['Year']]['S'] += 1
        if row['Medal'] == 'Bronze':
            medals[row['Year']]['B'] += 1
    print(medals)


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    howManyMedals(data, 'Kjetil Andr Aamodt')
    pass

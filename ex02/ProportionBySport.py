from FileLoader import FileLoader
import sys
import pandas


def proportionBySport(df, year, sport, gender):
    participants = df[(df['Sex'] == gender) & (df['Year'] == year)]
    participants = participants.drop_duplicates(subset='Name')
    totnumber = len(participants)
    # print(totnumber)
    sport = participants[participants['Sport'] == sport]
    number = len(sport)
    percent = number/totnumber
    print(str(percent))


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    proportionBySport(data, 2004, 'Tennis', 'F')
    pass

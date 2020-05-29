import sys
import pandas


class FileLoader:
    def load(self, path):
        data_frame = pandas.read_csv(path)
        dim = data_frame.shape
        print("Dataset dimensions :", str(dim[0]), "x", str(dim[1]))
        return data_frame

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        if n < 0:
            print(df.tail(-n))


if __name__ == "__main__":
    loader = FileLoader()
    data_frame = loader.load("../resources/athlete_events.csv")
    loader.display(data_frame, -5)

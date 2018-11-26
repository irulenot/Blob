import Constants
import pandas as pd

def getTrainingDataframe():
    data = pd.read_csv(Constants.PLAY_DATA_PATH, sep="\n", header=None)
    parsed_data = data[data[:].str.contains("KeyDown")]
    print(parsed_data)

getTrainingDataframe()
import Constants
import pandas as pd

def getTrainingDataframe():
    data = pd.read_csv(Constants.PLAY_DATA_PATH, sep="\n", header=None)
    jump_data = data[data[0].str.contains("KeyDown")]
    print(data[0][jump_data.index-1])

getTrainingDataframe()
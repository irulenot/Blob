import pandas as pd

import Constants

# Read in data from play data history then
def getTrainingDataframe():
    data = pd.read_csv(Constants.PLAY_DATA_PATH, sep="\n", header=None)

    valid_dataframe = getValidDataframe(data)

    return getFeatureDataframe(valid_dataframe)



# Returns dataframe vector with pillar properties and location when player jumped
def getValidDataframe(data):
    # Parse out all jump data and data 2 places before it (pillars hopefully)
    jump_dataframe = data[data[0].str.contains("KeyDown")]
    pillar_series = data[0][jump_dataframe.index - 2]

    # Check pillar data and prune out invalid data
    valid_pillar_series = pillar_series[pillar_series.str.contains("<Surface")]
    return valid_pillar_series.reset_index()


# Returns dataframe with training ready features
def getFeatureDataframe(valid_dataframe):
    # Getting rid of formatting
    valid_dataframe[0].replace(regex=True, inplace=True, \
                               to_replace=r'<Surface[(]|SW[)]>,<rect[(]|[)]>', value=r'')


    # TODO: Currently trying to split column into 10 columns
    training_dataframe = pd.DataFrame(valid_dataframe[0].str.row.str.split('x , ', 10).tolist(), \
                                      columns=['surface_x','surface_y','surface_z', \
                                               'position_x','position_y','position_z', \
                                               'data_a', 'data_b', 'data_c', 'speed_x'])
    print(training_dataframe)


    return None


# TESTING

getTrainingDataframe()
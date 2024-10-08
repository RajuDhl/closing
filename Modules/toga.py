import pandas as pd


def toga(toga_file):
    dataframe = pd.read_excel(toga_file, header=None)
    # delete all other columns except column1
    df = dataframe[[0]]

    # reshape such that every 3 row is made a column
    df = df.values.reshape(-1, 3)

    # back as df
    df = pd.DataFrame(df)

    # replace rm for room numbering
    df[0] = df[0].str.replace("RM ", "", regex=False)

    # make room numbers int
    df[0] = df[0].astype(int)

    # sort df
    df = df.sort_values(by=0, ascending=True)

    dict = {}
    for index, row in df.iterrows():
        if row[1] == 'Departure Clean':
            dict[row[0]] = 'dep'
        elif row[1] == 'Occupied Clean':
            dict[row[0]] = 'occ'
        elif row[1] == 'Weekly Clean':
            dict[row[0]] = 'wc'
        else:
            dict[row[0]] = 'vacant'

    return dict

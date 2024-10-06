import pandas as pd

# starting of each section in 1c
start = ['101', '220', '219']

file = 'rc.xlsx'


def room_count(rc_file):
    dataframe = pd.read_excel(rc_file)
    df = dataframe.astype(str)
    pos = []
    # find start and end of each section and save to pos array
    for each in start:
        result = (df == each)
        pos.append(result.stack().idxmax())

    # start and end of file
    rc_start = pos[0][0]
    rc_end = pos[2][0]

    # number of columns in each section
    delimeter = int(pos[1][1].split(" ")[1])

    # total number of column in file
    no_of_columns = df.shape[1]

    # trim dataframe to only include start to finish of room count section
    rc_df = df.iloc[rc_start - 1:rc_end + 1]
    row_dict = {}
    column_start = 0

    # loop through all columns
    while column_start < no_of_columns:
        next_attr = column_start + delimeter  # next section
        extract = rc_df.iloc[:, column_start:next_attr]
        extract = extract.reset_index(drop=True)
        extract.columns = extract.iloc[0]
        extract = extract[1:]
        extract.columns = ['Room'] + list(extract.columns[1:])

        for _, row in extract.iterrows():
            # row_dict = {}
            if any(row[col] != 'nan' and int(row[col]) >= 1 for col in ['Dep', 'Occupied C', 'WC']):
                dep = row['Dep']
                occ = row['Occupied C']
                wc = row['WC']
                if dep in ['1', '2']:
                    row_dict[int(float(row['Room']))] = 'dep'
                if occ in ['1', '2']:
                    row_dict[int(float(row['Room']))] = 'occ'
                if wc in ['1', '2']:
                    row_dict[int(float(row['Room']))] = 'wc'
            elif row['Room'] != 'nan':
                row_dict[int(float(row['Room']))] = 'vacant'

            # dont save empty lines
        column_start += delimeter
    return row_dict

#state abbreviation to full name

import pandas as pd

def add_state_names(my_df):
    new_df = my_df.copy()
    names_map = {'CA':'Cali', 'CO':'Colo','CT':'Conn'}
    new_df['name'] = new_df['abbrev'].map(names_map)
    return new_df



if __name__ == '__main__':
    df = pd.DataFrame({'abbrev':['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2)
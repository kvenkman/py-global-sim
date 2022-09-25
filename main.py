import pandas as pd
from pathlib import Path
import re

populations_file = Path('data/wtf.csv')
male_populations_file = Path('data/global_make_populations.csv')

def initialize():
    """
    Initialize the model
    """
    df = pd.read_csv(populations_file, header=4)

    def fix_names(input_name):
        input_name = re.sub(', The', '', input_name)
        input_name = re.sub('[^a-zA-Z]', '-', input_name)
        input_name = re.sub('--', '-', input_name)
        input_name = re.sub('-$', '', input_name)
        return input_name
    
    df['Country Name'] = df['Country Name'].apply(fix_names)
    print(df.iloc[105])



def main():
    pass

if __name__ == '__main__':
    initialize()

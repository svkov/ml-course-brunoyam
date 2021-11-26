import sys
import pandas as pd

if __name__ == '__main__':
    input_filename = sys.argv[0]
    output_filename = sys.argv[1]
    df = pd.read_excel(input_filename, engine='openpyxl')
    author = df.user[1]
    first_tweet = df.tweet[1]
    with open(output_filename, mode='w') as file:
        file.write(f'{author}\t{first_tweet}')
    
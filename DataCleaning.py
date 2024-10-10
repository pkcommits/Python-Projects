import numpy as np
import pandas as pd


input_path = input("Enter file path: ")
chunk_size = int(input("Enter chunk size: "))
output_path = 'D:\datascience\output\output_file.csv'

def format_path(input_path):
    input_path = input_path.strip() 
    raw_path = input_path.replace("\\", "\\\\")
    print(f'filepath is: {raw_path}')

    return raw_path

formatted_path = format_path(input_path)

def convert_duration(duration):
    if isinstance(duration, str):  # Check if duration is a string
        if 'season' in duration:
            seasons = int(duration.split()[0])
            run_time_s = seasons * 50
            return run_time_s
        elif 'min' in duration:
            run_time_m = int(duration.split()[0])
            return run_time_m
    return None  # Return None for other cases


def clean(chunk):
    df = chunk.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Replace "Not Given" with NaN and drop NaN values
    df.replace("Not Given", np.nan, inplace=True)
    df.dropna(inplace=True)

    #Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)

    # Remove white spaces from all columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    #Convert data types
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['release_year'] = df['release_year'].astype(int)
    df['duration'] = df['duration'].astype(str)
    df['duration'] = df['duration'].apply(convert_duration) 
    return df
    
    
def data_split(formatted_path, chunk_size):
    data = pd.read_csv(formatted_path)
    info = data.info()
    print(f"Dataset Information \n {info}")
    chunks = pd.read_csv(formatted_path, chunksize= chunk_size)
    cleaned_list = []

    for index, chunk in enumerate(chunks, start= 1):
        print(f"Cleaning chunk {index}")
        cleaned_chunk = clean(chunk)
        cleaned_list.append(cleaned_chunk)
        print(f"Chunk {index} has been cleaned")
         
    
    cleaned_combine = pd.concat(cleaned_list, ignore_index=True)
    print(f"Cleaning completed")

    return cleaned_combine    

#Call the data split function
Cleaned_data = data_split(formatted_path, chunk_size)
Cleaned_data.to_csv(output_path, index=False)

print(f"CSV file saved at: {output_path}")





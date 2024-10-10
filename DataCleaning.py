import pandas as pd

input_path = input("Enter file path: ")
chunk_size = input("Enter chunk size: ")

def format_path(input_path):
    input_path = input_path.strip() 
    raw_path = input_path.replace("\\", "\\\\")
    print(f'filepath is: {raw_path}')

    return raw_path

formatted_path = format_path(input_path)



def clean():
    print



def data_split(formatted_path, chunk_size):
    chunks = pd.read_csv(formatted_path, chunksize= chunk_size)
    cleaned_list = []

    for chunk in chunks:
        cleaned_chunk = clean(chunks)
        cleaned_list.append(cleaned_chunk)
    
    cleaned_data = pd.concat(cleaned_list)
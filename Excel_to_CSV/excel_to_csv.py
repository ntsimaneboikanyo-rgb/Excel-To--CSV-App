import pandas as pd
from ImportFile.import_file import import_file

# df_excel = pd.DataFrame(pd.read_excel("DAISIES 2K26.xlsx"))

# turn this into a function 
def excel_to_csv():
    #print("File type: ", type(import_file))
    read_file = pd.read_excel(import_file())

    read_file.to_csv("convertedFile.csv",index=None,header=True)

    df_csv = pd.read_csv("convertedFile.csv")

    print(df_csv)
    return df_csv



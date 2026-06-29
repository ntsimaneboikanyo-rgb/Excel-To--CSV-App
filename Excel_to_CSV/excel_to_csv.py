import pandas as pd
from ImportFile.import_file import import_file

# df_excel = pd.DataFrame(pd.read_excel("DAISIES 2K26.xlsx"))

# Function converts excel file to csv and returns csv file 
def excel_to_csv(filename):
    #print("File type: ", type(import_file))
    
    read_file = pd.read_excel(filename)

    read_file.to_csv(filename+".csv",index=None,header=True)

    df_csv = pd.read_csv(filename+".csv")

    print(df_csv)
    return df_csv




# 
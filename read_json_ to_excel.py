import pandas as pd
patients_df = pd.read_json('list.json')
patients_df.head()
patients_df.to_excel('qr.xlsx')
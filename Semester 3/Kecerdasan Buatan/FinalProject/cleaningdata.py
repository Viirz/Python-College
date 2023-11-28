import pandas as pd
import demoji

class CleaningData:
    
    def __init__(self):
        
        # membaca data dari file csv
        self.ayamdata = pd.read_csv('data\dataset-ayam.csv')
        self.kambingdata = pd.read_csv('data\dataset-kambing.csv')
        self.sapidata = pd.read_csv('data\dataset-sapi.csv')
        self.ikandata = pd.read_csv('data\dataset-ikan.csv')
        self.udangdata = pd.read_csv('data\dataset-udang.csv')

        self.clean_data()

    def clean_data(self):
        
        # menghapus kolom yang null
        self.ayamdata = self.ayamdata.dropna()
        self.kambingdata = self.kambingdata.dropna()
        self.sapidata = self.sapidata.dropna()
        self.ikandata = self.ikandata.dropna()
        self.udangdata = self.udangdata.dropna()

        #menghapus kolom duplikat
        self.ayamdata = self.ayamdata.drop_duplicates()
        self.kambingdata = self.kambingdata.drop_duplicates()
        self.sapidata = self.sapidata.drop_duplicates()
        self.ikandata = self.ikandata.drop_duplicates()
        self.udangdata = self.udangdata.drop_duplicates()

        # reset index agar tidak ada index yang hilang
        self.ayamdata = self.ayamdata.reset_index(drop=True)
        self.kambingdata = self.kambingdata.reset_index(drop=True)
        self.sapidata = self.sapidata.reset_index(drop=True)
        self.ikandata = self.ikandata.reset_index(drop=True)
        self.udangdata = self.udangdata.reset_index(drop=True)

        # Mengubah Dtype Title dan Ingeredients menjadi String dan huruf kecil
        self.ayamdata['Title'] = self.ayamdata['Title'].astype('str')
        self.ayamdata['Title'] = self.ayamdata['Title'].str.lower()
        self.ayamdata['Ingredients'] = self.ayamdata['Ingredients'].astype('str')
        self.ayamdata['Ingredients'] = self.ayamdata['Ingredients'].str.lower()

        self.kambingdata['Title'] = self.kambingdata['Title'].astype('str')
        self.kambingdata['Title'] = self.kambingdata['Title'].str.lower()
        self.kambingdata['Ingredients'] = self.kambingdata['Ingredients'].astype('str')
        self.kambingdata['Ingredients'] = self.kambingdata['Ingredients'].str.lower()

        self.sapidata['Title'] = self.sapidata['Title'].astype('str')
        self.sapidata['Title'] = self.sapidata['Title'].str.lower()
        self.sapidata['Ingredients'] = self.sapidata['Ingredients'].astype('str')
        self.sapidata['Ingredients'] = self.sapidata['Ingredients'].str.lower()

        self.ikandata['Title'] = self.ikandata['Title'].astype('str')
        self.ikandata['Title'] = self.ikandata['Title'].str.lower()
        self.ikandata['Ingredients'] = self.ikandata['Ingredients'].astype('str')
        self.ikandata['Ingredients'] = self.ikandata['Ingredients'].str.lower()

        self.udangdata['Title'] = self.udangdata['Title'].astype('str')
        self.udangdata['Title'] = self.udangdata['Title'].str.lower()
        self.udangdata['Ingredients'] = self.udangdata['Ingredients'].astype('str')
        self.udangdata['Ingredients'] = self.udangdata['Ingredients'].str.lower()

        # Remove emojis from the 'Title' and 'Ingredients' columns
        self.ayamdata['Title'] = self.ayamdata['Title'].apply(lambda x: demoji.replace(x, ""))
        self.ayamdata['Ingredients'] = self.ayamdata['Ingredients'].apply(lambda x: demoji.replace(x, ""))

        self.kambingdata['Title'] = self.kambingdata['Title'].apply(lambda x: demoji.replace(x, ""))
        self.kambingdata['Ingredients'] = self.kambingdata['Ingredients'].apply(lambda x: demoji.replace(x, ""))

        self.sapidata['Title'] = self.sapidata['Title'].apply(lambda x: demoji.replace(x, ""))
        self.sapidata['Ingredients'] = self.sapidata['Ingredients'].apply(lambda x: demoji.replace(x, ""))

        self.ikandata['Title'] = self.ikandata['Title'].apply(lambda x: demoji.replace(x, ""))
        self.ikandata['Ingredients'] = self.ikandata['Ingredients'].apply(lambda x: demoji.replace(x, ""))

        self.udangdata['Title'] = self.udangdata['Title'].apply(lambda x: demoji.replace(x, ""))
        self.udangdata['Ingredients'] = self.udangdata['Ingredients'].apply(lambda x: demoji.replace(x, ""))

    def ayam(self):
        return self.ayamdata
    
    def ayam_backup(self):
        return pd.DataFrame(columns=self.ayamdata.columns)

    def kambing(self):
        return self.kambingdata
    
    def kambing_backup(self):
        return pd.DataFrame(columns=self.kambingdata.columns)
    
    def sapi(self):
        return self.sapidata
    
    def sapi_backup(self):
        return pd.DataFrame(columns=self.sapidata.columns)
    
    def ikan(self):
        return self.ikandata
    
    def ikan_backup(self):
        return pd.DataFrame(columns=self.ikandata.columns)
    
    def udang(self):
        return self.udangdata
    
    def udang_backup(self):
        return pd.DataFrame(columns=self.udangdata.columns)






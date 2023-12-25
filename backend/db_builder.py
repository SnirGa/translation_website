from os import listdir
import pandas as pd
from sqlalchemy import create_engine
class DbBuilder:
    def __init__(self,username,password,port,db,host):
        self.username=username
        self.password=password
        self.port=port
        self.db=db
        self.host=host

    def update_db(self,directory):
        csv_files=self.get_csv_files_from_directory(directory)
        for csv_file in csv_files:
            self.add_table_from_csv_file(f'{directory}/{csv_file}')

    def add_table_from_csv_file(self,csv_file):
        table_name=csv_file.split('.csv')[0]
        table_name=table_name.replace('\\','/')
        if '/' in table_name:
            table_name=table_name.split('/')[-1]
        connection_string=f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}'
        engine = create_engine(connection_string)
        df=pd.read_csv(csv_file)
        df.to_sql(table_name, engine)
        
    def get_csv_files_from_directory(self,directory):
        filenames = listdir(directory)
        return [filename for filename in filenames if filename.endswith('.csv')]

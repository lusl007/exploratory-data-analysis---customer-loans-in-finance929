import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import psycopg2
import pandas as pd


# Load .yaml file containing credentials to access database
def load_dict():
    with open('credentials.yaml', 'r') as file:
        cred_dict = yaml.safe_load(file)
    return cred_dict


class RDSDatabaseConnector:
    def __init__(self, cred_dict):
        self.cred_dict = load_dict(cred_dict)
        
    def SQL_engine(self):    
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.HOST = self.cred_dict["RDS_HOST"]
        self.PASSWORD = self.cred_dict["RDS_PASSWORD"]
        self.USER = self.cred_dict["RDS_USER"]
        self.DATABASE = self.cred_dict["RDS_DATABASE"]
        self.PORT = self.cred_dict["RDS_PORT"]

        #create an engine containing information about the database and its type
        self.engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}")
        self.engine.execution_options(isolation_level='AUTOCOMMIT').connect()

    # extract data from the RDS as a Pandas dataframe
    def extract_data_df(self):
         with self.engine.connect() as connection:
            self.df = pd.read_sql_table('loan_payments', self.engine)
            return self.df

    # save the data as a .csv file format
    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)


# below methods are run if the script is directly executed
if __name__ == '__main__':
    credentials = load_dict()
    rds_connect = RDSDatabaseConnector(credentials)
    rds_connect.connect()
    rds_connect.SQL_engine()
    df_extraction = rds_connect.extract_data_df()
    rds_connect.save_to_csv()

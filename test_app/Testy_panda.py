
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())
# fifa=pd.read_csv('D:\STUDIA\Inżynierka\Dash_App\csv_memory\Part_Maxymos_1_MP-001_2017-02-22_16-05-27_Sila_bl_trans150obr_000001_OK.csv')
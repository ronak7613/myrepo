import pandas as pd
from django.contrib.staticfiles import finders
from myapp.models import table_TapTyag


# Load the Excel file into a DataFrame
path = finders.find('taptyag_test.xlsx')
df = pd.read_excel(path)

# Iterate over the DataFrame and save each row to the database
for index, row in df.iterrows():
    data_instance = table_TapTyag(
        sr=row['sr'],  
        Id=row['ID'] ,
        Time=pd.to_datetime(row['Time']),
        off_Time=pd.to_datetime(row['off Time']),
        Activity=row['Activity'],
        पहला_नाम_First_Name=row['पहला नाम / First Name'],
        पिता_पति_का_नाम_Husband_Father_Name=row['पिता / पति का नाम /  Husband / Father Name'],
        सरनेम_Surname=row['सरनेम / Surname'],
        लिंग_Gender=row['लिंग / Gender'],
        उम्र_Age=row['उम्र / Age'],
        देश_Country=row['देश - Country'],
        मोबाइल_नंबर_भारत_India_Whatsapp_No=row['मोबाइल नंबर_भारत _India _Whatsapp No'],
        Pincode=row['Pincode'],
        मोबाइल_नंबर_विदेश_Foreign_WhatsappNo=row['मोबाइल नंबर_विदेश _ Foreign _WhatsappNo'],
        Pincode_FR=row['Pincode_FR'],
        Sub_Region=row['Sub Region'],
        State_राज्य=row['State / राज्य'],
        Region=row['Region'],
        A1=row['A1'],
        इनमे_से_किस_लड़ी_में_भाग_लेंगे=row['इनमे से किस लड़ी में भाग लेंगे'],
        A2=row['A2'],
        आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_प्रतिदिन_1_घंटा_मौन_आराधना_करेंगे=row['आप महत्तम महोत्सव में फरवरी 2025 तक  प्रतिदिन 1 घंटा मौन आराधना करेंगे'],
        आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_प्रतिमाह_4_रात्रि_चौविहार_प्रत्याख्यान_सूर्यास्त_से_अगले_दिन_तक_नवकारसी_पक्की_नवकारसी_कर_जीवो_को_अभय_दान_देंगे=row['आप महत्तम महोत्सव में फरवरी 2025 तक  प्रतिमाह 4 रात्रि चौविहार प्रत्याख्यान_सूर्यास्त से अगले दिन तक नवकारसी_पक्की नवकारसी कर जीवो को अभय दान देंगे'],
        आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_50_दिन_पूर्ण_सूर्य_अस्त_से_सूर्य_उदय_संवर_पौषध_पूर्ण_दया_करेंगे=row['आप महत्तम महोत्सव में फरवरी 2025 तक 50 दिन पूर्ण सूर्य अस्त से सूर्य उदय संवर/पौषध/ पूर्ण दया करेंगे'],
        आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_दूध_दही_घी_तेल_मीठा_में_से_किसी_भी_एक_विगय_का_प्रतिदिन_त्याग_करेंगे=row['आप महत्तम महोत्सव में फरवरी 2025 तक दूध_दही_घी_तेल_मीठा  में से किसी भी एक विगय का प्रतिदिन त्याग करेंगे'],
        स्कोर=row['स्कोर'],  # Note: Make sure the column names match your DataFrame
    )
    
    data_instance.save()
# #code to delete all rows
# from your_app.models import Data

#  # Delete all entries
# Data.objects.all().delete()

#---------------------pygsheet to sqllite-------------------

import pygsheets
path='G:/ronak_project_freelance/sanyam_jain_bhilwara/ronak/backend/myapp/static/credential/hybrid-flame-400820-b702938eebb4.json'
gc = pygsheets.authorize(service_account_file=path)
sh=gc.open('testing_bhilwara')
wk1=sh[1]
df = wk1.get_as_df(index_column=0,include_tailing_empty=False)
print(df) 

# inserting dataframe to SQLite table:  Part 2 
import pandas as pd 
from sqlalchemy import create_engine
#my_path='G:\\My Drive\\testing\\my_db\\my_db.db'
my_path='backend\db.sqlite3'
my_conn = create_engine("sqlite:///"+ my_path)
df.to_sql(con=my_conn,name='testdb',if_exists='append', index=False)


## to check the data use the code below ##
r_set=my_conn.execute('SELECT * from student2');
for row in r_set:
    print(row)

#-----------------------------------------------------------
import sqlite3
import pygsheets
path='G:/ronak_project_freelance/sanyam_jain_bhilwara/ronak/backend/myapp/static/credential/hybrid-flame-400820-b702938eebb4.json'
gc = pygsheets.authorize(service_account_file=path)
sh=gc.open('testing_bhilwara')
wk1=sh[1]
df = wk1.get_as_df(index_column=0,include_tailing_empty=False)
print(df) 



conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Replace special characters ("/") in column names
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.replace('-', '_')

# Create SQLite3 table based on the columns from Google Sheets
#create_table_query = f"CREATE TABLE IF NOT EXISTS test ({', '.join([f'/"{col}/" TEXT' for col in df.columns])})"
create_table_query = f"CREATE TABLE IF NOT EXISTS test ({', '.join([f'{col} TEXT' for col in df.columns])})"
cursor.execute(create_table_query)

# Insert data into the SQLite3 table
for _, row in df.iterrows():
    placeholders = ', '.join(['?' for _ in range(len(row))])
    cursor.execute(f'INSERT INTO test VALUES ({placeholders})', tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()
#------------for sheet 2 gyanargan----------------------
import sqlite3
import pygsheets
path='G:/ronak_project_freelance/sanyam_jain_bhilwara/ronak/backend/myapp/static/credential/hybrid-flame-400820-b702938eebb4.json'
gc = pygsheets.authorize(service_account_file=path)
sh=gc.open('testing_bhilwara')
wk1=sh[2]
df = wk1.get_as_df(index_column=0,include_tailing_empty=False)
print(df) 

# SQLite database connection
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Replace special characters and spaces in column names
columns = df.columns.tolist()
columns = [col.replace(' ', '_').replace('-', '_').replace('/', '_').replace('.', '_').replace('?', '').replace('(', '').replace(')', '') for col in columns]
#columns = [col.encode('utf-8') if isinstance(col, str) else col for col in columns]

# Create the CREATE TABLE query
#create_table_query = f"CREATE TABLE IF NOT EXISTS gyan ({', '.join([f'/{col.decode('''utf-8''')}/ TEXT' for col in columns])})"
create_table_query = f"CREATE TABLE IF NOT EXISTS gyan ({', '.join([f'{col} TEXT' for col in columns])})"


# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data into the SQLite3 table
for _, row in df.iterrows():
    placeholders = ', '.join(['?' for _ in range(len(row))])
    cursor.execute(f'INSERT INTO gyan VALUES ({placeholders})', tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data 2 inserted into SQLite database.")


#------------------------------------------------------
#-----------------------for sheet 1 taptyag---------------------------------
import sqlite3
import pygsheets
path='G:/ronak_project_freelance/sanyam_jain_bhilwara/ronak/backend/myapp/static/credential/hybrid-flame-400820-b702938eebb4.json'
gc = pygsheets.authorize(service_account_file=path)
sh=gc.open('testing_bhilwara')
wk1=sh[1]
df = wk1.get_as_df(index_column=0,include_tailing_empty=False)
print(df) 

# SQLite database connection
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Replace special characters and spaces in column names
columns = df.columns.tolist()
columns = [col.replace(' ', '_').replace('-', '_').replace('/', '_').replace('.', '_').replace('?', '') for col in columns]
#columns = [col.encode('utf-8') if isinstance(col, str) else col for col in columns]

# Create the CREATE TABLE query
#create_table_query = f"CREATE TABLE IF NOT EXISTS test ({', '.join([f'/{col.decode('''utf-8''')}/ TEXT' for col in columns])})"
create_table_query = f"CREATE TABLE IF NOT EXISTS test ({', '.join([f'{col} TEXT' for col in columns])})"


# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data into the SQLite3 table
for _, row in df.iterrows():
    placeholders = ', '.join(['?' for _ in range(len(row))])
    cursor.execute(f'INSERT INTO test VALUES ({placeholders})', tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into SQLite database.")

#--------------------------------------------------------
#----------------------not-------------------------------------
import sqlite3
import pygsheets

# Replace special characters and spaces in column names
columns = [
    "sr", "ID", "Time", "offTime", "Activity",
    "पहलानाम_FirstName", "पिता_पतिकानाम_HusbandsFathersName", "सरनेम_Surname",
    "लिंग_Gender", "उम्र_Age", "देश_Country", "मोबाइलनंबर_भारत_India_WhatsappNo",
    "पिनकोड_Pincode", "मोबाइलनंबर_विदेश_Foreign_WhatsappNo", "पिनकोड_Pincode2",
    "SubRegion", "State_राज्य", "Region", "A1", "इनमेसे_किस_लड़ी_में_भाग_लेंगे",
    "A2", "आप_महत्तम_महोत्सव_में_फरवरी2025तक_प्रतिदिन1घंटा_मौन_आराधना_करेंगे",
    "आप_महत्तम_महोत्सव_में_फरवरी2025तक_प्रतिमाह4रात्रि_चौविहार_प्रत्याख्यान",
    "आप_महत्तम_महोत्सव_में_फरवरी2025तक50दिन_पूर्ण_सूर्य_अस्त_से_सूर्य_उदयसंवर_पौषध_पूर्णदया_करेंगे",
    "आप_महत्तम_महोत्सव_में_फरवरी2025तक_दूध_दही_घी_तेल_मीठा_में_से_किसी_भी_एक_विगय_काप्रतिदिनत्याग_करेंगे",
    "स्कोर"
]

# Join columns to create the CREATE TABLE query
create_table_query = f"CREATE TABLE IF NOT EXISTS test ({', '.join([f'{col} TEXT' for col in columns])})"


# Authenticate with Google Sheets API using pygsheets
path = 'path_to_your_credentials.json'  # Update this with your credentials path
gc = pygsheets.authorize(service_file=path)

# Open the Google Sheets spreadsheet
spreadsheet = gc.open('testing_bhilwara')
worksheet = spreadsheet.sheet1  # Assuming you want data from the first worksheet

# Fetch all data from Google Sheets
data = worksheet.get_as_df()

# Connect to SQLite3 database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data into the SQLite3 table
for _, row in data.iterrows():
    placeholders = ', '.join(['?' for _ in range(len(row))])
    cursor.execute(f'INSERT INTO test VALUES ({placeholders})', tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()

#-------------------to know dta type o columns using python-----

# import pandas as pd
# from django.contrib.staticfiles import finders
# # Load the Excel file into a DataFrame
# path = finders.find('MM_TRIAL.xlsx')
# df = pd.read_excel(path)

# # Print the data types of each column
# print("Data types of each column:")
# print(df.dtypes)
#----------------------------------------
#-----------------------------------------------------------
# # #from django.shortcuts import render
# import pandas as pd
# import json
# # #from django.views.decorators.csrf import csrf_protect,csrf_exempt

# # #from .models import usersList,entry
# # #from django.http import JsonResponse
# # #from django.contrib.staticfiles import finders

# data = pd.read_excel('backend\myapp\static\MM_TRIAL.xlsx')

# header = ['Date', 'Activity', 'Region', 'Sub_Region', 'Full_name', 'Age',
#         'Gender', 'Whatsapp_India', 'Pincode', 'Village', 'SUB_ACTIVITY1',
#         'SA2', 'SA3', 'SA4']

# rows = {}

# for c in header:
#     rows[c] = list(data.loc[:][c])


# json_object = json.dumps(rows) 

# print(json_object[1])

# # for r in range(len(rows['Region'])):
# #     for c in list(rows.keys()):
# #         print(rows[c][r])
# # # rows = {'rows':{
# # #                 'id':list(data.iloc[:,0]),
# # #                 'chemblid':list(data.iloc[:,0]), 
# # #                 'prefName':list(data.iloc[:,0])}}

# # # <table class="table">
# # #     <thead>
# # #         <tr>
# # #             {% for k in header %}
# # #             <th>{{k}}</th>
# # #             {% endfor %}
# # #         </tr>
# # #     </thead>
# # #     <tbody>
# # #         {% for r in rows %}
# # #             <tr>
# # #                 {% for e in r %}
# # #                     <td>{{e.id}}</td>
# # #                     <td>{{e.chemblid}}</td>
# # #                     <td>{{e.prefName}}</td>
# # #                 {% endfor %}
# # #             </tr>
# # #         {% endfor %}
# # #     </tbody>
# # # </table> 



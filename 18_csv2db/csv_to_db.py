import csv

def convert(row):
    for i in range(len(row)):
        if row[i].isnumeric():
            row[i]= int(row[i])
    return tuple(row)
def csv_to_db(c, csv_name, table_name, headers):
    c.execute(f"DROP TABLE if exists {table_name};")
    #print(f"CREATE TABLE {table_name} {headers};")
    c.execute(f"CREATE TABLE {table_name} {headers};")
    with open(csv_name, 'r') as f:
        dictreader = csv.reader(f)
        for row in dictreader:
            row = convert(row)
            c.execute(f"INSERT INTO {table_name} VALUES " + str(row) + ";")
    

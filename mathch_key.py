#Match the tables, source and target list of tables and row count stored in
#a dictionary. I need to compare both the dictionaries to find out if tables and data are migrated successfully

sourceRowData = {'table1': 5, 'table2': 10, 'table3': 20, 'table4': 50}
targetRowData = {'table1': 5, 'table2': 10, 'table3': 8}


for key, v in sourceRowData.items():
    if key not in targetRowData:   #Check if table in targetRowData
        print ("Table {} not found in target database {}".format(key, "targetDatabase"))
    else:
        if v != targetRowData[key]:  #Check for count mismatch
            print("Failed: Table Row Count mismatch {}".format(key))
            
            
  #Output:

Failed: Table Row Count mismatch table3
Table table4 not found in target database targetDatabase

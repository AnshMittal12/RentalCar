# All
def ParseDict(records):
    L=[]
    for  R in records:
        d=dict(R)
        L.append(d)
    return(L)

# Single Record ke liye 
def ParseDictSingleRecord(cursor):
    schema = cursor.description
    record = cursor.fetchone()
    rec = {}
    for i in range(len(record)):
        rec[schema[i][0]] = record[i]
    return(rec)

# Multiple Records ke liye 
def ParseDictMultipleRecord(cursor):
    schema = cursor.description
    record = cursor.fetchall()
    print("In Funcction Record:" ,record)
    rec = []
    for row in record:
        R = {}
        for i in range(len(row)):
            R[schema[i][0]] = row[i]
        rec.append(R)
    return(rec)
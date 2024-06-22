import pyodbc 
def Con():
    cnxn_str = 'DRIVER={SQL Server};Server=MAXO3IFY;Database=PruebaCS50;Trusted_Connection=yes'
    cnxn = pyodbc.connect(cnxn_str)
    return cnxn
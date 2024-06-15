import Modulos.connectionstring
from werkzeug.security import check_password_hash
cnxn = Modulos.connectionstring.Con()


def UserRegister(User,Pass,Correo):
    cursor = cnxn.cursor()
    cursor.execute("""  INSERT INTO Usuarios (sUserName,sPassword,sCorreo,sCreadoPor)
                        VALUES(?,?,?,?)""",User,Pass,Correo,User)
    cursor.commit()
    cursor.close()

def UserLogin(User,Pass):
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 sPassword FROM Usuarios WHERE sUserName = ?", User)
    sPass = cursor.fetchone()[0]
    if check_password_hash(sPass,Pass):
        return True
    else:
        return False
    

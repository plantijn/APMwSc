import os

def ACambioClave():
    params  = request.get_json()
    res = results[0]
    #results = [{'label':''}]
    ouser = user()
    opwd = ouser.password("1233")
    
    db = dbConnect()
    
    
# Aqui va lo de usuario, check_password, encrypt, length (de la tarea2)

# No tocar lo del controlador
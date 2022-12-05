# BASE DE DATOS
# Columnas: | Usuario Id | Player Name | Team Name | Age | Average Score | 
basededatos={
    1:["Maira", "Monzon", 23, 58],
    2:["Flavio", "Salas", 22, 60],
    3:["Marcos", "Lugones", 23, 56],
    4:["Gonzalo", "Copes", 24, 53]
        }
# API simulation of READ operation
# Input Payload
'''
    usuario={
            "usuario": id
        }
'''
def leer_usuario(payload):
    id = payload["usuario"]
    if id in basededatos:
        entry=basededatos[id]
        return {"Code":200, 
                "Response":{"Nombre":entry[0],"Apellido":entry[1]},
                "Message":"Correcto!"}
    else:
        return {"Code":404,"Message":"El usuario no existe."}

# API Testing Function
# Testing function

test_usuario={
        "usuario":2
    }

def test_leer_usuario():
    response=leer_usuario(test_usuario)
    assert response.get("Code")==200


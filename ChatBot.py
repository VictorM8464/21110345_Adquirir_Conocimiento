import os
import json

#Carga el conocimiento desde el archivo JSON si existe
def cargar_conocimiento():
    conocimiento = {}
    if os.path.exists("conocimiento.json"):
        with open("conocimiento.json", "r") as archivo:
            conocimiento = json.load(archivo)
    return conocimiento

#Guarda el conocimiento en el archivo JSON
def guardar_conocimiento(conocimiento):
    with open("conocimiento.json", "w") as archivo:
        json.dump(conocimiento, archivo)

#Obtiene la respuesta a una pregunta del conocimiento
#Si la pregunta no está en el conocimiento, devuelve un mensaje predeterminado
def obtener_respuesta(conocimiento, pregunta):
    if pregunta in conocimiento:
        return conocimiento[pregunta]
    else:
        return "Lo siento, no tengo informacion sobre eso."


def main():
    print("Hola! Soy un chatbot. En que puedo ayudarte?")
    conocimiento = cargar_conocimiento()

    while True:
        pregunta = input("Tu: ").strip().lower()

        if pregunta == "salir":
            guardar_conocimiento(conocimiento)
            print("Hasta luego!")
            break

        respuesta = obtener_respuesta(conocimiento, pregunta)
        print("Chatbot:", respuesta)

        if respuesta == "Lo siento, no tengo informacion sobre eso.":
            nueva_informacion = input("Chatbot: Cual seria la respuesta adecuada a esa pregunta? ").strip()
            conocimiento[pregunta] = nueva_informacion
            print("Chatbot: Gracias por tu respuesta.")
            guardar_conocimiento(conocimiento)

if __name__ == "__main__":
    main()

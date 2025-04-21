import json

# Lista ordenada por número
animales = [
    (1, "animales/1.png", "Murciélago", "Pasivo", "Realmente no se puede interactuar con ellos y solo sirven para propósitos de inmersión. Es posible matar murciélagos golpeándolos con el arma que elijas, pero no dejan caer nada."),
    (2, "animales/2.png", "Aves", "Pasivo", "Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest . Proporcionan plumas , que son cruciales para fabricar flechas , y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales ."),
    (3, "animales/3.png", "Ciervo", "Pasivo", "Los ciervos se pueden encontrar en las zonas boscosas, aunque también en campos abiertos, como las Tierras Fértiles . Cuando los matan, pueden ser desollados por una piel de ciervo , luego sacrificados por cuatro carnes y finalmente dejar caer una cabeza de ciervo ."),
    (4, "animales/4.png", "Peces", "Pasivo", "Los peces son un grupo de animales pasivos que se pueden encontrar en el océano , río , estanques o en el agua de cuevas . Cuando se matan, los peces caen como un artículo de colección, el pescado crudo , que luego se puede cocinar o colgar en una rejilla de secado ."),
    (5, "animales/5.png", "Gansos", "Pasivo", "El ganso es un animal volador y emplumado que se encuentra cerca de los lagos. Es el único pájaro que se posa en el agua, y el mismo nombre del lago de los gansos , al suroeste de Sinkhole ."),
    (6, "animales/6.png", "Lagarto", "Pasivo", "Las lagartijas se pueden encontrar en casi toda la superficie de la península , excepto en las costas y las regiones nevadas profundas. Cuando muere, el jugador puede obtener una piel de lagarto y un lagarto crudo , así como una cabeza de lagarto."),
    (7, "animales/8.png", "Conejo", "Pasivo", "El conejo se puede recolectar para obtener una piel de conejo , una carne de conejo cruda y una cabeza de conejo . La carne cosechada se puede cocinar al fuego o secar en una rejilla de secado y comer."),
    (8, "animales/9.png", "Mapache", "Pasivo", "Los mapaches son algunos de los animales más raros del juego. Cuando los matan y los despellejan, dejan caer 2 carnes , 1 piel de mapache y 1 cabeza de mapache . A diferencia de la mayoría de los animales pequeños en The Forest , los mapaches solo se pueden matar con dos golpes de cualquier arma."),
    (9, "animales/10.png", "Gaviota", "Pasivo", "Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest . Proporcionan plumas , que son cruciales para fabricar flechas , y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales."),
    (10, "animales/11.png", "Ardilla", "Pasivo", "Las ardillas le dan al jugador una carne pequeña y una cabeza de ardilla . Al igual que con la mayoría de los animales pequeños, las ardillas se pueden matar con un solo golpe de cualquier arma en el juego."),
    (11, "animales/12.png", "Tortuga de tierra", "Pasivo", "Las tortugas son animales pasivos que desovan en áreas específicas alrededor del agua, especialmente en las tierras pantanosas. Se mueven muy lentamente y se esconderán dentro de su caparazón si intentas atacarlos. Al igual que las tortugas , la tortuga dejará caer un caparazón de tortuga y dos piezas de carne después de la muerte."),
    (12, "animales/13.png", "Tortuga de mar", "Pasivo", "Dejan caer un caparazón de tortuga , que se puede usar para fabricar el colector de agua , o como un trineo a partir de la v0.67, y dos carnes , que se pueden cocinar o secar y comer."),
    (13, "animales/Boar.webp", "Jabalí", "Agresivo", "Similar al cocodrilo , el jabalí es un animal agresivo capaz de atacar y dañar al jugador. Si el jugador permanece cerca de un jabalí durante demasiado tiempo, emitirá un chillido y comenzará a cargar hacia el jugador. Si el jabalí golpea al jugador con su carga, inflige 15 puntos de daño al jugador sin armadura, al morir suelta 2 de carne y piel."),
    (14, "animales/Shark.webp", "Tiburón", "Agresivo", "Los cocodrilos se pueden encontrar esparcidos por la parte norte del río que atraviesa la península , aunque casi nunca se encuentran en el agua . Dejan caer 4 pieles de lagarto y 4 carnes si se matan, junto con su cabeza que se puede usar como decoración."),
    (15, "animales/Crocodile.webp", "Cocodrilo", "Agresivo", "Los tiburones son animales hostiles que se pueden encontrar nadando en áreas particulares del océano donde el agua es demasiado profunda para pararse. Si el jugador se acerca demasiado, un tiburón cargará hacia él y lo atacará mordiéndolo, al morir solo sueltan 1 de carne y la cabeza.")
]

# Ordenar por número por si no estuvieran ordenados
animales.sort(key=lambda x: x[0])

json_data = [
    {
        "model": "wiki.animal",
        "fields": {
            "numero": numero,
            "imagen": imagen,
            "nombre": nombre,
            "hostilidad": hostilidad,
            "descripcion": descripcion
        }
    }
    for numero, imagen, nombre, hostilidad, descripcion in animales
]

json_path = "animales.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"✅ Archivo JSON 'animales.json' creado correctamente y en orden.")
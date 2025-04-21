import json

armas = [
    (1, "armas/PlaneAxe.webp", "Hacha de avión", "Melee", "Es el primer arma que encuentras en el juego. Sirve para talar árboles, cazar y combatir."),
    (2, "armas/CraftedAxe.webp", "Hacha artesanal", "Melee", "Arma lenta pero con buen daño. Muy fácil de fabricar."),
    (3, "armas/RustyAxe.webp", "Hacha oxidada", "Melee", "Arma lenta pero con alto poder de derribo y bloqueo."),
    (4, "armas/ModernAxe.webp", "Hacha moderna", "Melee", "La mejor hacha para cortar árboles. Daño alto y eficaz para derribar enemigos."),
    (5, "armas/ClimbingAxe.webp", "Pico de escalada", "Melee", "Se usa para escalar acantilados. Causa poco daño pero es rápida."),
    (6, "armas/Machete.webp", "Machete", "Melee", "Corta arbustos fácilmente. Daño medio y corto alcance."),
    (7, "armas/Katana.webp", "Katana", "Melee", "Muy rápida, permite golpear sin parar pero con daño limitado."),
    (8, "armas/WeakSpear.webp", "Lanza débil", "Melee/Distancia", "Útil para cazar. Se lanza pero tiene daño intermedio."),
    (9, "armas/UpgradedSpear.webp", "Lanza mejorada", "Melee/Distancia", "Arma veloz, se puede lanzar, alto daño y versátil."),
    (10, "armas/Chainsaw.webp", "Motosierra", "Melee", "Herramienta potente. No requiere energía. Corta árboles y enemigos con gran velocidad."),
    (11, "armas/CraftedBow.webp", "Arco artesanal", "Distancia", "Lanza flechas. Sin mira, pero muy efectivo con práctica."),
    (12, "armas/TurtleShell.webp", "Caparazón de tortuga", "Melee", "Bloquea daño casi completamente. Poco daño y lento."),
    (13, "armas/Club.webp", "Mazo", "Melee", "Lento pero con gran daño. Excelente para bloquear."),
    (14, "armas/Dynamite.webp", "Dinamita", "Distancia", "Explosivo poderoso. Eficaz contra enemigos y árboles."),
    (15, "armas/Molotov.webp", "Molotov", "Distancia", "Explota e incendia al impactar. Útil para control de áreas.")
]

# Ordenar las armas por número
armas.sort(key=lambda x: x[0])

json_data = [
    {
        "model": "wiki.arma",
        "fields": {
            "numero": numero,
            "imagen": imagen,
            "nombre": nombre,
            "tipo": tipo,
            "descripcion": descripcion
        }
    }
    for numero, imagen, nombre, tipo, descripcion in armas
]

json_path = "armas.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"✅ Archivo JSON 'armas.json' creado correctamente y en orden.")
import json

enemigos = [
    ("enemigos/SkinnyCannibals.webp", "Canibales delgados", "Canibal", "Son los más débiles, con poca vida y daño. Solo son peligrosos en grupo."),
    ("enemigos/RegularCannibals.webp", "Canibales normales", "Canibal", "Aparecen en grupos liderados. Vida y daño intermedios."),
    ("enemigos/PaleCannibal.webp", "Canibales pálidos", "Canibal", "Tienen el doble de vida y daño que los delgados."),
    ("enemigos/PaleSkinnyCannibal.webp", "Canibales pálidos y delgados", "Canibal", "Versión débil y pálida. Muy fácil de derrotar."),
    ("enemigos/PaintedCannibals.webp", "Canibales pintados", "Canibal", "Los más fuertes del juego. Alta vida y daño."),
    ("enemigos/Firemen.webp", "Canibales de fuego", "Canibal", "Usan antorchas. Aplica quemadura."),
    ("enemigos/MaskedCannibal.webp", "Canibales enmascarados", "Canibal", "Altos, con máscaras. Daño medio-alto."),
    ("enemigos/MaskedSkinnyCannibal.webp", "Canibales enmascarados y delgados", "Canibal", "Más débiles que los enmascarados."),
    ("enemigos/DynamiteCannibal.webp", "Canibales dinamita", "Canibal", "Explotan durante la batalla. Peligrosos."),
    ("enemigos/Armsy.webp", "Armsy", "Mutante", "Mutante con múltiples brazos. Daño acumulativo."),
    ("enemigos/Virginia.webp", "Virginia", "Mutante", "Patas múltiples. Embiste y salta."),
    ("enemigos/Cowman.webp", "Cowman", "Mutante", "Robusto. Ataques por embestida."),
    ("enemigos/BabyMutant.webp", "Bebe mutante", "Mutante", "Pequeños pero atacan en grupo."),
    ("enemigos/GreyArmsy.webp", "Armsy gris", "Mutante", "Variante más fuerte del Armsy."),
    ("enemigos/GreyVirginia.webp", "Virginia gris", "Mutante", "Más vida y daño que Virginia normal."),
    ("enemigos/Worm.webp", "Gusano", "Mutante", "Vida baja. Se combinan y vuelan."),
    ("enemigos/Girl.webp", "Niña", "Mutante", "Variante débil del jefe final."),
    ("enemigos/EndBoss.webp", "Jefe final", "Mutante", "Muchísima vida. Ataques de amplio rango.")
]

json_data = [
    {
        "model": "wiki.enemigo",  # ⚠️ Asegúrate que tu modelo se llama "Enemigo" y tu app "wiki"
        "fields": {
            "imagen": imagen,
            "nombre": nombre,
            "tipo": tipo,
            "descripcion": descripcion
        }
    }
    for imagen, nombre, tipo, descripcion in enemigos
]

with open("enemigos.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("✅ Archivo 'enemigos.json' generado correctamente.")
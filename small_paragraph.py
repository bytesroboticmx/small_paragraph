#Nombre:
#Matricula:
#Grupo:
#Fecha:
import re

# Párrafo original en inglés
parrafo_en = (
    "While remote work was initially embraced as a temporary measure, it has eventually "
    "reshaped corporate culture. Companies that are reluctant to adapt risk losing top talent, "
    "whereas those willing to embrace flexibility are seeing a surge in productivity—proving "
    "that the traditional nine-to-five grind is no longer the only path to success."
)

# Traducción naturalizada al español
parrafo_es = (
    "Aunque en un principio el trabajo remoto se adoptó como una medida temporal, con el tiempo "
    "ha transformado la cultura corporativa. Las empresas que se resisten al cambio corren el "
    "riesgo de perder a sus mejores talentos, mientras que aquellas dispuestas a apostar por la "
    "flexibilidad están registrando un repunte en la productividad, lo que demuestra que el "
    "horario tradicional de oficina ya no es el único camino hacia el éxito."
)

# Glosario palabra por palabra (inglés -> español según el contexto del párrafo)
glosario_contexto = {
    "while": "aunque",
    "remote": "remoto",
    "work": "trabajo",
    "was": "fue / se (auxiliar)",
    "initially": "inicialmente / en un principio",
    "embraced": "adoptado / acogido",
    "as": "como",
    "a": "un / una",
    "temporary": "temporal",
    "measure": "medida",
    "it": "ello (sujeto tácito)",
    "has": "ha",
    "eventually": "con el tiempo / finalmente",
    "reshaped": "transformado / remodelado",
    "corporate": "corporativa",
    "culture": "cultura",
    "companies": "empresas",
    "that": "que",
    "are": "son / están",
    "reluctant": "reacias / que se resisten",
    "to": "a / hacia (preposición)",
    "adapt": "adaptarse",
    "risk": "corren el riesgo de",
    "losing": "perder",
    "top": "mejores",
    "talent": "talento(s)",
    "whereas": "mientras que",
    "those": "aquellas",
    "willing": "dispuestas",
    "embrace": "adoptar / apostar por",
    "flexibility": "flexibilidad",
    "seeing": "viendo / registrando",
    "surge": "repunte / aumento",
    "in": "en",
    "productivity": "productividad",
    "proving": "lo que demuestra / probando",
    "the": "el / la",
    "traditional": "tradicional",
    "nine": "nueve",
    "five": "cinco",
    "grind": "rutina / jornada laboral",
    "is": "es / está",
    "no": "ya no / no",
    "longer": "más tiempo (junto a 'no': ya no)",
    "only": "único",
    "path": "camino",
    "success": "éxito",
}

# Extraer palabras limpias en orden de aparición y sin duplicados
palabras_limpias = re.findall(r"[a-zA-Z]+", parrafo_en.lower())
palabras_unicas = list(dict.fromkeys(palabras_limpias))

# Construir la estructura de datos diccionario dinámicamente a partir del párrafo
diccionario_palabras = {
    palabra: glosario_contexto.get(palabra, "Traducción no encontrada")
    for palabra in palabras_unicas
}

# --- SALIDA POR CONSOLA ---
print("=== PÁRRAFO ORIGINAL (EN) ===")
print(parrafo_en)

print("\n=== TRADUCCIÓN (ES) ===")
print(parrafo_es)

print(f"\n=== DICCIONARIO DE PALABRAS ({len(diccionario_palabras)} palabras únicas) ===")
for palabra_en, traduccion_es in diccionario_palabras.items():
    print(f"'{palabra_en}': '{traduccion_es}'")

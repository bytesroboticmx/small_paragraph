# small_paragraph

Script en Python que toma un párrafo en inglés sobre el trabajo remoto, muestra su
traducción al español y genera un glosario palabra por palabra a partir del texto
original.

## Contenido

- `small_paragraph.py` — programa principal.
- `.gitignore` — exclusiones habituales de Python.

## Requisitos

- Python 3.8 o superior (probado con 3.14).
- Solo usa la librería estándar (`re`), no requiere dependencias externas.

## Uso

```bash
python3 small_paragraph.py
```

Salida esperada:

1. El párrafo original en inglés.
2. La traducción naturalizada al español.
3. Un diccionario con cada palabra única del párrafo (en minúsculas y sin
   duplicados, en orden de aparición) y su traducción según el contexto.

## Cómo funciona

1. `parrafo_en` guarda el texto original y `parrafo_es` su traducción.
2. `glosario_contexto` es un diccionario inglés → español con la traducción
   contextual de cada término.
3. Se extraen las palabras del párrafo con la expresión regular `[a-zA-Z]+`
   sobre el texto en minúsculas.
4. Se eliminan los duplicados conservando el orden con `dict.fromkeys`.
5. Se construye `diccionario_palabras` combinando las palabras encontradas con el
   glosario; si una palabra no está en el glosario se marca como
   `"Traducción no encontrada"`.

## Ejemplo de salida

```text
=== PÁRRAFO ORIGINAL (EN) ===
While remote work was initially embraced as a temporary measure, ...

=== TRADUCCIÓN (ES) ===
Aunque en un principio el trabajo remoto se adoptó como una medida temporal, ...

=== DICCIONARIO DE PALABRAS (47 palabras únicas) ===
'while': 'aunque'
'remote': 'remoto'
...
```

## Personalización

Para trabajar con otro párrafo:

1. Reemplaza `parrafo_en` por el nuevo texto en inglés.
2. Actualiza `parrafo_es` con su traducción.
3. Añade al `glosario_contexto` las palabras nuevas que quieras traducir.

Las palabras que falten en el glosario aparecerán como
`"Traducción no encontrada"`, lo que sirve para detectar términos pendientes.

## Autor

Aldo Gonzalez Vazquez

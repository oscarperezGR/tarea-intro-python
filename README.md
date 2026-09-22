#%%
# Catálogo de Piezas Coleccionables

Programa de consola en Python para registrar piezas coleccionables (nombre, categoría, precio, estado y descripción) dentro de un catálogo con capacidad máxima de 10 piezas.


## 📋 Descripción

El programa parte de un diccionario `catalog` con 10 espacios predefinidos (`piezas1` a `piezas10`), cada uno con la siguiente estructura:

```python
{
    "id": 0,
    "name": "",
    "category": "",
    "price": 0,
    "status": "",
    "description": ""
}
```

El usuario elige cuántas piezas quiere registrar (máximo 10) y el programa va pidiendo, pieza por pieza, cada uno de sus datos.

## ⚙️ Funcionalidades

- **Selección de cantidad**: pide cuántas piezas se van a registrar, con un máximo de 10 y hasta 3 intentos antes de cerrar el programa.
- **Registro por pieza**:
  - Identificador y nombre (texto libre).
  - Categoría (texto libre).
  - Precio: valida que sea un número entero mayor a 0, usando `try`/`except` para evitar errores si se ingresa texto.
  - Estado: menú de opciones (1. disponible / 2. reservada / 3. vendida).
  - Descripción: menú de opciones (1. usada / 2. certificada) combinado con texto adicional escrito por el usuario.
- **Validación de opciones**: cada menú usa un bucle `while True` que solo termina (`break`) cuando la opción ingresada es válida.
- **Resumen final**: al terminar, imprime el catálogo completo actualizado.

## 🧠 Conceptos de Python aplicados

- Diccionarios anidados y acceso dinámico a claves con f-strings (`catalog[f"piezas{cont2}"]`)
- Bucles `while` (incluyendo el patrón `while True` + `break` para repetición controlada)
- Validación de datos con `try` / `except`
- Conversión de tipos (`int()`, `str()`)
- `input()` y concatenación de cadenas

## ▶️ Cómo ejecutarlo

```bash
python nombre_del_archivo.py
```

Sigue las instrucciones que aparecen en consola para ir registrando cada pieza.

## 🚧 Pendiente

- Guardar el catálogo en un archivo externo (`.json`) para que los datos persistan entre ejecuciones.
- Validaciones adicionales según se sigan detectando casos no contemplados.
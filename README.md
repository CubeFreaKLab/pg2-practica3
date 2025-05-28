# PG2: PRÁCTICA 3

## API DE PELICULAS Y SERIES

### Descripción
Esta API REST permite crear, leer, actualizar y eliminar (CRUD) datos relacionados con:

- **Películas**: Información sobre títulos, descripciones, fechas de estreno, duración, géneros y directores.
- **Series**: Datos de series televisivas, incluyendo temporadas, episodios, creadores y fechas de lanzamiento.
- **Actores**: Datos biográficos de actores y actrices que participan en películas y series.
- **Roles**: La relación entre actores y los personajes que interpretan en películas o series.

### ¿Para qué sirve esta API?

Esta API está diseñada para desarrolladores y proyectos que necesiten una base de datos organizada y accesible sobre contenido audiovisual. Algunas aplicaciones comunes incluyen:

- Aplicaciones web o móviles para catalogar y mostrar películas y series.
- Plataformas de streaming que necesitan gestionar información sobre su contenido.
- Proyectos educativos o de análisis de cine y televisión.
- Cualquier sistema que requiera un backend para gestionar datos de entretenimiento.

## Instalación y Configuración

### Requisitos
- Python 3.8+
- Django 5.2.1
- Django REST Framework 3.16.0
- Django Extensions 4.1

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/CubeFreaKLab/pg2-practica3.git
cd filmsdataapi
```

2. **Crear entorno virtual**
```bash
python -m venv env
.\env\Scripts\activate # En Windows
source env/bin/activate  # En Linux
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar migraciones**
```bash
python manage.py migrate
```

5. **Iniciar el servidor**
```bash
python manage.py runserver
```

La API estará disponible en `http://localhost:8000/api/`

## Diagrama de Modelos

 ![Image Alt](https://github.com/CubeFreaKLab/pg2-practica3/blob/main/diagrama.png?raw=true)

```
Pelicula
├── id (BigAutoField)
├── titulo (CharField)
├── descripcion (TextField)
├── fecha_estreno (DateField)
├── duracion (PositiveIntegerField)
├── genero (CharField)
└── director (CharField)

Serie
├── id (BigAutoField)
├── titulo (CharField)
├── descripcion (TextField)
├── fecha_estreno (DateField)
├── temporadas (PositiveIntegerField)
├── episodios (PositiveIntegerField)
└── creador (CharField)

Actor
├── id (BigAutoField)
├── nombre (CharField)
├── fecha_nacimiento (DateField)
└── nacionalidad (CharField)

Rol
├── id (BigAutoField)
├── actor (ForeignKey → Actor)
├── pelicula (ForeignKey → Pelicula, opcional)
├── serie (ForeignKey → Serie, opcional)
└── nombre_personaje (CharField)
```

## Referencia de Endpoints

### Base URL
`http://localhost:8000/api/`

### 1. Películas (`/peliculas/`)

| Método | Endpoint | Descripción | Argumentos |
|--------|----------|-------------|------------|
| `GET` | `/peliculas/` | Listar todas las películas | - |
| `POST` | `/peliculas/` | Crear nueva película | JSON con datos de película |
| `GET` | `/peliculas/{id}/` | Obtener película específica | `id`: ID de la película |
| `PUT` | `/peliculas/{id}/` | Actualizar película completa | `id`: ID de la película, JSON con todos los campos |
| `PATCH` | `/peliculas/{id}/` | Actualizar película parcial | `id`: ID de la película, JSON con campos a actualizar |
| `DELETE` | `/peliculas/{id}/` | Eliminar película | `id`: ID de la película |

**Estructura de datos:**
```json
{
  "id": 1,
  "titulo": "El Padrino",
  "descripcion": "Historia de una familia mafiosa italiana en Nueva York",
  "fecha_estreno": "1972-03-24",
  "duracion": 175,
  "genero": "Drama",
  "director": "Francis Ford Coppola"
}
```

### 2. Series (`/series/`)

| Método | Endpoint | Descripción | Argumentos |
|--------|----------|-------------|------------|
| `GET` | `/series/` | Listar todas las series | - |
| `POST` | `/series/` | Crear nueva serie | JSON con datos de serie |
| `GET` | `/series/{id}/` | Obtener serie específica | `id`: ID de la serie |
| `PUT` | `/series/{id}/` | Actualizar serie completa | `id`: ID de la serie, JSON con todos los campos |
| `PATCH` | `/series/{id}/` | Actualizar serie parcial | `id`: ID de la serie, JSON con campos a actualizar |
| `DELETE` | `/series/{id}/` | Eliminar serie | `id`: ID de la serie |

**Estructura de datos:**
```json
{
  "id": 1,
  "titulo": "Breaking Bad",
  "descripcion": "Un profesor de química se convierte en fabricante de metanfetaminas",
  "fecha_estreno": "2008-01-20",
  "temporadas": 5,
  "episodios": 62,
  "creador": "Vince Gilligan"
}
```

### 3. Actores (`/actores/`)

| Método | Endpoint | Descripción | Argumentos |
|--------|----------|-------------|------------|
| `GET` | `/actores/` | Listar todos los actores | - |
| `POST` | `/actores/` | Crear nuevo actor | JSON con datos de actor |
| `GET` | `/actores/{id}/` | Obtener actor específico | `id`: ID del actor |
| `PUT` | `/actores/{id}/` | Actualizar actor completo | `id`: ID del actor, JSON con todos los campos |
| `PATCH` | `/actores/{id}/` | Actualizar actor parcial | `id`: ID del actor, JSON con campos a actualizar |
| `DELETE` | `/actores/{id}/` | Eliminar actor | `id`: ID del actor |

**Estructura de datos:**
```json
{
  "id": 1,
  "nombre": "Bryan Cranston",
  "fecha_nacimiento": "1956-03-07",
  "nacionalidad": "Estadounidense"
}
```

### 4. Roles (`/roles/`)

| Método | Endpoint | Descripción | Argumentos |
|--------|----------|-------------|------------|
| `GET` | `/roles/` | Listar todos los roles | - |
| `POST` | `/roles/` | Crear nuevo rol | JSON con datos de rol |
| `GET` | `/roles/{id}/` | Obtener rol específico | `id`: ID del rol |
| `PUT` | `/roles/{id}/` | Actualizar rol completo | `id`: ID del rol, JSON con todos los campos |
| `PATCH` | `/roles/{id}/` | Actualizar rol parcial | `id`: ID del rol, JSON con campos a actualizar |
| `DELETE` | `/roles/{id}/` | Eliminar rol | `id`: ID del rol |

**Estructura de datos:**
```json
{
  "id": 1,
  "actor": 1,
  "pelicula": null,
  "serie": 1,
  "nombre_personaje": "Walter White"
}
```

## Ejemplo de Caso de Uso

### Escenario: Gestión de la serie "Breaking Bad" con su reparto principal

Este ejemplo muestra cómo usar todos los endpoints para crear y gestionar información sobre la serie Breaking Bad, incluyendo actores y sus personajes.

#### Paso 1: Crear la serie Breaking Bad
**Endpoint:** `POST /api/series/`

```bash
curl -X POST http://localhost:8000/api/series/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Breaking Bad",
    "descripcion": "Un profesor de química de secundaria se asocia con un ex alumno para fabricar y vender metanfetaminas después de enterarse de que tiene cáncer terminal.",
    "fecha_estreno": "2008-01-20",
    "temporadas": 5,
    "episodios": 62,
    "creador": "Vince Gilligan"
  }'
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "titulo": "Breaking Bad",
  "descripcion": "Un profesor de química de secundaria se asocia con un ex alumno para fabricar y vender metanfetaminas después de enterarse de que tiene cáncer terminal.",
  "fecha_estreno": "2008-01-20",
  "temporadas": 5,
  "episodios": 62,
  "creador": "Vince Gilligan"
}
```

#### Paso 2: Crear los actores principales
**Endpoint:** `POST /api/actores/`

**Crear Bryan Cranston:**
```bash
curl -X POST http://localhost:8000/api/actores/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Bryan Cranston",
    "fecha_nacimiento": "1956-03-07",
    "nacionalidad": "Estadounidense"
  }'
```

**Crear Aaron Paul:**
```bash
curl -X POST http://localhost:8000/api/actores/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Aaron Paul",
    "fecha_nacimiento": "1979-08-27",
    "nacionalidad": "Estadounidense"
  }'
```

#### Paso 3: Asignar roles a los actores
**Endpoint:** `POST /api/roles/`

**Asignar Walter White a Bryan Cranston:**
```bash
curl -X POST http://localhost:8000/api/roles/ \
  -H "Content-Type: application/json" \
  -d '{
    "actor": 1,
    "serie": 1,
    "pelicula": null,
    "nombre_personaje": "Walter White"
  }'
```

**Asignar Jesse Pinkman a Aaron Paul:**
```bash
curl -X POST http://localhost:8000/api/roles/ \
  -H "Content-Type: application/json" \
  -d '{
    "actor": 2,
    "serie": 1,
    "pelicula": null,
    "nombre_personaje": "Jesse Pinkman"
  }'
```

#### Paso 4: Consultar información completa
**Endpoint:** `GET /api/series/`

```bash
curl http://localhost:8000/api/series/
```

**Endpoint:** `GET /api/actores/`

```bash
curl http://localhost:8000/api/actores/
```

**Endpoint:** `GET /api/roles/`

```bash
curl http://localhost:8000/api/roles/
```

#### Paso 5: Actualizar información específica
**Endpoint:** `PATCH /api/series/1/`

```bash
curl -X PATCH http://localhost:8000/api/series/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "descripcion": "Galardonada serie sobre un profesor de química que se convierte en el fabricante de drogas más temido de Albuquerque."
  }'
```

#### Paso 6: Consultar actor específico
**Endpoint:** `GET /api/actores/1/`

```bash
curl http://localhost:8000/api/actores/1/
```

#### Paso 7: Eliminar un rol (si es necesario)
**Endpoint:** `DELETE /api/roles/1/`

```bash
curl -X DELETE http://localhost:8000/api/roles/1/
```

### Flujo completo del caso de uso:

1. **POST /api/series/**: Crea la serie Breaking Bad
2. **POST /api/actores/**: Crea los actores Bryan Cranston y Aaron Paul
3. **POST /api/roles/**: Asigna los personajes Walter White y Jesse Pinkman a sus respectivos actores
4. **GET /api/series/**: Lista todas las series para verificar la creación
5. **GET /api/actores/**: Lista todos los actores registrados
6. **GET /api/roles/**: Muestra las relaciones entre actores y personajes
7. **PATCH /api/series/1/**: Actualiza la descripción de la serie
8. **GET /api/actores/1/**: Consulta información específica de Bryan Cranston
9. **DELETE /api/roles/1/**: Elimina una relación actor-personaje si es necesario

## Licencia de Publicación

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.
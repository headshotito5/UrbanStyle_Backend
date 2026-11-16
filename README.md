# UrbanStyle — Backend

Backend académico para **UrbanStyle**, una barbería que administra información de barberos, productos, servicios y reservas. Está desarrollado con **Python, Django, Django REST Framework y MongoDB Atlas**.

> **Estado del proyecto:** en desarrollo e integración. Existen modelos, serializers, rutas de API y vistas HTML, pero algunas vistas y la escritura de reservas aún requieren correcciones y pruebas. Este README describe la versión revisada de `UrbanStyle_Backend88.zip`.

## Tecnologías

- **Python 3.11**, utilizado durante las pruebas locales.
- **Django 5.2** y **Django REST Framework**, para la aplicación web y la API.
- **Django MongoDB Backend** y **Django MongoDB Extensions**, para los modelos y serializers de MongoDB.
- **MongoDB Atlas**, para el almacenamiento de los datos.
- **HTML y CSS**, para las páginas básicas de Django.
- **`unittest`**, para las pruebas automatizadas.

## Funcionalidades implementadas

- Modelos para **Barbero**, **Producto**, **Servicio** y **Reserva**.
- Serializers para representar los cuatro modelos en la API REST.
- Validaciones de productos: precio y stock no negativos.
- Validaciones de servicios: precio no negativo y duración mayor que cero.
- Validación independiente de reservas: fecha no pasada, hora de término posterior a la de inicio y **duración mínima de 20 minutos**.
- Validación básica de horarios de reserva: lista no vacía, con campos `dia` y `hora` que no estén vacíos.
- Rutas de API para listar, consultar, crear, actualizar y eliminar registros mediante `ModelViewSet`. **Las operaciones de escritura todavía deben verificarse en conjunto con MongoDB Atlas**.
- Páginas HTML básicas para inicio, productos, servicios, personal y reservas, con correcciones de integración pendientes.

## Estructura del proyecto

```text
UrbanStyle_Backend/
├── README.md
└── barbería/
    └── UrbanStyle/
        ├── manage.py
        ├── config/
        │   ├── settings.py
        │   └── urls.py
        └── inicio/
            ├── models.py
            ├── views.py
            ├── urls.py
            ├── api_urls.py
            ├── serializers.py
            ├── serializers_mongo.py
            ├── validaciones.py
            ├── test_validaciones.py
            ├── templates/inicio/
            └── static/
```

### Archivos principales

| Archivo | Responsabilidad |
| --- | --- |
| `inicio/models.py` | Define los modelos y sus colecciones en MongoDB. |
| `inicio/serializers_mongo.py` | Convierte y valida datos de los modelos para la API REST. |
| `inicio/serializers.py` | Valida fechas y horarios mediante `ReservaSerializer`. |
| `inicio/validaciones.py` | Contiene funciones reutilizables de validación de reservas. |
| `inicio/views.py` | Implementa las vistas HTML y los `ModelViewSet` de la API. |
| `inicio/api_urls.py` | Registra las rutas de la API con un router. |
| `inicio/test_validaciones.py` | Contiene las pruebas automatizadas de validaciones y serializers. |

## Instalación y ejecución local

### 1. Requisitos previos

- Python 3.11 y `pip`.
- Acceso a una instancia autorizada de MongoDB Atlas.
- Credenciales de base de datos facilitadas de forma segura por el responsable del proyecto.

Desde la **raíz del repositorio**, acceder a la carpeta donde se encuentra `manage.py`:

```powershell
cd ".\barbería\UrbanStyle"
```

### 2. Crear un entorno virtual (recomendado)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

La versión revisada **no incluye todavía `requirements.txt`**. Como punto de partida, instalar las dependencias utilizadas por el proyecto:

```powershell
python -m pip install "Django>=5.2,<5.3" "django-mongodb-backend>=5.2,<5.3" "django-mongodb-extensions[rest_framework]==0.3.0" "djangorestframework>=3.16,<4"
```

Antes de la entrega final se recomienda generar y revisar un `requirements.txt` para reproducir las versiones utilizadas por el equipo.

### 4. Configurar MongoDB Atlas

El proyecto configura la conexión en `config/settings.py` mediante `DATABASES`, con el motor `django_mongodb_backend` y la base de datos `urbanstyle_db`.

**Seguridad:** no publicar cadenas de conexión con usuario y contraseña. El responsable de MongoDB debe trasladar las credenciales a variables de entorno o a un sistema seguro de secretos y actualizar `settings.py` para leerlas. La versión revisada todavía requiere ese ajuste. También debe autorizarse la IP pública del equipo en la lista de acceso de Atlas.

El proyecto utiliza modelos con `managed = False`: las colecciones deben existir en la base de datos configurada. No se debe asumir que ejecutar migraciones creará estas colecciones.

### 5. Iniciar el servidor

Desde la carpeta que contiene `manage.py`:

```powershell
python manage.py check
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/> en el navegador. La API está disponible en <http://127.0.0.1:8000/api/>.

> **Nota:** `python manage.py check` comprueba parte de la configuración, pero no demuestra que todos los endpoints o las páginas HTML funcionen. Algunas vistas todavía tienen incidencias identificadas en esta versión.

## Endpoints de la API REST

Las rutas se registran en `inicio/api_urls.py` y se publican bajo el prefijo `/api/`.

| Recurso | Listado y creación | Detalle, actualización y eliminación |
| --- | --- | --- |
| Productos | `/api/productos/` | `/api/productos/{id}/` |
| Servicios | `/api/servicios/` | `/api/servicios/{id}/` |
| Barberos | `/api/barberos/` | `/api/barberos/{id}/` |
| Reservas | `/api/reservas/` | `/api/reservas/{id}/` |

Los `ModelViewSet` están preparados para los métodos habituales `GET`, `POST`, `PUT`, `PATCH` y `DELETE`, según la ruta.

### Ejemplo: consulta de productos

Iniciar Django y visitar:

```text
GET http://127.0.0.1:8000/api/productos/
```

En una comprobación manual se obtuvo una respuesta **HTTP 200 OK** con productos existentes en MongoDB Atlas. Los campos de producto incluyen `id`, `marca`, `nombre`, `categoria`, `precio` y `stock`.

## Validaciones

- **Producto:** `precio >= 0` y `stock >= 0`.
- **Servicio:** `precio >= 0` y `duracion > 0`.
- **Reserva (validador independiente):** no permitir fechas pasadas; la hora final debe ser posterior a la inicial; duración mínima predeterminada de **20 minutos**.
- **Reserva MongoDB:** la lista `horario` no puede estar vacía, y cada elemento debe incluir valores no vacíos para `dia` y `hora`.

**Limitación actual:** el validador independiente de reservas utiliza `fecha_reserva`, `hora_inicio` y `hora_fin`, mientras que el modelo `Reserva` utiliza `horario`. Además, se observó una diferencia entre el tipo declarado en el modelo y los diccionarios presentes en los registros reales. La integración de estas estructuras debe resolverse antes de considerar finalizado el guardado de reservas.

## Pruebas automatizadas

Desde el directorio de `manage.py` ejecutar:

```powershell
python -m unittest inicio.test_validaciones -v
```

En la versión revisada, el archivo contiene **22 pruebas** distribuidas en:

| Área | Casos |
| --- | ---: |
| Funciones de validación | 9 |
| Serializer independiente de reservas | 5 |
| Serializers MongoDB de productos y servicios | 6 |
| Validación de horario de reservas MongoDB | 2 |
| **Total** | **22** |

Estas pruebas comprueban principalmente reglas y validación de datos **sin guardar documentos**. En ejecuciones locales previas se obtuvo `OK` para las 22 pruebas; antes de entregar, se deben repetir sobre la versión definitiva y guardar la evidencia.

### Evidencias de funcionamiento de la API

Para la evaluación, guardar capturas de Postman, Insomnia o una herramienta equivalente que muestren **método HTTP, URL, código de estado y respuesta**. Se recomienda cubrir cada recurso y las operaciones CRUD requeridas, utilizando registros de prueba para crear, modificar y eliminar. No incluir credenciales ni datos personales de clientes en las capturas.


## Alcance

Este repositorio contiene el **backend Django** y plantillas HTML básicas. No se incluye en esta estructura el frontend React de la barbería. La integración con un frontend independiente requiere configuración y pruebas adicionales.

---

**Proyecto UrbanStyle — Desarrollo de Aplicaciones Web.**
USO DE IA: 
README.md = 100%
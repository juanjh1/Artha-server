# Artha - Sistema de Evaluación de Código

Artha es un sistema de evaluación de código desarrollado con Django y Django REST Framework que utiliza Judge0 como motor de ejecución de código.

## Requisitos Previos

- Python 3.11+
- Docker y Docker Compose
- Git

## Estructura del Proyecto

```
artha/
├── artha/              # Configuración principal de Django
├── judge/              # Aplicación para gestión de jueces
├── submission/         # Aplicación para gestión de envíos
├── run.py             # Script de automatización
├── docker-compose.yml # Configuración de Judge0
├── judge0.conf        # Configuración de Judge0
└── requirements.txt   # Dependencias de Python
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <https://github.com/juanjh1/Artha-server>
cd artha
```

### 2. Crear entorno virtual

```bash
python -m venv env
```

### 3. Activar entorno virtual

**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

### 1. Iniciar servicios de Judge0

El proyecto utiliza Judge0 como motor de evaluación. Para iniciarlo:

```bash
docker-compose up -d
```

Esto iniciará los siguientes servicios:
- **Judge0 Server** (puerto 2358)
- **Judge0 Workers** 
- **PostgreSQL** (base de datos para Judge0)
- **Redis** (cola de trabajos)

### 2. Configurar base de datos de Django

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

## Ejecución

### Método 1: Usando el script de automatización (Recomendado)

El proyecto incluye un script `run.py` que automatiza las tareas comunes:

```bash
# Ejecutar linting y verificaciones de código
python run.py

# Ejecutar migraciones y iniciar servidor
python run.py -m -r

# Crear superusuario
python run.py -c

# Todas las opciones juntas
python run.py -m -c -r
```

**Opciones disponibles:**
- `-m, --run_migrations`: Ejecuta makemigrations y migrate
- `-r, --run_server`: Inicia el servidor de desarrollo
- `-c, --create_user`: Crea un superusuario

### Método 2: Comandos manuales

```bash
# Verificar código con mypy y ruff
mypy .
ruff check . --fix

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver
```

## Acceso a la Aplicación

Una vez iniciado el servidor:

- **Aplicación Django**: http://localhost:8000
- **Admin de Django**: http://localhost:8000/admin
- **Judge0 API**: http://localhost:2358

## Desarrollo

### Herramientas de Calidad de Código

El proyecto utiliza:
- **mypy**: Verificación de tipos estáticos
- **ruff**: Linting y formateo de código

### Estructura de Aplicaciones

- **judge/**: Gestiona la configuración y administración de jueces
- **submission/**: Maneja los envíos de código y su evaluación

### Configuración de Judge0

La configuración de Judge0 se encuentra en `judge0.conf`. Los servicios principales son:
- Base de datos PostgreSQL para almacenar resultados
- Redis para gestión de colas
- Workers para procesar envíos de código

## Comandos Útiles

```bash
# Detener servicios de Docker
docker-compose down

# Ver logs de Judge0
docker-compose logs -f

# Reiniciar servicios
docker-compose restart

# Ejecutar tests
python manage.py test

# Crear nueva aplicación Django
python manage.py startapp nombre_app
```

## Solución de Problemas

### Judge0 no responde
```bash
docker-compose down
docker-compose up -d
```

### Error de migraciones
```bash
python manage.py makemigrations --empty nombre_app
python manage.py migrate
```

### Problemas con dependencias
```bash
pip install --upgrade -r requirements.txt
```


- [Contributing](https://github.com/juanjh1/Artha-server?tab=contributing-ov-file)



# TodoList API - Django + MySQL

Este proyecto es una API REST creada con **Django REST Framework** y base de datos **MySQL**.  
La API permite gestionar una lista de tareas (crear, listar, actualizar y eliminar tareas).

## 🚀 Características
- API REST construida con Django y Django REST Framework.
- Base de datos MySQL para persistencia de datos.
- Manejo automático de timestamps (`created_at`, `updated_at`).
- Configuración de **CORS** para permitir peticiones desde frontend.

---

## 📋 Prerrequisitos
Antes de instalar el proyecto asegúrate de tener:
- Python 3.10+
- MySQL instalado y corriendo
- `pip` (gestor de paquetes de Python)
- Virtualenv (opcional, recomendado)

---

## ⚙️ Instalación y configuración

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/tuusuario/todolist-django.git
   cd todolist-django
   ```

2. **Crea y activa un entorno virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate    # En Windows
   ```

3. **Instala las dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos MySQL**  
   Crea una base de datos en MySQL llamada `todolist_db`.  
   CREATE DATABASE todolist_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   Edita el archivo `settings.py` en la sección `DATABASES` para que coincida con tus credenciales:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'todolist_db',
           'USER': 'root',
           'PASSWORD': 'tu_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Aplica migraciones**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Ejecuta el servidor**  
   ```bash
   python manage.py runserver
   ```

---

## 🌐 Endpoints principales

- **Crear tarea (POST)** → `/api/tasks/`
  ```json
  {
    "title": "Mi primera tarea",
    "description": "Descripción de la tarea"
  }
  ```

- **Listar tareas (GET)** → `/api/tasks/`
- **Actualizar tarea (PUT/PATCH)** → `/api/tasks/{id}/`
- **Eliminar tarea (DELETE)** → `/api/tasks/{id}/`

---

## 🔧 Habilitar CORS
Se configuró con el paquete `django-cors-headers`.  
En `settings.py` se agregó:
```python
INSTALLED_APPS += ["corsheaders"]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOW_ALL_ORIGINS = True  # Permitir todos los orígenes
```

---

## 📄 Licencia
Este proyecto es de uso libre para fines educativos y puede adaptarse a proyectos personales o empresariales.

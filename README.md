# 🎓 ScholarTrack

**ScholarTrack** es un sistema de gestión escolar basado en consola desarrollado en Python. Está diseñado para que los profesores puedan administrar de manera eficiente periodos académicos, calificaciones, grupos, estudiantes y asignaturas, todo con persistencia de datos local mediante archivos JSON.

---

## 🚀 Características Principales

* **Gestión Académica Completa:** Control total sobre periodos escolares, asignaturas y grupos.
* **Administración de Alumnos:** Registro y seguimiento de estudiantes por grupo.
* **Control de Calificaciones:** Registro de notas por estudiante y materia.
* **Reportes Automáticos:** Generación de reportes de rendimiento académico.
* **Persistencia de Datos:** Toda la información se guarda automáticamente en archivos `.json`, evitando la pérdida de datos al cerrar la aplicación.
* **Interfaz de Consola Intuitiva:** Menús claros y validación de datos para evitar errores de usuario.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Almacenamiento:** JSON (JavaScript Object Notation)
* **Módulos Nativos:** `json`, `os`

---

## 📦 Estructura del Proyecto

```text
ScholarTrack/
│
├── data/
│   └── .gitkeep        # Archivo para permanencia de la carpeta
│   └── storage.json    # Archivo de persistencia de datos
│   └── configs.json    # Archivo de configuraciones guardadas
│
├── main.py             # Interfas y navegacion
├── storage.py          # Gestion de escritura de datos
├── utils.py            # Funciones mas usadas
├── config.py           # Archivo con configuracion predeteminada
│
├── README.md
└── .gitignore

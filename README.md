# 🖥️ Tarea: Registro de Usuarios - Tkinter + MySQL

Este proyecto consiste en una aplicación de escritorio desarrollada en **Python**, usando **Tkinter** como interfaz gráfica y **MySQL** como base de datos. Permite registrar nombres de usuarios en una tabla llamada `usuarios` y almacenarlos de forma segura utilizando variables de entorno.

<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/9fba9701-74b2-4a58-9078-4f99ae6c623d" />

---

## 🎓 Materia
**Tópicos Especiales de Ingeniería de Software**

---

## 🛠️ Tecnologías Utilizadas

- Python 3.11.4
- Tkinter (Interfaz gráfica)
- MySQL (usado con MySQL Workbench)
- `mysql-connector-python` (para conexión con la BD)
- `python-dotenv` (para manejar credenciales seguras)
- Git

---

## ⚙️ Requisitos previos

- Python 3 instalado
- MySQL Server + Workbench
- Crear una base de datos y tabla:
```sql
CREATE DATABASE nombre_de_tu_base;
USE nombre_de_tu_base;

CREATE TABLE usuarios (
    nombre VARCHAR(100)
);

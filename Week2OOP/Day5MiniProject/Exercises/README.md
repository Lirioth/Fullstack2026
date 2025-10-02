# 🛠️ Day 5 Exercises - Mini Project

## 🎯 Objetivo de los Ejercicios

Estos ejercicios te ayudarán a construir paso a paso el sistema integral de biblioteca digital, aplicando todos los conceptos de la semana.

---

## 🥉 Exercise 1: Modelado de Clases

### 📚 Descripción
Diseña las clases principales del sistema: `User`, `Book`, `Loan`.

### 📋 Requisitos
- Definir atributos y métodos clave para cada clase
- Implementar relaciones entre clases (ej: un usuario puede tener varios préstamos)
- Añadir validaciones básicas en los constructores
- Documentar cada clase con docstrings

---

## 🥈 Exercise 2: Carga y Validación de Datos

### 📊 Descripción
Implementa la carga de datos de libros desde un archivo CSV y/o una API externa.

### 📋 Requisitos
- Leer datos de libros desde CSV usando pandas o csv
- Validar y transformar los datos cargados
- Integrar datos adicionales desde una API (ej: Google Books)
- Manejar errores de formato y datos faltantes

---

## 🥇 Exercise 3: Gestión de Préstamos y Persistencia

### 💾 Descripción
Desarrolla la lógica para registrar préstamos y devoluciones, y almacena los datos en archivos JSON.

### 📋 Requisitos
- Métodos para registrar préstamo y devolución de libros
- Validar disponibilidad de libros y usuarios
- Guardar y cargar usuarios y préstamos en JSON
- Manejar errores de concurrencia y duplicados

---

## 💪 Exercise 4: Reportes y Testing

### 📈 Descripción
Implementa generación de reportes y pruebas unitarias para el sistema.

### 📋 Requisitos
- Generar reportes de libros más prestados, usuarios activos, etc.
- Crear pruebas unitarias para los módulos principales
- Documentar el flujo de trabajo y decisiones de diseño

---

## ✅ Criterios de Evaluación
- [ ] Modelado OOP correcto y documentado
- [ ] Carga y validación de datos robusta
- [ ] Persistencia y gestión de préstamos funcional
- [ ] Reportes útiles y pruebas unitarias

---

**💡 Consejo**: Trabaja de forma incremental, validando cada parte antes de avanzar. Usa tests para asegurar la calidad del sistema.

**🎯 Meta**: Construir un sistema profesional, modular y bien probado que integre todos los aprendizajes de la semana.
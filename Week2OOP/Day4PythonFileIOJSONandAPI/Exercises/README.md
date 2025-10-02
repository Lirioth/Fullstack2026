# 🛠️ Day 4 Exercises - Python File I/O, JSON and API

## 🎯 Objetivos de los Ejercicios

Estos ejercicios te ayudarán a dominar:
- 📁 **Lectura y escritura de archivos** en diferentes formatos
- 📊 **Procesamiento de datos CSV** y validación
- 🔄 **Serialización y deserialización JSON** avanzada
- 🌐 **Consumo de APIs REST** y manejo de respuestas
- 🛡️ **Manejo de errores y validación de datos externos**

---

## 🥉 Exercise 1: Sistema de Análisis de Datos CSV

### 📊 Descripción
Desarrolla un sistema que lea archivos CSV, procese los datos y genere reportes estadísticos.

### 📋 Requisitos
- Leer un archivo CSV con pandas y con el módulo csv estándar
- Validar y transformar tipos de datos (int, float, date)
- Calcular estadísticas básicas (suma, promedio, máximo, mínimo, mediana)
- Filtrar datos por condiciones (ej: ventas > 1000)
- Exportar resultados a un nuevo archivo CSV

---

## 🥈 Exercise 2: Aggregador de Noticias desde APIs

### 🌐 Descripción
Crea un script que consuma una API pública de noticias, procese los resultados y los almacene en JSON.

### 📋 Requisitos
- Usar requests para hacer GET a una API de noticias (ej: NewsAPI, GNews, etc.)
- Procesar la respuesta y extraer campos clave (título, fuente, fecha, resumen)
- Guardar los resultados en un archivo JSON
- Implementar manejo de errores y reintentos
- Permitir búsqueda por palabra clave y paginación

---

## 🥇 Exercise 3: Sistema de Backup y Sincronización

### 💾 Descripción
Desarrolla un sistema que realice backups automáticos de archivos y sincronización entre carpetas.

### 📋 Requisitos
- Crear backups de archivos con timestamp
- Sincronizar archivos entre dos carpetas (copiar solo los nuevos o modificados)
- Registrar logs de operaciones en un archivo de texto
- Validar integridad de archivos (hash MD5/SHA256)
- Manejar errores de permisos y espacio insuficiente

---

## 💪 Exercise 4: Pipeline de Procesamiento de Datos

### 🔄 Descripción
Implementa un pipeline completo que lea datos de CSV, los transforme, los combine con datos de una API y exporte el resultado en JSON.

### 📋 Requisitos
- Leer y limpiar datos de un archivo CSV
- Consumir una API para enriquecer los datos (ej: obtener información adicional por ID)
- Validar y transformar los datos combinados
- Exportar el resultado final a un archivo JSON
- Manejar errores y registrar el proceso

---

## ✅ Criterios de Evaluación
- [ ] Lectura y escritura de archivos robusta
- [ ] Procesamiento y validación de datos CSV
- [ ] Serialización/deserialización JSON avanzada
- [ ] Consumo de APIs con manejo de errores
- [ ] Logging y documentación clara

---

**💡 Consejo**: Siempre valida los datos externos antes de procesarlos. Implementa logs para rastrear errores y resultados.

**🎯 Meta**: Cada ejercicio debe demostrar integración real de datos externos y manejo profesional de archivos y APIs.
# 🌍 Daily Challenge - Sistema de Monitoreo Climático Global

## 🎯 Descripción del Desafío

Desarrolla un sistema completo que integre datos meteorológicos de múltiples fuentes (APIs y archivos históricos) para monitoreo, análisis y alertas climáticas.

---

## 🏗️ Arquitectura Sugerida

- **Módulo de Ingesta**: Lee datos históricos desde CSV y consume APIs meteorológicas públicas (ej: OpenWeatherMap, WeatherAPI).
- **Procesador de Datos**: Limpia, valida y transforma los datos (unifica formatos, corrige valores atípicos).
- **Almacenamiento**: Guarda los datos procesados en archivos JSON estructurados.
- **Sistema de Alertas**: Detecta condiciones extremas (ej: temperaturas fuera de rango, lluvias intensas) y genera alertas.
- **Dashboard/Reporte**: Genera reportes diarios/semanales en texto o JSON.

---

## 📋 Requisitos Técnicos

- Leer archivos CSV históricos de clima (mínimo 1 año de datos)
- Consumir al menos 1 API meteorológica y combinar los datos con los históricos
- Validar y transformar los datos (fechas, unidades, valores nulos)
- Detectar eventos extremos y registrar alertas en un archivo
- Exportar reportes diarios/semanales en JSON
- Manejar errores de red, formato y datos faltantes
- Documentar el flujo de datos y decisiones tomadas

---

## 📝 Sugerencia de Estructura de Archivos
```
DailyChallenge/
├── data/
│   ├── historical_weather.csv
│   └── processed_weather.json
├── alerts/
│   └── alerts_log.txt
├── src/
│   ├── ingest.py
│   ├── processor.py
│   ├── storage.py
│   ├── alert_system.py
│   └── report.py
├── main.py
└── README.md
```

---

## 🏆 Criterios de Éxito
- [ ] Integración real de datos de al menos 2 fuentes
- [ ] Validación y limpieza robusta de datos
- [ ] Generación de alertas automáticas
- [ ] Reportes claros y útiles
- [ ] Código modular y documentado

---

**💡 Consejo**: Prioriza la validación y el manejo de errores. Documenta cada paso del pipeline y justifica tus decisiones de diseño.

**🎯 Meta**: Demostrar dominio en integración de datos externos, manejo de archivos y APIs, y generación de reportes útiles para usuarios reales.
# 📄 Day 4 - Python File I/O, JSON and API

## 🎯 Objetivos de Aprendizaje

Al finalizar este día, podrás:
- 📁 **Manejar archivos** de manera eficiente y segura
- 📄 **Procesar diferentes formatos** (TXT, CSV, JSON, XML)
- 🌐 **Consumir APIs REST** y manejar respuestas HTTP
- 🔄 **Serializar y deserializar** datos complejos
- 🛡️ **Manejar errores** de I/O y conexiones de red
- 🗃️ **Integrar datos externos** en aplicaciones OOP

## 📚 Conceptos Clave

### 📂 File I/O Fundamentals

#### 🔹 Operaciones Básicas de Archivos
```python
import os
from pathlib import Path

# Usando open() tradicional
def read_file_traditional(filename):
    """Lectura tradicional de archivos"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Usando pathlib (moderno)
def read_file_pathlib(filepath):
    """Lectura moderna con pathlib"""
    try:
        path = Path(filepath)
        if path.exists():
            return path.read_text(encoding='utf-8')
        else:
            print(f"File {filepath} does not exist")
            return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Lectura línea por línea (eficiente para archivos grandes)
def read_file_lines(filename):
    """Lectura línea por línea para archivos grandes"""
    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                lines.append({
                    'number': line_number,
                    'content': line.strip(),
                    'length': len(line.strip())
                })
        return lines
    except IOError as e:
        print(f"Error reading file: {e}")
        return []

# Escritura de archivos
def write_file_safe(filename, content, mode='w'):
    """Escritura segura de archivos"""
    try:
        # Crear directorio si no existe
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filename, mode, encoding='utf-8') as file:
            if isinstance(content, list):
                for line in content:
                    file.write(f"{line}\\n")
            else:
                file.write(content)
        
        print(f"File '{filename}' written successfully")
        return True
    except IOError as e:
        print(f"Error writing file: {e}")
        return False
```

#### 📋 Manejo Avanzado de Archivos
```python
import shutil
import tempfile
from datetime import datetime

class FileManager:
    """Gestor avanzado de archivos con funcionalidades OOP"""
    
    def __init__(self, base_directory="."):
        """
        Inicializar gestor de archivos
        
        Args:
            base_directory (str): Directorio base para operaciones
        """
        self.base_path = Path(base_directory)
        self.base_path.mkdir(exist_ok=True)
        self.temp_files = []
    
    def create_backup(self, filename, backup_suffix=None):
        """
        Crear backup de archivo
        
        Args:
            filename (str): Nombre del archivo
            backup_suffix (str): Sufijo para el backup
        
        Returns:
            str: Ruta del archivo de backup
        """
        original_path = self.base_path / filename
        
        if not original_path.exists():
            raise FileNotFoundError(f"File {filename} not found")
        
        if backup_suffix is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_suffix = f"_backup_{timestamp}"
        
        backup_name = f"{original_path.stem}{backup_suffix}{original_path.suffix}"
        backup_path = original_path.parent / backup_name
        
        shutil.copy2(original_path, backup_path)
        return str(backup_path)
    
    def get_file_info(self, filename):
        """
        Obtener información detallada de archivo
        
        Args:
            filename (str): Nombre del archivo
        
        Returns:
            dict: Información del archivo
        """
        file_path = self.base_path / filename
        
        if not file_path.exists():
            return None
        
        stat = file_path.stat()
        
        return {
            'name': file_path.name,
            'size_bytes': stat.st_size,
            'size_human': self._format_file_size(stat.st_size),
            'created': datetime.fromtimestamp(stat.st_ctime),
            'modified': datetime.fromtimestamp(stat.st_mtime),
            'accessed': datetime.fromtimestamp(stat.st_atime),
            'permissions': oct(stat.st_mode)[-3:],
            'is_directory': file_path.is_dir(),
            'extension': file_path.suffix,
            'absolute_path': str(file_path.absolute())
        }
    
    def _format_file_size(self, size_bytes):
        """Formatear tamaño de archivo en formato legible"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        
        return f"{s} {size_names[i]}"
    
    def find_files(self, pattern="*", recursive=True):
        """
        Buscar archivos por patrón
        
        Args:
            pattern (str): Patrón de búsqueda (glob)
            recursive (bool): Búsqueda recursiva
        
        Returns:
            list: Lista de archivos encontrados
        """
        if recursive:
            return list(self.base_path.rglob(pattern))
        else:
            return list(self.base_path.glob(pattern))
    
    def create_temp_file(self, content="", suffix=".tmp"):
        """
        Crear archivo temporal
        
        Args:
            content (str): Contenido inicial
            suffix (str): Sufijo del archivo
        
        Returns:
            str: Ruta del archivo temporal
        """
        temp_file = tempfile.NamedTemporaryFile(
            mode='w',
            suffix=suffix,
            delete=False,
            dir=self.base_path
        )
        
        temp_file.write(content)
        temp_file.close()
        
        self.temp_files.append(temp_file.name)
        return temp_file.name
    
    def cleanup_temp_files(self):
        """Limpiar archivos temporales creados"""
        for temp_file in self.temp_files:
            try:
                Path(temp_file).unlink()
            except FileNotFoundError:
                pass
        
        self.temp_files.clear()
    
    def __del__(self):
        """Destructor: limpiar archivos temporales"""
        self.cleanup_temp_files()
```

### 📊 Procesamiento de CSV

#### 📈 CSV con el Módulo csv
```python
import csv
from typing import List, Dict, Any
from decimal import Decimal
from datetime import datetime

class CSVProcessor:
    """Procesador avanzado de archivos CSV"""
    
    def __init__(self, delimiter=',', quotechar='"'):
        """
        Inicializar procesador CSV
        
        Args:
            delimiter (str): Delimitador de campos
            quotechar (str): Carácter de comillas
        """
        self.delimiter = delimiter
        self.quotechar = quotechar
    
    def read_csv_to_dict(self, filename: str) -> List[Dict[str, Any]]:
        """
        Leer CSV y convertir a lista de diccionarios
        
        Args:
            filename (str): Nombre del archivo CSV
        
        Returns:
            List[Dict[str, Any]]: Datos del CSV
        """
        data = []
        
        try:
            with open(filename, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(
                    file,
                    delimiter=self.delimiter,
                    quotechar=self.quotechar
                )
                
                for row_number, row in enumerate(reader, 2):  # Empezar en 2 (fila 1 = headers)
                    # Limpiar espacios en blanco
                    cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
                    
                    # Añadir metadatos
                    cleaned_row['_row_number'] = row_number
                    cleaned_row['_original_row'] = dict(row)
                    
                    data.append(cleaned_row)
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file '{filename}' not found")
        except csv.Error as e:
            raise ValueError(f"Error reading CSV file: {e}")
        
        return data
    
    def write_dict_to_csv(self, filename: str, data: List[Dict[str, Any]], 
                         fieldnames: List[str] = None) -> bool:
        """
        Escribir lista de diccionarios a CSV
        
        Args:
            filename (str): Nombre del archivo CSV
            data (List[Dict[str, Any]]): Datos a escribir
            fieldnames (List[str]): Nombres de campos (opcional)
        
        Returns:
            bool: True si se escribió correctamente
        """
        if not data:
            raise ValueError("No data provided to write")
        
        # Determinar fieldnames si no se proporcionan
        if fieldnames is None:
            fieldnames = list(data[0].keys())
            # Filtrar metadatos si existen
            fieldnames = [f for f in fieldnames if not f.startswith('_')]
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                    delimiter=self.delimiter,
                    quotechar=self.quotechar,
                    quoting=csv.QUOTE_MINIMAL
                )
                
                writer.writeheader()
                
                for row in data:
                    # Filtrar solo los campos especificados
                    filtered_row = {k: v for k, v in row.items() if k in fieldnames}
                    writer.writerow(filtered_row)
            
            return True
            
        except IOError as e:
            print(f"Error writing CSV file: {e}")
            return False
    
    def convert_types(self, data: List[Dict[str, Any]], 
                     type_mapping: Dict[str, type]) -> List[Dict[str, Any]]:
        """
        Convertir tipos de datos en CSV
        
        Args:
            data (List[Dict[str, Any]]): Datos originales
            type_mapping (Dict[str, type]): Mapeo de campos a tipos
        
        Returns:
            List[Dict[str, Any]]: Datos con tipos convertidos
        """
        converted_data = []
        
        for row in data:
            converted_row = row.copy()
            
            for field, target_type in type_mapping.items():
                if field in row and row[field]:
                    try:
                        if target_type == int:
                            converted_row[field] = int(float(row[field]))
                        elif target_type == float:
                            converted_row[field] = float(row[field])
                        elif target_type == Decimal:
                            converted_row[field] = Decimal(row[field])
                        elif target_type == datetime:
                            converted_row[field] = datetime.fromisoformat(row[field])
                        elif target_type == bool:
                            converted_row[field] = row[field].lower() in ['true', '1', 'yes', 'on']
                        else:
                            converted_row[field] = target_type(row[field])
                    
                    except (ValueError, TypeError) as e:
                        print(f"Warning: Could not convert '{row[field]}' to {target_type.__name__} for field '{field}': {e}")
                        # Mantener valor original en caso de error
                        pass
            
            converted_data.append(converted_row)
        
        return converted_data
    
    def filter_data(self, data: List[Dict[str, Any]], 
                   filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Filtrar datos CSV
        
        Args:
            data (List[Dict[str, Any]]): Datos originales
            filters (Dict[str, Any]): Filtros a aplicar
        
        Returns:
            List[Dict[str, Any]]: Datos filtrados
        """
        filtered_data = []
        
        for row in data:
            match = True
            
            for field, filter_value in filters.items():
                if field not in row:
                    match = False
                    break
                
                row_value = row[field]
                
                # Diferentes tipos de filtros
                if isinstance(filter_value, dict):
                    # Filtros avanzados: {'gte': 100}, {'contains': 'text'}
                    if 'gte' in filter_value and row_value < filter_value['gte']:
                        match = False
                        break
                    if 'lte' in filter_value and row_value > filter_value['lte']:
                        match = False
                        break
                    if 'contains' in filter_value and filter_value['contains'] not in str(row_value):
                        match = False
                        break
                    if 'in' in filter_value and row_value not in filter_value['in']:
                        match = False
                        break
                else:
                    # Filtro directo por valor
                    if row_value != filter_value:
                        match = False
                        break
            
            if match:
                filtered_data.append(row)
        
        return filtered_data
    
    def get_statistics(self, data: List[Dict[str, Any]], 
                      numeric_fields: List[str]) -> Dict[str, Dict[str, float]]:
        """
        Calcular estadísticas para campos numéricos
        
        Args:
            data (List[Dict[str, Any]]): Datos del CSV
            numeric_fields (List[str]): Campos numéricos a analizar
        
        Returns:
            Dict[str, Dict[str, float]]: Estadísticas por campo
        """
        statistics = {}
        
        for field in numeric_fields:
            values = []
            
            for row in data:
                if field in row and row[field] is not None:
                    try:
                        value = float(row[field])
                        values.append(value)
                    except (ValueError, TypeError):
                        continue
            
            if values:
                statistics[field] = {
                    'count': len(values),
                    'sum': sum(values),
                    'mean': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'median': sorted(values)[len(values) // 2]
                }
            else:
                statistics[field] = {
                    'count': 0,
                    'sum': 0,
                    'mean': 0,
                    'min': 0,
                    'max': 0,
                    'median': 0
                }
        
        return statistics
```

### 🔄 JSON Processing

#### 📋 JSON Avanzado con Validación
```python
import json
from typing import Any, Dict, List, Optional, Union
from datetime import datetime, date
from decimal import Decimal
from pathlib import Path

class JSONProcessor:
    """Procesador avanzado de JSON con validación y serialización custom"""
    
    def __init__(self, indent=2, ensure_ascii=False):
        """
        Inicializar procesador JSON
        
        Args:
            indent (int): Indentación para pretty printing
            ensure_ascii (bool): Forzar ASCII en output
        """
        self.indent = indent
        self.ensure_ascii = ensure_ascii
    
    def load_json(self, filename: str) -> Any:
        """
        Cargar JSON desde archivo
        
        Args:
            filename (str): Nombre del archivo JSON
        
        Returns:
            Any: Datos deserializados
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file '{filename}' not found")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file '{filename}': {e}")
    
    def save_json(self, data: Any, filename: str) -> bool:
        """
        Guardar datos como JSON
        
        Args:
            data (Any): Datos a serializar
            filename (str): Nombre del archivo
        
        Returns:
            bool: True si se guardó correctamente
        """
        try:
            # Crear directorio si no existe
            Path(filename).parent.mkdir(parents=True, exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(
                    data,
                    file,
                    indent=self.indent,
                    ensure_ascii=self.ensure_ascii,
                    default=self._json_serializer
                )
            
            return True
            
        except (IOError, TypeError) as e:
            print(f"Error saving JSON file: {e}")
            return False
    
    def _json_serializer(self, obj: Any) -> Any:
        """
        Serializer custom para tipos no JSON nativos
        
        Args:
            obj (Any): Objeto a serializar
        
        Returns:
            Any: Objeto serializable
        """
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    def validate_schema(self, data: Any, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validar datos contra un schema simple
        
        Args:
            data (Any): Datos a validar
            schema (Dict[str, Any]): Schema de validación
        
        Returns:
            Dict[str, Any]: Resultado de validación
        """
        errors = []
        warnings = []
        
        def validate_field(field_name: str, value: Any, field_schema: Dict[str, Any]):
            """Validar campo individual"""
            # Verificar tipo requerido
            if 'type' in field_schema:
                expected_type = field_schema['type']
                if expected_type == 'string' and not isinstance(value, str):
                    errors.append(f"Field '{field_name}' must be string, got {type(value).__name__}")
                elif expected_type == 'number' and not isinstance(value, (int, float)):
                    errors.append(f"Field '{field_name}' must be number, got {type(value).__name__}")
                elif expected_type == 'array' and not isinstance(value, list):
                    errors.append(f"Field '{field_name}' must be array, got {type(value).__name__}")
                elif expected_type == 'object' and not isinstance(value, dict):
                    errors.append(f"Field '{field_name}' must be object, got {type(value).__name__}")
            
            # Verificar valor requerido
            if field_schema.get('required', False) and (value is None or value == ""):
                errors.append(f"Field '{field_name}' is required")
            
            # Verificar longitud mínima/máxima
            if isinstance(value, (str, list)):
                min_length = field_schema.get('min_length')
                max_length = field_schema.get('max_length')
                
                if min_length and len(value) < min_length:
                    errors.append(f"Field '{field_name}' must have at least {min_length} characters/items")
                
                if max_length and len(value) > max_length:
                    errors.append(f"Field '{field_name}' must have at most {max_length} characters/items")
            
            # Verificar rango para números
            if isinstance(value, (int, float)):
                min_value = field_schema.get('min_value')
                max_value = field_schema.get('max_value')
                
                if min_value is not None and value < min_value:
                    errors.append(f"Field '{field_name}' must be at least {min_value}")
                
                if max_value is not None and value > max_value:
                    errors.append(f"Field '{field_name}' must be at most {max_value}")
            
            # Verificar valores permitidos
            allowed_values = field_schema.get('allowed_values')
            if allowed_values and value not in allowed_values:
                errors.append(f"Field '{field_name}' must be one of {allowed_values}")
        
        # Validar estructura principal
        if not isinstance(data, dict):
            errors.append("Data must be a JSON object")
            return {'valid': False, 'errors': errors, 'warnings': warnings}
        
        # Validar campos definidos en schema
        for field_name, field_schema in schema.get('fields', {}).items():
            value = data.get(field_name)
            validate_field(field_name, value, field_schema)
        
        # Verificar campos no definidos en schema
        if schema.get('strict', False):
            for field_name in data:
                if field_name not in schema.get('fields', {}):
                    warnings.append(f"Unknown field '{field_name}' found in data")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def merge_json(self, base_data: Dict[str, Any], 
                  update_data: Dict[str, Any], 
                  deep_merge: bool = True) -> Dict[str, Any]:
        """
        Fusionar dos objetos JSON
        
        Args:
            base_data (Dict[str, Any]): Datos base
            update_data (Dict[str, Any]): Datos a fusionar
            deep_merge (bool): Fusión profunda de objetos anidados
        
        Returns:
            Dict[str, Any]: Datos fusionados
        """
        result = base_data.copy()
        
        for key, value in update_data.items():
            if key in result and deep_merge:
                if isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = self.merge_json(result[key], value, deep_merge)
                elif isinstance(result[key], list) and isinstance(value, list):
                    result[key] = result[key] + value
                else:
                    result[key] = value
            else:
                result[key] = value
        
        return result
    
    def extract_fields(self, data: Any, field_paths: List[str]) -> Dict[str, Any]:
        """
        Extraer campos específicos usando dot notation
        
        Args:
            data (Any): Datos JSON
            field_paths (List[str]): Rutas de campos (ej: 'user.profile.name')
        
        Returns:
            Dict[str, Any]: Campos extraídos
        """
        result = {}
        
        for path in field_paths:
            keys = path.split('.')
            current_data = data
            
            try:
                for key in keys:
                    if isinstance(current_data, dict):
                        current_data = current_data[key]
                    elif isinstance(current_data, list) and key.isdigit():
                        current_data = current_data[int(key)]
                    else:
                        raise KeyError(f"Cannot access {key}")
                
                result[path] = current_data
                
            except (KeyError, IndexError, TypeError):
                result[path] = None
        
        return result
    
    def transform_data(self, data: Any, transformations: Dict[str, callable]) -> Any:
        """
        Aplicar transformaciones a datos JSON
        
        Args:
            data (Any): Datos originales
            transformations (Dict[str, callable]): Transformaciones a aplicar
        
        Returns:
            Any: Datos transformados
        """
        if isinstance(data, dict):
            transformed = {}
            for key, value in data.items():
                if key in transformations:
                    transformed[key] = transformations[key](value)
                else:
                    transformed[key] = self.transform_data(value, transformations)
            return transformed
        
        elif isinstance(data, list):
            return [self.transform_data(item, transformations) for item in data]
        
        else:
            return data
```

### 🌐 API Consumption

#### 🔌 HTTP Client con requests
```python
import requests
from typing import Dict, Any, Optional, List, Union
from datetime import datetime, timedelta
import json
import time

class APIClient:
    """Cliente HTTP avanzado para consumo de APIs REST"""
    
    def __init__(self, base_url: str, timeout: int = 30, 
                 retry_attempts: int = 3, retry_delay: float = 1.0):
        """
        Inicializar cliente API
        
        Args:
            base_url (str): URL base de la API
            timeout (int): Timeout para requests
            retry_attempts (int): Intentos de reintento
            retry_delay (float): Delay entre reintentos
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay
        
        # Configuración de sesión
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Python-API-Client/1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        
        # Rate limiting
        self.rate_limit_delay = 0
        self.last_request_time = 0
        
        # Estadísticas
        self.request_count = 0
        self.success_count = 0
        self.error_count = 0
    
    def set_authentication(self, auth_type: str, **kwargs):
        """
        Configurar autenticación
        
        Args:
            auth_type (str): Tipo de autenticación
            **kwargs: Parámetros de autenticación
        """
        if auth_type == 'bearer_token':
            token = kwargs.get('token')
            self.session.headers['Authorization'] = f'Bearer {token}'
        
        elif auth_type == 'api_key':
            api_key = kwargs.get('api_key')
            header_name = kwargs.get('header_name', 'X-API-Key')
            self.session.headers[header_name] = api_key
        
        elif auth_type == 'basic':
            username = kwargs.get('username')
            password = kwargs.get('password')
            self.session.auth = (username, password)
        
        elif auth_type == 'custom_header':
            header_name = kwargs.get('header_name')
            header_value = kwargs.get('header_value')
            self.session.headers[header_name] = header_value
    
    def set_rate_limit(self, requests_per_second: float):
        """
        Configurar limitación de velocidad
        
        Args:
            requests_per_second (float): Requests permitidos por segundo
        """
        self.rate_limit_delay = 1.0 / requests_per_second if requests_per_second > 0 else 0
    
    def _wait_for_rate_limit(self):
        """Esperar si es necesario para respetar rate limiting"""
        if self.rate_limit_delay > 0:
            current_time = time.time()
            time_since_last_request = current_time - self.last_request_time
            
            if time_since_last_request < self.rate_limit_delay:
                sleep_time = self.rate_limit_delay - time_since_last_request
                time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Realizar request HTTP con reintentos
        
        Args:
            method (str): Método HTTP
            endpoint (str): Endpoint de la API
            **kwargs: Parámetros adicionales
        
        Returns:
            requests.Response: Respuesta HTTP
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Rate limiting
        self._wait_for_rate_limit()
        
        last_exception = None
        
        for attempt in range(self.retry_attempts):
            try:
                self.request_count += 1
                
                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )
                
                # Verificar códigos de estado que indican éxito
                if response.status_code < 400:
                    self.success_count += 1
                    return response
                
                # Para códigos 4xx, no reintentar (error del cliente)
                if 400 <= response.status_code < 500:
                    self.error_count += 1
                    response.raise_for_status()
                
                # Para códigos 5xx, reintentar
                if response.status_code >= 500 and attempt < self.retry_attempts - 1:
                    print(f"Server error {response.status_code}, retrying in {self.retry_delay}s...")
                    time.sleep(self.retry_delay * (attempt + 1))  # Backoff exponencial
                    continue
                
                # Si llegamos aquí, es el último intento
                self.error_count += 1
                response.raise_for_status()
                
            except requests.exceptions.RequestException as e:
                last_exception = e
                
                if attempt < self.retry_attempts - 1:
                    print(f"Request failed: {e}, retrying in {self.retry_delay}s...")
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                else:
                    self.error_count += 1
                    raise
        
        # Si llegamos aquí, todos los intentos fallaron
        if last_exception:
            raise last_exception
    
    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Realizar GET request
        
        Args:
            endpoint (str): Endpoint de la API
            params (Dict[str, Any]): Parámetros de query
        
        Returns:
            Dict[str, Any]: Respuesta JSON
        """
        response = self._make_request('GET', endpoint, params=params)
        return self._parse_response(response)
    
    def post(self, endpoint: str, data: Dict[str, Any] = None, 
             json_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Realizar POST request
        
        Args:
            endpoint (str): Endpoint de la API
            data (Dict[str, Any]): Datos form-encoded
            json_data (Dict[str, Any]): Datos JSON
        
        Returns:
            Dict[str, Any]: Respuesta JSON
        """
        kwargs = {}
        if json_data is not None:
            kwargs['json'] = json_data
        elif data is not None:
            kwargs['data'] = data
        
        response = self._make_request('POST', endpoint, **kwargs)
        return self._parse_response(response)
    
    def put(self, endpoint: str, json_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Realizar PUT request"""
        response = self._make_request('PUT', endpoint, json=json_data)
        return self._parse_response(response)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Realizar DELETE request"""
        response = self._make_request('DELETE', endpoint)
        return self._parse_response(response)
    
    def _parse_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Parsear respuesta HTTP
        
        Args:
            response (requests.Response): Respuesta HTTP
        
        Returns:
            Dict[str, Any]: Datos parseados
        """
        try:
            # Intentar parsear como JSON
            json_data = response.json()
            
            # Añadir metadatos de la respuesta
            return {
                'data': json_data,
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'url': response.url,
                'elapsed': response.elapsed.total_seconds()
            }
            
        except json.JSONDecodeError:
            # Si no es JSON, devolver texto
            return {
                'data': response.text,
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'url': response.url,
                'elapsed': response.elapsed.total_seconds()
            }
    
    def paginated_get(self, endpoint: str, params: Dict[str, Any] = None,
                     page_param: str = 'page', per_page_param: str = 'per_page',
                     per_page: int = 100) -> List[Dict[str, Any]]:
        """
        Obtener todos los resultados de un endpoint paginado
        
        Args:
            endpoint (str): Endpoint de la API
            params (Dict[str, Any]): Parámetros base
            page_param (str): Nombre del parámetro de página
            per_page_param (str): Nombre del parámetro de items por página
            per_page (int): Items por página
        
        Returns:
            List[Dict[str, Any]]: Todos los resultados
        """
        all_results = []
        page = 1
        
        if params is None:
            params = {}
        
        while True:
            # Configurar parámetros de paginación
            page_params = params.copy()
            page_params[page_param] = page
            page_params[per_page_param] = per_page
            
            # Realizar request
            response = self.get(endpoint, page_params)
            
            # Extraer datos (esto puede variar según la API)
            if 'data' in response and 'data' in response['data']:
                page_data = response['data']['data']
            elif 'data' in response:
                page_data = response['data']
            else:
                page_data = response
            
            if not page_data:
                break
            
            all_results.extend(page_data)
            
            # Verificar si hay más páginas
            # (esto puede variar según la API)
            if len(page_data) < per_page:
                break
            
            page += 1
            
            # Seguridad: evitar bucles infinitos
            if page > 1000:
                print("Warning: Stopped pagination after 1000 pages")
                break
        
        return all_results
    
    def get_statistics(self) -> Dict[str, Any]:
        """Obtener estadísticas del cliente"""
        return {
            'total_requests': self.request_count,
            'successful_requests': self.success_count,
            'failed_requests': self.error_count,
            'success_rate': (self.success_count / self.request_count * 100) if self.request_count > 0 else 0,
            'base_url': self.base_url
        }
```

## 📋 Actividades del Día

### 🥉 **Nivel Principiante**
- [ ] Leer y escribir archivos de texto simples
- [ ] Procesar archivos CSV básicos
- [ ] Trabajar con JSON simple
- [ ] Hacer requests GET básicos a APIs públicas

### 🥈 **Nivel Intermedio**
- [ ] Crear sistema de backup y gestión de archivos
- [ ] Procesar CSV con validación y transformación de tipos
- [ ] Validar y transformar datos JSON complejos
- [ ] Implementar cliente API con autenticación y reintentos

### 🥇 **Nivel Avanzado**
- [ ] Desarrollar procesador de múltiples formatos de archivo
- [ ] Sistema de ETL (Extract, Transform, Load) completo
- [ ] Cliente API con paginación y rate limiting
- [ ] Integración de datos desde múltiples fuentes

### 💪 **Desafío Ninja**
- [ ] Framework de procesamiento de datos en tiempo real
- [ ] Sistema distribuido de scraping de datos
- [ ] API Gateway con caching y balanceeo
- [ ] Pipeline de datos con monitoreo y alertas

## 🎮 Ejercicios Prácticos

### 📁 [Exercises](./Exercises/README.md)
- **Exercise 1**: 📊 Sistema de Análisis de Datos CSV
- **Exercise 2**: 🌐 Aggregador de Noticias desde APIs
- **Exercise 3**: 💾 Sistema de Backup y Sincronización
- **Exercise 4**: 🔄 Pipeline de Procesamiento de Datos

### 🏆 [Daily Challenge](./DailyChallenge/README.md)
**🌍 Sistema de Monitoreo Climático Global**
- Integración con múltiples APIs meteorológicas
- Procesamiento de datos históricos desde CSV
- Almacenamiento y análisis en JSON
- Dashboard de reportes con alertas automáticas

## 📚 Herramientas y Mejores Prácticas

### 🛠️ Librerías Importantes

#### 📦 Requests y HTTP
```python
import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configuración avanzada de requests
def create_robust_session():
    session = requests.Session()
    
    # Estrategia de reintentos
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"],
        backoff_factor=1
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session
```

#### 📊 Pandas para Análisis de Datos
```python
import pandas as pd

# Lectura avanzada de CSV
def read_csv_advanced(filename, **kwargs):
    """Lectura robusta de CSV con pandas"""
    try:
        df = pd.read_csv(
            filename,
            encoding='utf-8-sig',  # Handle BOM
            na_values=['', 'NULL', 'null', 'N/A', 'n/a'],
            keep_default_na=True,
            **kwargs
        )
        return df
    except UnicodeDecodeError:
        # Intentar con diferentes encodings
        for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
            try:
                return pd.read_csv(filename, encoding=encoding, **kwargs)
            except UnicodeDecodeError:
                continue
        raise ValueError("Could not decode file with any encoding")
```

### 🔒 Seguridad y Mejores Prácticas

#### 🛡️ Manejo Seguro de APIs
```python
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class SecureAPIClient:
    """Cliente API con prácticas de seguridad"""
    
    def __init__(self):
        # Obtener credentials desde variables de entorno
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET')
        
        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")
    
    def make_secure_request(self, url, **kwargs):
        """Request con validación de SSL y timeouts"""
        return requests.get(
            url,
            timeout=(5, 30),  # (connect timeout, read timeout)
            verify=True,       # Verificar certificados SSL
            **kwargs
        )
```

#### 📁 Validación de Archivos
```python
import mimetypes
from pathlib import Path

def validate_file_upload(file_path, allowed_types=None, max_size_mb=10):
    """
    Validar archivo antes de procesarlo
    
    Args:
        file_path (str): Ruta del archivo
        allowed_types (list): Tipos MIME permitidos
        max_size_mb (int): Tamaño máximo en MB
    
    Returns:
        dict: Resultado de validación
    """
    path = Path(file_path)
    
    if not path.exists():
        return {'valid': False, 'error': 'File does not exist'}
    
    # Verificar tamaño
    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > max_size_mb:
        return {'valid': False, 'error': f'File too large: {size_mb:.2f}MB > {max_size_mb}MB'}
    
    # Verificar tipo MIME
    mime_type, _ = mimetypes.guess_type(str(path))
    if allowed_types and mime_type not in allowed_types:
        return {'valid': False, 'error': f'Invalid file type: {mime_type}'}
    
    return {'valid': True, 'mime_type': mime_type, 'size_mb': size_mb}
```

## ✅ Checklist de Progreso

### 🎯 Objetivos Completados
- [ ] Manejo eficiente de archivos con context managers
- [ ] Procesamiento de CSV con validación y transformación
- [ ] Serialización/deserialización JSON compleja
- [ ] Consumo de APIs REST con manejo de errores
- [ ] Implementación de reintentos y rate limiting
- [ ] Validación de datos y esquemas

### 🛠️ Habilidades Técnicas
- [ ] Uso de pathlib para operaciones de archivos
- [ ] Manejo de diferentes encodings y formatos
- [ ] Transformación y limpieza de datos
- [ ] Autenticación en APIs (Bearer, API Key, Basic)
- [ ] Paginación y manejo de grandes datasets
- [ ] Manejo de errores de red y I/O

### 🎨 Proyecto del Día
- [ ] Sistema completo de procesamiento de datos
- [ ] Integración con al menos 2 APIs externas
- [ ] Almacenamiento en múltiples formatos
- [ ] Validación y transformación de datos robusta
- [ ] Manejo de errores comprehensivo

## 🔍 Conceptos para Investigar

### 🤔 Preguntas de Reflexión
1. **¿Cuándo usar CSV vs JSON vs XML?**
2. **¿Cómo manejar archivos muy grandes que no caben en memoria?**
3. **¿Qué consideraciones de seguridad hay al descargar archivos?**
4. **¿Cómo implementar caché efectivo para APIs?**

### 🔬 Experimentos
- Comparar rendimiento de diferentes métodos de lectura de archivos
- Analizar el comportamiento de APIs con diferentes estrategias de reintentos
- Implementar compresión de datos en tiempo real
- Crear sistema de validación de datos personalizados

## 🚀 Preparación para Mañana

### 📖 Lecturas Recomendadas
- Patrones de diseño para aplicaciones complejas
- Gestión de proyectos de software
- Testing y documentación avanzada
- Deployment y distribución de aplicaciones

### 🎯 Próximos Temas
- **Day 5**: 🚀 Mini Project - Integración de todos los conceptos
- Arquitectura de aplicación completa
- Testing comprehensivo
- Documentación profesional
- Deployment y distribución

## 🆘 Troubleshooting

### ❌ Errores Comunes
1. **UnicodeDecodeError en archivos**
   ```python
   # ❌ Problema
   with open('file.txt', 'r') as f:  # Encoding por defecto
   
   # ✅ Solución
   with open('file.txt', 'r', encoding='utf-8-sig') as f:
   ```

2. **Timeouts en APIs**
   ```python
   # ❌ Problema
   response = requests.get(url)  # Sin timeout
   
   # ✅ Solución
   response = requests.get(url, timeout=(5, 30))
   ```

3. **Memory issues con archivos grandes**
   ```python
   # ❌ Problema
   content = file.read()  # Cargar todo en memoria
   
   # ✅ Solución
   for line in file:  # Procesar línea por línea
       process_line(line)
   ```

### 🔧 Tips de Debugging
- Usar logging en lugar de print para debugging
- Validar datos antes de procesarlos
- Implementar checkpoints en operaciones largas
- Monitorear uso de memoria y recursos

## 📚 Recursos Adicionales

### 🎥 Videos Recomendados
- "Python File I/O Best Practices"
- "Working with APIs in Python"
- "Data Processing Pipelines"

### 📖 Documentación
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Requests Documentation](https://docs.python-requests.org/)
- [JSON in Python](https://docs.python.org/3/library/json.html)

### 🛠️ Herramientas
- **httpx**: Cliente HTTP moderno alternativo a requests
- **aiofiles**: I/O de archivos asíncrono
- **jsonschema**: Validación de esquemas JSON
- **pandas**: Análisis de datos estructurados

---

**💡 Recuerda**: El manejo de datos externos requiere siempre validación, manejo de errores y consideraciones de rendimiento. Nunca asumas que los datos están en el formato correcto.

**🎯 Meta del día**: Crear un sistema robusto que pueda manejar datos del mundo real con todas sus irregularidades y problemas potenciales.
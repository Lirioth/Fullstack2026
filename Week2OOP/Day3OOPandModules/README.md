# 📦 Day 3 - OOP and Modules

## 🎯 Objetivos de Aprendizaje

Al finalizar este día, podrás:
- 📚 **Organizar código** en módulos y paquetes efectivamente
- 🏗️ **Estructurar proyectos** OOP de gran escala
- 🔗 **Importar y utilizar** módulos propios y de terceros
- 📖 **Documentar APIs** y crear interfaces claras
- 🧩 **Aplicar patrones** de diseño con módulos
- 🚀 **Distribuir código** como paquetes reutilizables

## 📚 Conceptos Clave

### 📁 Estructura de Módulos y Paquetes

#### 🔹 Módulo Simple
```python
# math_utils.py
"""
Módulo de utilidades matemáticas
Proporciona funciones para cálculos comunes
"""

class Calculator:
    """Calculadora avanzada con operaciones OOP"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self._record_operation("add", a, b, result)
        return result
    
    def _record_operation(self, op, a, b, result):
        self.history.append({
            'operation': op,
            'operands': (a, b),
            'result': result
        })
    
    def get_history(self):
        return self.history.copy()

def fibonacci(n):
    """Generar secuencia de Fibonacci hasta n términos"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

# Constantes del módulo
PI = 3.14159265359
E = 2.71828182846

# Variable de módulo
_module_version = "1.0.0"

def get_version():
    return _module_version
```

#### 📂 Paquete Completo
```
my_game_engine/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── engine.py
│   └── events.py
├── graphics/
│   ├── __init__.py
│   ├── renderer.py
│   └── sprites.py
├── audio/
│   ├── __init__.py
│   └── sound_manager.py
└── utils/
    ├── __init__.py
    ├── math_helpers.py
    └── file_helpers.py
```

### 🏗️ Archivo `__init__.py`

#### 📋 Configuración Básica
```python
# my_game_engine/__init__.py
"""
My Game Engine - A simple 2D game engine
Version: 1.0.0
Author: Developer
"""

# Importar clases principales para acceso directo
from .core.engine import GameEngine
from .graphics.renderer import Renderer
from .audio.sound_manager import SoundManager

# Definir qué se exporta cuando se hace "from my_game_engine import *"
__all__ = [
    'GameEngine',
    'Renderer', 
    'SoundManager',
    'create_game',
    'VERSION'
]

# Metadatos del paquete
VERSION = "1.0.0"
AUTHOR = "Developer Team"
EMAIL = "dev@gameengine.com"

# Función de conveniencia
def create_game(title="My Game", width=800, height=600):
    """
    Función de conveniencia para crear un juego rápidamente
    
    Args:
        title (str): Título del juego
        width (int): Ancho de la ventana
        height (int): Alto de la ventana
    
    Returns:
        GameEngine: Instancia configurada del motor de juego
    """
    engine = GameEngine(title, width, height)
    return engine

# Configuración al importar el paquete
print(f"Game Engine v{VERSION} loaded successfully!")
```

#### 🔧 Configuración Avanzada
```python
# my_game_engine/core/__init__.py
"""
Core module - Motor principal del juego
"""

from .engine import GameEngine, GameState
from .events import EventManager, Event

# Re-exportar para facilitar importaciones
__all__ = ['GameEngine', 'GameState', 'EventManager', 'Event']

# Configuración específica del módulo core
CORE_VERSION = "1.0.0"
DEBUG_MODE = False

def enable_debug():
    """Habilitar modo debug para el core"""
    global DEBUG_MODE
    DEBUG_MODE = True
    print("🐛 Core Debug Mode enabled")

def disable_debug():
    """Deshabilitar modo debug"""
    global DEBUG_MODE
    DEBUG_MODE = False
    print("✅ Core Debug Mode disabled")
```

### 🔗 Patrones de Importación

#### 📥 Importaciones Básicas
```python
# Importar módulo completo
import math_utils
calculator = math_utils.Calculator()

# Importar elementos específicos
from math_utils import Calculator, fibonacci

# Importar con alias
from math_utils import Calculator as Calc
import math_utils as math

# Importar todo (usar con cuidado)
from math_utils import *
```

#### 🎯 Importaciones Avanzadas
```python
# Importación condicional
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

class AdvancedCalculator:
    def __init__(self):
        if not HAS_NUMPY:
            raise ImportError("NumPy required for AdvancedCalculator")
        self.np = np

# Importación dinámica
def load_plugin(plugin_name):
    """Cargar plugin dinámicamente"""
    import importlib
    
    try:
        plugin_module = importlib.import_module(f"plugins.{plugin_name}")
        return plugin_module
    except ImportError as e:
        print(f"Failed to load plugin {plugin_name}: {e}")
        return None

# Importación relativa
from .core import GameEngine  # Relativa al paquete actual
from ..utils import math_helpers  # Subir un nivel y luego bajar
```

### 🧩 Patrones de Diseño con Módulos

#### 🏭 Factory Pattern
```python
# factory/shape_factory.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class ShapeFactory:
    """Factory para crear diferentes formas"""
    
    _shapes = {
        'circle': Circle,
        'rectangle': Rectangle
    }
    
    @classmethod
    def create_shape(cls, shape_type, **kwargs):
        """
        Crear forma según el tipo especificado
        
        Args:
            shape_type (str): Tipo de forma ('circle', 'rectangle')
            **kwargs: Parámetros específicos de la forma
        
        Returns:
            Shape: Instancia de la forma creada
        """
        if shape_type not in cls._shapes:
            raise ValueError(f"Unknown shape type: {shape_type}")
        
        shape_class = cls._shapes[shape_type]
        return shape_class(**kwargs)
    
    @classmethod
    def register_shape(cls, name, shape_class):
        """Registrar nueva forma en el factory"""
        cls._shapes[name] = shape_class
    
    @classmethod
    def available_shapes(cls):
        """Obtener lista de formas disponibles"""
        return list(cls._shapes.keys())
```

#### 🔍 Observer Pattern
```python
# patterns/observer.py
from abc import ABC, abstractmethod
from typing import List, Any

class Observer(ABC):
    """Interface para observadores"""
    
    @abstractmethod
    def update(self, subject: 'Subject', event_data: Any):
        """Método llamado cuando el sujeto notifica cambios"""
        pass

class Subject:
    """Sujeto que puede ser observado"""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None
    
    def attach(self, observer: Observer):
        """Agregar observador"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Remover observador"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_data: Any = None):
        """Notificar a todos los observadores"""
        for observer in self._observers:
            observer.update(self, event_data)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify({'state_changed': value})

# Ejemplo de uso del patrón Observer
class EmailNotifier(Observer):
    def update(self, subject, event_data):
        print(f"📧 Email notification: {event_data}")

class SMSNotifier(Observer):
    def update(self, subject, event_data):
        print(f"📱 SMS notification: {event_data}")

class UserAccount(Subject):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        self.notify({
            'action': 'deposit',
            'amount': amount,
            'new_balance': self.balance
        })
```

### 📖 Documentación de Módulos

#### 📝 Docstrings Completos
```python
# documentation_example.py
"""
Módulo de gestión de usuarios
=============================

Este módulo proporciona clases y funciones para gestionar usuarios
en una aplicación web.

Ejemplo de uso básico:
    >>> from user_management import UserManager, User
    >>> manager = UserManager()
    >>> user = manager.create_user("john_doe", "john@example.com")
    >>> print(user.username)
    john_doe

Clases principales:
    User: Representa un usuario individual
    UserManager: Gestiona operaciones CRUD de usuarios
    UserGroup: Representa grupos de usuarios

Funciones utilitarias:
    validate_email: Valida formato de email
    hash_password: Encripta contraseñas
    
Author: Development Team
Version: 2.1.0
Since: 1.0.0
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
import re
import hashlib

class User:
    """
    Representa un usuario en el sistema
    
    Esta clase encapsula toda la información y comportamiento
    relacionado con un usuario individual.
    
    Attributes:
        username (str): Nombre único del usuario
        email (str): Dirección de correo electrónico
        created_at (datetime): Fecha de creación de la cuenta
        is_active (bool): Estado activo del usuario
        
    Example:
        >>> user = User("john_doe", "john@example.com")
        >>> user.username
        'john_doe'
        >>> user.is_active
        True
    
    Note:
        Los usernames deben ser únicos en todo el sistema.
        Los emails deben tener formato válido.
    """
    
    def __init__(self, username: str, email: str, password: str):
        """
        Inicializar nuevo usuario
        
        Args:
            username (str): Nombre único del usuario (3-20 caracteres)
            email (str): Email válido del usuario
            password (str): Contraseña en texto plano (será encriptada)
            
        Raises:
            ValueError: Si username o email no son válidos
            TypeError: Si los parámetros no son strings
            
        Example:
            >>> user = User("alice", "alice@example.com", "secret123")
        """
        if not isinstance(username, str) or not isinstance(email, str):
            raise TypeError("Username y email deben ser strings")
        
        if len(username) < 3 or len(username) > 20:
            raise ValueError("Username debe tener entre 3 y 20 caracteres")
        
        if not self._validate_email(email):
            raise ValueError("Email no tiene formato válido")
        
        self.username = username
        self.email = email
        self._password_hash = self._hash_password(password)
        self.created_at = datetime.now()
        self.is_active = True
        self._login_attempts = 0
    
    def _validate_email(self, email: str) -> bool:
        """
        Validar formato de email
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si el email es válido, False en caso contrario
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _hash_password(self, password: str) -> str:
        """
        Encriptar contraseña usando SHA-256
        
        Args:
            password (str): Contraseña en texto plano
            
        Returns:
            str: Hash de la contraseña
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password: str) -> bool:
        """
        Verificar si la contraseña proporcionada es correcta
        
        Args:
            password (str): Contraseña a verificar
            
        Returns:
            bool: True si la contraseña es correcta
            
        Example:
            >>> user = User("alice", "alice@example.com", "secret123")
            >>> user.verify_password("secret123")
            True
            >>> user.verify_password("wrong_password")
            False
        """
        return self._password_hash == self._hash_password(password)
    
    def deactivate(self) -> None:
        """
        Desactivar cuenta de usuario
        
        Una vez desactivada, el usuario no puede iniciar sesión.
        
        Example:
            >>> user.deactivate()
            >>> user.is_active
            False
        """
        self.is_active = False
    
    def __str__(self) -> str:
        """Representación string del usuario"""
        return f"User(username='{self.username}', email='{self.email}')"
    
    def __repr__(self) -> str:
        """Representación técnica del usuario"""
        return f"User('{self.username}', '{self.email}', created_at={self.created_at})"
```

## 📋 Actividades del Día

### 🥉 **Nivel Principiante**
- [ ] Crear módulo de utilidades matemáticas con clases y funciones
- [ ] Organizar código en múltiples archivos .py
- [ ] Implementar importaciones básicas entre módulos
- [ ] Documentar módulos con docstrings

### 🥈 **Nivel Intermedio**
- [ ] Crear paquete completo con estructura de directorios
- [ ] Implementar patrón Factory usando módulos
- [ ] Configurar `__init__.py` para exposición de API
- [ ] Manear importaciones condicionales y dinámicas

### 🥇 **Nivel Avanzado**
- [ ] Desarrollar sistema de plugins cargables dinámicamente
- [ ] Implementar patrón Observer distribuido en módulos
- [ ] Crear documentación automática con Sphinx
- [ ] Sistema de configuración multi-módulo

### 💪 **Desafío Ninja**
- [ ] Framework OOP modular extensible
- [ ] Sistema de hooks y middlewares
- [ ] Distribución como paquete PyPI
- [ ] Testing automático multi-módulo

## 🎮 Ejercicios Prácticos

### 📁 [Exercises](./Exercises/README.md)
- **Exercise 1**: 🧮 Sistema de Calculadora Modular
- **Exercise 2**: 🎮 Motor de Juegos con Arquitectura Modular
- **Exercise 3**: 🏪 Sistema de E-commerce Multi-módulo
- **Exercise 4**: 🔌 Framework de Plugins Dinámicos

### 🏆 [Daily Challenge](./DailyChallenge/README.md)
**🏗️ Sistema de Gestión de Biblioteca Digital**
- Arquitectura modular completa
- Múltiples tipos de recursos (libros, revistas, multimedia)
- Sistema de préstamos y reservas
- Gestión de usuarios y permisos

## 📚 Herramientas y Mejores Prácticas

### 🛠️ Herramientas de Desarrollo

#### 📦 Gestión de Dependencias
```python
# requirements.txt
requests>=2.25.0
numpy>=1.21.0
pytest>=6.0.0
sphinx>=4.0.0

# setup.py para distribución
from setuptools import setup, find_packages

setup(
    name="my-library",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.21.0"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
```

#### 🧪 Testing Multi-módulo
```python
# tests/test_math_utils.py
import unittest
import sys
import os

# Añadir el directorio padre al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import Calculator, fibonacci

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_history_tracking(self):
        self.calc.add(2, 3)
        self.calc.add(5, 7)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        result = fibonacci(5)
        expected = [0, 1, 1, 2, 3]
        self.assertEqual(result, expected)
    
    def test_fibonacci_edge_cases(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])

if __name__ == '__main__':
    unittest.main()
```

### 📖 Documentación Automática

#### 🔧 Configuración Sphinx
```python
# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'My Library'
copyright = '2024, Your Name'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings para Google/NumPy docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
```

## ✅ Checklist de Progreso

### 🎯 Objetivos Completados
- [ ] Comprendo la diferencia entre módulos y paquetes
- [ ] Puedo estructurar proyectos grandes con múltiples módulos
- [ ] Sé configurar `__init__.py` efectivamente
- [ ] Manejo importaciones relativas y absolutas
- [ ] Implemento patrones de diseño usando módulos
- [ ] Documento código siguiendo estándares PEP

### 🛠️ Habilidades Técnicas
- [ ] Creación de paquetes distribuibles
- [ ] Gestión de dependencias con requirements.txt
- [ ] Testing multi-módulo con unittest/pytest
- [ ] Documentación automática con Sphinx
- [ ] Manejo de namespace packages
- [ ] Implementación de plugins dinámicos

### 🎨 Proyecto del Día
- [ ] Arquitectura modular bien diseñada
- [ ] Separación clara de responsabilidades
- [ ] APIs bien documentadas
- [ ] Tests comprehensivos
- [ ] Distribución como paquete

## 🔍 Conceptos para Investigar

### 🤔 Preguntas de Reflexión
1. **¿Cuándo crear un módulo vs un paquete?**
2. **¿Cómo manejar dependencias circulares?**
3. **¿Qué es el namespace pollution y cómo evitarlo?**
4. **¿Cuándo usar importaciones relativas vs absolutas?**

### 🔬 Experimentos
- Comparar rendimiento de diferentes estrategias de importación
- Analizar el module search path de Python
- Implementar diferentes patrones de singleton en módulos
- Crear sistema de configuration management

## 🚀 Preparación para Mañana

### 📖 Lecturas Recomendadas
- File I/O y manejo de archivos
- JSON y serialización de datos
- APIs REST y requests
- Manejo de errores y excepciones

### 🎯 Próximos Temas
- **Day 4**: 📄 Python File I/O, JSON and API
- Lectura y escritura de archivos
- Procesamiento de JSON
- Consumo de APIs REST
- Manejo de datos externos

## 🆘 Troubleshooting

### ❌ Errores Comunes
1. **ModuleNotFoundError**
   ```python
   # ❌ Problema
   # Archivo no en el path o nombre incorrecto
   
   # ✅ Solución
   import sys
   sys.path.append('/path/to/module')
   # O usar PYTHONPATH
   ```

2. **Circular imports**
   ```python
   # ❌ Problema
   # module_a.py imports module_b
   # module_b.py imports module_a
   
   # ✅ Solución
   # Importar dentro de funciones o usar importlib
   def get_dependency():
       from . import module_b
       return module_b.function()
   ```

3. **__init__.py mal configurado**
   ```python
   # ❌ Problema
   # __init__.py vacío o mal estructurado
   
   # ✅ Solución
   from .module import Class
   __all__ = ['Class']
   ```

### 🔧 Tips de Debugging
- Usar `python -m module` para ejecutar módulos
- `__file__` y `__name__` para debugging de paths
- `importlib.reload()` para recargar módulos durante desarrollo
- `sys.modules` para ver módulos cargados

## 📚 Recursos Adicionales

### 🎥 Videos Recomendados
- "Python Modules and Packages"
- "Advanced Python Module Systems"
- "Building Distributable Python Packages"

### 📖 Documentación
- [Python Module Tutorial](https://docs.python.org/3/tutorial/modules.html)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

### 🛠️ Herramientas
- **setuptools**: Para crear paquetes distribuibles
- **pip**: Gestión de paquetes
- **virtualenv**: Entornos virtuales
- **sphinx**: Documentación automática

---

**💡 Recuerda**: Un código bien organizado en módulos es más fácil de mantener, testear y escalar. Piensa en la separación de responsabilidades.

**🎯 Meta del día**: Crear un sistema modular que demuestre organización profesional de código y mejores prácticas de desarrollo.
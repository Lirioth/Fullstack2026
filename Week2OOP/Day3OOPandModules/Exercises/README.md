# 🛠️ Day 3 Exercises - OOP and Modules

## 🎯 Objetivos de los Ejercicios

Estos ejercicios te ayudarán a dominar:
- 📦 **Organización modular**: Estructurar código en módulos y paquetes
- 🏗️ **Arquitectura de software**: Diseñar sistemas escalables y mantenibles
- 📖 **Documentación**: Crear APIs claras y bien documentadas
- 🔗 **Patrones de diseño**: Implementar patrones usando estructura modular
- 🧪 **Testing**: Probar sistemas multi-módulo efectivamente

---

## 🥉 Exercise 1: Sistema de Calculadora Modular

### 🧮 Descripción
Desarrolla un sistema de calculadora completo organizado en módulos separados, cada uno con responsabilidades específicas.

### 📋 Estructura del Proyecto
```
calculator_system/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── basic_operations.py
│   ├── advanced_operations.py
│   └── calculator.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── formatters.py
├── history/
│   ├── __init__.py
│   ├── history_manager.py
│   └── exporters.py
├── plugins/
│   ├── __init__.py
│   ├── scientific.py
│   └── financial.py
└── tests/
    ├── test_basic_operations.py
    ├── test_calculator.py
    └── test_history.py
```

### 🔧 Implementación Requerida

#### 1. **Módulo `core/basic_operations.py`**
```python
"""
Operaciones básicas de calculadora
Proporciona funciones para operaciones aritméticas básicas
"""

from typing import Union, List
from decimal import Decimal, InvalidOperation

Number = Union[int, float, Decimal]

class MathError(Exception):
    """Excepción personalizada para errores matemáticos"""
    pass

def add(a: Number, b: Number) -> Number:
    """
    Sumar dos números
    
    Args:
        a (Number): Primer número
        b (Number): Segundo número
    
    Returns:
        Number: Suma de a + b
        
    Example:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.7)
        6.2
    """
    try:
        return Decimal(str(a)) + Decimal(str(b))
    except InvalidOperation:
        raise MathError(f"Cannot add {a} and {b}")

def subtract(a: Number, b: Number) -> Number:
    """Restar b de a"""
    try:
        return Decimal(str(a)) - Decimal(str(b))
    except InvalidOperation:
        raise MathError(f"Cannot subtract {b} from {a}")

def multiply(a: Number, b: Number) -> Number:
    """Multiplicar dos números"""
    try:
        return Decimal(str(a)) * Decimal(str(b))
    except InvalidOperation:
        raise MathError(f"Cannot multiply {a} and {b}")

def divide(a: Number, b: Number) -> Number:
    """
    Dividir a entre b
    
    Raises:
        MathError: Si b es cero o la operación es inválida
    """
    if b == 0:
        raise MathError("Division by zero is not allowed")
    
    try:
        return Decimal(str(a)) / Decimal(str(b))
    except InvalidOperation:
        raise MathError(f"Cannot divide {a} by {b}")

def power(base: Number, exponent: Number) -> Number:
    """Calcular base elevado a exponent"""
    try:
        return Decimal(str(base)) ** Decimal(str(exponent))
    except InvalidOperation:
        raise MathError(f"Cannot calculate {base}^{exponent}")

# Diccionario de operaciones disponibles
OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '^': power
}

def get_available_operations() -> List[str]:
    """Obtener lista de operaciones disponibles"""
    return list(OPERATIONS.keys())
```

#### 2. **Módulo `core/advanced_operations.py`**
```python
"""
Operaciones avanzadas de calculadora
Incluye funciones trigonométricas, logarítmicas y estadísticas
"""

import math
from typing import List
from decimal import Decimal
from .basic_operations import Number, MathError

def sqrt(n: Number) -> Number:
    """Calcular raíz cuadrada"""
    if n < 0:
        raise MathError("Cannot calculate square root of negative number")
    return Decimal(str(math.sqrt(float(n))))

def factorial(n: int) -> int:
    """Calcular factorial de n"""
    if not isinstance(n, int) or n < 0:
        raise MathError("Factorial is only defined for non-negative integers")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sin(angle: Number, degrees: bool = False) -> Number:
    """Calcular seno del ángulo"""
    angle_float = float(angle)
    if degrees:
        angle_float = math.radians(angle_float)
    return Decimal(str(math.sin(angle_float)))

def cos(angle: Number, degrees: bool = False) -> Number:
    """Calcular coseno del ángulo"""
    angle_float = float(angle)
    if degrees:
        angle_float = math.radians(angle_float)
    return Decimal(str(math.cos(angle_float)))

def tan(angle: Number, degrees: bool = False) -> Number:
    """Calcular tangente del ángulo"""
    angle_float = float(angle)
    if degrees:
        angle_float = math.radians(angle_float)
    return Decimal(str(math.tan(angle_float)))

def log(n: Number, base: Number = math.e) -> Number:
    """Calcular logaritmo de n en base especificada"""
    if n <= 0:
        raise MathError("Logarithm is only defined for positive numbers")
    if base <= 0 or base == 1:
        raise MathError("Logarithm base must be positive and not equal to 1")
    
    return Decimal(str(math.log(float(n), float(base))))

def mean(numbers: List[Number]) -> Number:
    """Calcular promedio de una lista de números"""
    if not numbers:
        raise MathError("Cannot calculate mean of empty list")
    
    total = sum(Decimal(str(num)) for num in numbers)
    return total / Decimal(str(len(numbers)))

def median(numbers: List[Number]) -> Number:
    """Calcular mediana de una lista de números"""
    if not numbers:
        raise MathError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (Decimal(str(mid1)) + Decimal(str(mid2))) / Decimal('2')
    else:
        return Decimal(str(sorted_numbers[n // 2]))

# Diccionario de operaciones avanzadas
ADVANCED_OPERATIONS = {
    'sqrt': sqrt,
    'factorial': factorial,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'log': log,
    'mean': mean,
    'median': median
}
```

#### 3. **Módulo `utils/validators.py`**
```python
"""
Validadores para entradas de calculadora
"""

import re
from typing import Union, List
from decimal import Decimal, InvalidOperation

def is_valid_number(value: str) -> bool:
    """
    Verificar si una cadena representa un número válido
    
    Args:
        value (str): Cadena a validar
    
    Returns:
        bool: True si es un número válido
    """
    try:
        Decimal(value)
        return True
    except (InvalidOperation, ValueError):
        return False

def is_valid_expression(expression: str) -> bool:
    """
    Verificar si una expresión matemática es válida
    
    Args:
        expression (str): Expresión a validar
    
    Returns:
        bool: True si la expresión es válida
    """
    # Eliminar espacios
    expression = expression.replace(' ', '')
    
    # Verificar caracteres permitidos
    allowed_chars = r'^[0-9+\-*/().^]+$'
    if not re.match(allowed_chars, expression):
        return False
    
    # Verificar balanceado de paréntesis
    return _check_balanced_parentheses(expression)

def _check_balanced_parentheses(expression: str) -> bool:
    """Verificar que los paréntesis estén balanceados"""
    count = 0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def validate_operation_input(operation: str, operands: List[Union[str, float, int]]) -> bool:
    """
    Validar entrada para una operación específica
    
    Args:
        operation (str): Nombre de la operación
        operands (List): Lista de operandos
    
    Returns:
        bool: True si la entrada es válida para la operación
    """
    if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
        return len(operands) == 2 and all(is_valid_number(str(op)) for op in operands)
    
    elif operation in ['sqrt', 'sin', 'cos', 'tan', 'log']:
        return len(operands) >= 1 and is_valid_number(str(operands[0]))
    
    elif operation == 'factorial':
        if len(operands) != 1:
            return False
        try:
            n = int(operands[0])
            return n >= 0
        except (ValueError, TypeError):
            return False
    
    elif operation in ['mean', 'median']:
        return len(operands) > 0 and all(is_valid_number(str(op)) for op in operands)
    
    return False

class ValidationError(Exception):
    """Excepción para errores de validación"""
    pass

def validate_and_convert(value: str) -> Decimal:
    """
    Validar y convertir string a Decimal
    
    Args:
        value (str): Valor a convertir
    
    Returns:
        Decimal: Valor convertido
    
    Raises:
        ValidationError: Si el valor no es válido
    """
    if not is_valid_number(value):
        raise ValidationError(f"'{value}' is not a valid number")
    
    return Decimal(value)
```

#### 4. **Módulo `history/history_manager.py`**
```python
"""
Gestor de historial de operaciones
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import json
from pathlib import Path

class CalculationRecord:
    """Registro de una operación de calculadora"""
    
    def __init__(self, operation: str, operands: List[Any], result: Any, timestamp: Optional[datetime] = None):
        self.operation = operation
        self.operands = operands
        self.result = result
        self.timestamp = timestamp or datetime.now()
        self.id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generar ID único para el registro"""
        return f"{self.timestamp.strftime('%Y%m%d_%H%M%S')}_{id(self)}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir registro a diccionario"""
        return {
            'id': self.id,
            'operation': self.operation,
            'operands': [str(op) for op in self.operands],
            'result': str(self.result),
            'timestamp': self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CalculationRecord':
        """Crear registro desde diccionario"""
        record = cls(
            operation=data['operation'],
            operands=data['operands'],
            result=data['result'],
            timestamp=datetime.fromisoformat(data['timestamp'])
        )
        record.id = data['id']
        return record
    
    def __str__(self) -> str:
        operands_str = ', '.join(str(op) for op in self.operands)
        return f"{self.operation}({operands_str}) = {self.result}"

class HistoryManager:
    """Gestor del historial de cálculos"""
    
    def __init__(self, max_records: int = 1000):
        self.max_records = max_records
        self._records: List[CalculationRecord] = []
        self._current_session_records: List[CalculationRecord] = []
    
    def add_record(self, operation: str, operands: List[Any], result: Any) -> CalculationRecord:
        """
        Añadir nuevo registro al historial
        
        Args:
            operation (str): Nombre de la operación
            operands (List[Any]): Operandos utilizados
            result (Any): Resultado de la operación
        
        Returns:
            CalculationRecord: Registro creado
        """
        record = CalculationRecord(operation, operands, result)
        
        self._records.append(record)
        self._current_session_records.append(record)
        
        # Mantener límite de registros
        if len(self._records) > self.max_records:
            self._records.pop(0)
        
        return record
    
    def get_recent_records(self, count: int = 10) -> List[CalculationRecord]:
        """Obtener registros más recientes"""
        return self._records[-count:] if self._records else []
    
    def get_session_records(self) -> List[CalculationRecord]:
        """Obtener registros de la sesión actual"""
        return self._current_session_records.copy()
    
    def search_records(self, operation: str = None, date_from: datetime = None, date_to: datetime = None) -> List[CalculationRecord]:
        """
        Buscar registros con filtros
        
        Args:
            operation (str, optional): Filtrar por operación
            date_from (datetime, optional): Fecha de inicio
            date_to (datetime, optional): Fecha de fin
        
        Returns:
            List[CalculationRecord]: Registros que coinciden con los filtros
        """
        filtered_records = self._records.copy()
        
        if operation:
            filtered_records = [r for r in filtered_records if r.operation == operation]
        
        if date_from:
            filtered_records = [r for r in filtered_records if r.timestamp >= date_from]
        
        if date_to:
            filtered_records = [r for r in filtered_records if r.timestamp <= date_to]
        
        return filtered_records
    
    def clear_history(self) -> None:
        """Limpiar todo el historial"""
        self._records.clear()
        self._current_session_records.clear()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Obtener estadísticas del historial"""
        if not self._records:
            return {"total_operations": 0}
        
        operation_counts = {}
        for record in self._records:
            operation_counts[record.operation] = operation_counts.get(record.operation, 0) + 1
        
        return {
            "total_operations": len(self._records),
            "session_operations": len(self._current_session_records),
            "most_used_operation": max(operation_counts, key=operation_counts.get),
            "operation_counts": operation_counts,
            "first_operation": self._records[0].timestamp.isoformat(),
            "last_operation": self._records[-1].timestamp.isoformat()
        }
    
    def save_to_file(self, filename: str) -> None:
        """Guardar historial en archivo JSON"""
        data = {
            "records": [record.to_dict() for record in self._records],
            "metadata": {
                "total_records": len(self._records),
                "export_timestamp": datetime.now().isoformat()
            }
        }
        
        Path(filename).write_text(json.dumps(data, indent=2, ensure_ascii=False))
    
    def load_from_file(self, filename: str) -> None:
        """Cargar historial desde archivo JSON"""
        try:
            data = json.loads(Path(filename).read_text())
            self._records = [
                CalculationRecord.from_dict(record_data) 
                for record_data in data["records"]
            ]
            self._current_session_records.clear()
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Error loading history file: {e}")
```

### ✅ Criterios de Evaluación
- [ ] Estructura de módulos correcta con `__init__.py`
- [ ] Separación clara de responsabilidades
- [ ] Documentación completa con docstrings
- [ ] Manejo de errores personalizado
- [ ] Importaciones relativas funcionando
- [ ] Sistema de historial funcionando completamente

---

## 🥈 Exercise 2: Motor de Juegos con Arquitectura Modular

### 🎮 Descripción
Desarrolla un motor de juegos 2D simple pero completo, organizado en una arquitectura modular escalable.

### 📋 Estructura del Proyecto
```
game_engine/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── engine.py
│   ├── game_state.py
│   └── scene_manager.py
├── graphics/
│   ├── __init__.py
│   ├── renderer.py
│   ├── sprite.py
│   └── animation.py
├── input/
│   ├── __init__.py
│   ├── keyboard.py
│   └── mouse.py
├── physics/
│   ├── __init__.py
│   ├── collision.py
│   └── vector2d.py
├── audio/
│   ├── __init__.py
│   └── sound_manager.py
├── utils/
│   ├── __init__.py
│   ├── timer.py
│   └── config.py
└── examples/
    ├── pong.py
    └── space_invaders.py
```

### 🔧 Implementación Requerida

#### 1. **Configuración Principal `__init__.py`**
```python
"""
Simple 2D Game Engine
====================

Un motor de juegos 2D simple y modular para desarrollo rápido de juegos.

Ejemplo básico:
    >>> from game_engine import GameEngine, Sprite
    >>> engine = GameEngine("My Game", 800, 600)
    >>> sprite = Sprite("player.png", 100, 100)
    >>> engine.run()

Módulos principales:
    core: Motor principal y gestión de estados
    graphics: Renderizado y sprites
    input: Manejo de entrada de usuario
    physics: Física básica y colisiones
    audio: Gestión de sonido
    utils: Utilidades y configuración
"""

# Importaciones principales para facilitar el uso
from .core.engine import GameEngine
from .core.game_state import GameState
from .graphics.sprite import Sprite
from .graphics.renderer import Renderer
from .input.keyboard import KeyboardManager
from .input.mouse import MouseManager
from .physics.vector2d import Vector2D
from .physics.collision import CollisionDetector
from .utils.timer import Timer
from .utils.config import Config

# Metadatos del paquete
__version__ = "1.0.0"
__author__ = "Game Engine Team"
__license__ = "MIT"

# API principal disponible
__all__ = [
    'GameEngine',
    'GameState', 
    'Sprite',
    'Renderer',
    'KeyboardManager',
    'MouseManager',
    'Vector2D',
    'CollisionDetector',
    'Timer',
    'Config'
]

# Función de conveniencia
def create_game(title="My Game", width=800, height=600, fps=60):
    """
    Crear un juego rápidamente con configuración básica
    
    Args:
        title (str): Título de la ventana
        width (int): Ancho de la ventana
        height (int): Alto de la ventana
        fps (int): Frames por segundo objetivo
    
    Returns:
        GameEngine: Instancia configurada del motor
    """
    config = Config()
    config.set('window.title', title)
    config.set('window.width', width)
    config.set('window.height', height)
    config.set('engine.target_fps', fps)
    
    return GameEngine(config)

# Configuración inicial
print(f"🎮 Game Engine v{__version__} loaded!")
```

#### 2. **Core Engine `core/engine.py`**
```python
"""
Motor principal del juego
Gestiona el bucle principal, estados y coordinación entre sistemas
"""

import time
from typing import Optional, Dict, Any
from ..graphics.renderer import Renderer
from ..input.keyboard import KeyboardManager
from ..input.mouse import MouseManager
from ..audio.sound_manager import SoundManager
from ..utils.timer import Timer
from ..utils.config import Config
from .game_state import GameState

class GameEngine:
    """
    Motor principal del juego
    
    Coordina todos los sistemas del motor y maneja el bucle principal
    del juego, incluyendo actualización y renderizado.
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        Inicializar el motor de juego
        
        Args:
            config (Config, optional): Configuración del motor
        """
        self.config = config or Config()
        
        # Sistemas principales
        self.renderer = Renderer(self.config)
        self.keyboard = KeyboardManager()
        self.mouse = MouseManager()
        self.sound_manager = SoundManager(self.config)
        self.timer = Timer()
        
        # Estados del juego
        self._current_state: Optional[GameState] = None
        self._state_stack: List[GameState] = []
        
        # Control del bucle principal
        self._running = False
        self._target_fps = self.config.get('engine.target_fps', 60)
        self._frame_time = 1.0 / self._target_fps
        
        # Estadísticas
        self._frame_count = 0
        self._fps_counter = 0
        self._last_fps_update = 0
        
        self._initialize_systems()
    
    def _initialize_systems(self) -> None:
        """Inicializar todos los sistemas del motor"""
        try:
            self.renderer.initialize()
            self.keyboard.initialize()
            self.mouse.initialize()
            self.sound_manager.initialize()
            print("✅ All game engine systems initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing game engine: {e}")
            raise
    
    def push_state(self, state: GameState) -> None:
        """
        Añadir estado al stack y activarlo
        
        Args:
            state (GameState): Estado a añadir
        """
        if self._current_state:
            self._current_state.pause()
            self._state_stack.append(self._current_state)
        
        self._current_state = state
        state.engine = self
        state.enter()
    
    def pop_state(self) -> Optional[GameState]:
        """
        Remover estado actual y activar el anterior
        
        Returns:
            GameState: Estado removido, None si no había estados
        """
        if not self._current_state:
            return None
        
        old_state = self._current_state
        old_state.exit()
        
        if self._state_stack:
            self._current_state = self._state_stack.pop()
            self._current_state.resume()
        else:
            self._current_state = None
        
        return old_state
    
    def change_state(self, new_state: GameState) -> None:
        """
        Cambiar completamente al nuevo estado
        
        Args:
            new_state (GameState): Nuevo estado
        """
        if self._current_state:
            self._current_state.exit()
        
        self._state_stack.clear()
        self._current_state = new_state
        new_state.engine = self
        new_state.enter()
    
    def run(self) -> None:
        """Ejecutar el bucle principal del juego"""
        if not self._current_state:
            raise RuntimeError("No game state set. Use push_state() to add a state.")
        
        self._running = True
        last_time = time.time()
        accumulator = 0.0
        
        print(f"🚀 Game engine starting (Target FPS: {self._target_fps})")
        
        try:
            while self._running:
                current_time = time.time()
                frame_time = current_time - last_time
                last_time = current_time
                
                accumulator += frame_time
                
                # Procesar entrada
                self._handle_input()
                
                # Actualizar con timestep fijo
                while accumulator >= self._frame_time:
                    self._update(self._frame_time)
                    accumulator -= self._frame_time
                
                # Renderizar
                self._render()
                
                # Actualizar estadísticas
                self._update_statistics()
                
                # Control de FPS
                self._limit_fps(current_time)
                
        except KeyboardInterrupt:
            print("\\n🛑 Game interrupted by user")
        except Exception as e:
            print(f"❌ Game error: {e}")
            raise
        finally:
            self._cleanup()
    
    def _handle_input(self) -> None:
        """Procesar entrada de usuario"""
        self.keyboard.update()
        self.mouse.update()
        
        if self._current_state:
            self._current_state.handle_input(self.keyboard, self.mouse)
    
    def _update(self, delta_time: float) -> None:
        """
        Actualizar lógica del juego
        
        Args:
            delta_time (float): Tiempo transcurrido desde la última actualización
        """
        if self._current_state:
            self._current_state.update(delta_time)
    
    def _render(self) -> None:
        """Renderizar frame actual"""
        self.renderer.clear()
        
        if self._current_state:
            self._current_state.render(self.renderer)
        
        # Renderizar FPS si está habilitado
        if self.config.get('debug.show_fps', False):
            self._render_fps()
        
        self.renderer.present()
    
    def _render_fps(self) -> None:
        """Renderizar contador de FPS"""
        fps_text = f"FPS: {self._fps_counter}"
        # Implementar renderizado de texto aquí
        pass
    
    def _update_statistics(self) -> None:
        """Actualizar estadísticas del motor"""
        self._frame_count += 1
        
        current_time = time.time()
        if current_time - self._last_fps_update >= 1.0:
            self._fps_counter = self._frame_count
            self._frame_count = 0
            self._last_fps_update = current_time
    
    def _limit_fps(self, frame_start_time: float) -> None:
        """Limitar FPS si es necesario"""
        frame_end_time = time.time()
        frame_duration = frame_end_time - frame_start_time
        
        if frame_duration < self._frame_time:
            sleep_time = self._frame_time - frame_duration
            time.sleep(sleep_time)
    
    def _cleanup(self) -> None:
        """Limpiar recursos al cerrar"""
        print("🧹 Cleaning up game engine...")
        
        if self._current_state:
            self._current_state.exit()
        
        self.renderer.cleanup()
        self.sound_manager.cleanup()
        
        print("✅ Game engine cleanup complete")
    
    def quit(self) -> None:
        """Solicitar cierre del motor"""
        self._running = False
    
    # Propiedades de acceso
    @property
    def running(self) -> bool:
        return self._running
    
    @property
    def current_state(self) -> Optional[GameState]:
        return self._current_state
    
    @property
    def fps(self) -> int:
        return self._fps_counter
    
    def get_system_info(self) -> Dict[str, Any]:
        """Obtener información del sistema"""
        return {
            'fps': self._fps_counter,
            'frame_count': self._frame_count,
            'current_state': type(self._current_state).__name__ if self._current_state else None,
            'state_stack_size': len(self._state_stack),
            'renderer_info': self.renderer.get_info(),
            'audio_info': self.sound_manager.get_info()
        }
```

### ✅ Criterios de Evaluación
- [ ] Arquitectura modular bien definida
- [ ] Sistema de estados funcional
- [ ] Separación clara entre sistemas (graphics, input, audio, etc.)
- [ ] Configuración centralizada
- [ ] API pública bien diseñada
- [ ] Ejemplo funcional incluido

---

## 🥇 Exercise 3: Sistema de E-commerce Multi-módulo

### 🏪 Descripción
Desarrolla un sistema completo de e-commerce organizado en múltiples módulos, cada uno responsable de una parte específica del negocio.

### 📋 Estructura del Proyecto
```
ecommerce_system/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   ├── order.py
│   └── category.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── product_service.py
│   ├── order_service.py
│   └── payment_service.py
├── repositories/
│   ├── __init__.py
│   ├── base_repository.py
│   ├── user_repository.py
│   ├── product_repository.py
│   └── order_repository.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── security.py
│   └── email_sender.py
├── exceptions/
│   ├── __init__.py
│   └── business_exceptions.py
└── cli/
    ├── __init__.py
    └── admin_cli.py
```

### 🔧 Implementación Requerida

#### 1. **Modelos Base `models/base.py`**
```python
"""
Clases base para todos los modelos del sistema
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, Optional
import uuid

class BaseModel(ABC):
    """Clase base para todos los modelos del sistema"""
    
    def __init__(self):
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.is_active: bool = True
    
    def update_timestamp(self) -> None:
        """Actualizar timestamp de modificación"""
        self.updated_at = datetime.now()
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convertir modelo a diccionario"""
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """Crear modelo desde diccionario"""
        pass
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, BaseModel):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
```

#### 2. **Servicio de Productos `services/product_service.py`**
```python
"""
Servicio para gestión de productos
Encapsula lógica de negocio relacionada con productos
"""

from typing import List, Optional, Dict, Any
from decimal import Decimal

from ..models.product import Product
from ..repositories.product_repository import ProductRepository
from ..exceptions.business_exceptions import ProductNotFoundError, InvalidPriceError
from ..utils.validators import validate_product_data

class ProductService:
    """Servicio para gestión de productos"""
    
    def __init__(self, repository: ProductRepository):
        """
        Inicializar servicio de productos
        
        Args:
            repository (ProductRepository): Repositorio de productos
        """
        self._repository = repository
    
    def create_product(self, name: str, description: str, price: Decimal, 
                      category_id: str, stock: int = 0, **kwargs) -> Product:
        """
        Crear nuevo producto
        
        Args:
            name (str): Nombre del producto
            description (str): Descripción del producto
            price (Decimal): Precio del producto
            category_id (str): ID de la categoría
            stock (int): Stock inicial
            **kwargs: Datos adicionales del producto
        
        Returns:
            Product: Producto creado
            
        Raises:
            InvalidPriceError: Si el precio no es válido
            ValidationError: Si los datos no son válidos
        """
        # Validar datos
        product_data = {
            'name': name,
            'description': description,
            'price': price,
            'category_id': category_id,
            'stock': stock,
            **kwargs
        }
        
        validation_result = validate_product_data(product_data)
        if not validation_result.is_valid:
            raise ValidationError(validation_result.errors)
        
        # Validar precio
        if price <= 0:
            raise InvalidPriceError("Product price must be greater than zero")
        
        # Crear producto
        product = Product(
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            stock=stock,
            **kwargs
        )
        
        # Guardar en repositorio
        saved_product = self._repository.save(product)
        
        return saved_product
    
    def update_product(self, product_id: str, **updates) -> Product:
        """
        Actualizar producto existente
        
        Args:
            product_id (str): ID del producto
            **updates: Campos a actualizar
        
        Returns:
            Product: Producto actualizado
            
        Raises:
            ProductNotFoundError: Si el producto no existe
        """
        product = self._repository.find_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        # Validar updates si incluyen precio
        if 'price' in updates and updates['price'] <= 0:
            raise InvalidPriceError("Product price must be greater than zero")
        
        # Aplicar actualizaciones
        for key, value in updates.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        product.update_timestamp()
        
        # Guardar cambios
        updated_product = self._repository.save(product)
        
        return updated_product
    
    def delete_product(self, product_id: str) -> bool:
        """
        Eliminar producto (soft delete)
        
        Args:
            product_id (str): ID del producto
        
        Returns:
            bool: True si se eliminó correctamente
            
        Raises:
            ProductNotFoundError: Si el producto no existe
        """
        product = self._repository.find_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product.is_active = False
        product.update_timestamp()
        
        self._repository.save(product)
        
        return True
    
    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """
        Obtener producto por ID
        
        Args:
            product_id (str): ID del producto
        
        Returns:
            Optional[Product]: Producto si existe, None en caso contrario
        """
        return self._repository.find_by_id(product_id)
    
    def search_products(self, query: str = "", category_id: str = "", 
                       min_price: Decimal = None, max_price: Decimal = None,
                       page: int = 1, per_page: int = 20) -> Dict[str, Any]:
        """
        Buscar productos con filtros
        
        Args:
            query (str): Texto de búsqueda
            category_id (str): ID de categoría para filtrar
            min_price (Decimal): Precio mínimo
            max_price (Decimal): Precio máximo
            page (int): Página de resultados
            per_page (int): Resultados por página
        
        Returns:
            Dict[str, Any]: Resultados de búsqueda con metadatos
        """
        filters = {}
        
        if query:
            filters['name_contains'] = query
        if category_id:
            filters['category_id'] = category_id
        if min_price is not None:
            filters['price_gte'] = min_price
        if max_price is not None:
            filters['price_lte'] = max_price
        
        filters['is_active'] = True
        
        # Obtener resultados paginados
        results = self._repository.find_with_filters(
            filters=filters,
            page=page,
            per_page=per_page
        )
        
        return {
            'products': results['items'],
            'total': results['total'],
            'page': page,
            'per_page': per_page,
            'total_pages': (results['total'] + per_page - 1) // per_page,
            'has_next': page * per_page < results['total'],
            'has_prev': page > 1
        }
    
    def update_stock(self, product_id: str, quantity_change: int) -> Product:
        """
        Actualizar stock de producto
        
        Args:
            product_id (str): ID del producto
            quantity_change (int): Cambio en stock (puede ser negativo)
        
        Returns:
            Product: Producto con stock actualizado
            
        Raises:
            ProductNotFoundError: Si el producto no existe
            InsufficientStockError: Si no hay stock suficiente
        """
        product = self._repository.find_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        new_stock = product.stock + quantity_change
        
        if new_stock < 0:
            raise InsufficientStockError(
                f"Insufficient stock. Available: {product.stock}, Requested: {abs(quantity_change)}"
            )
        
        product.stock = new_stock
        product.update_timestamp()
        
        updated_product = self._repository.save(product)
        
        return updated_product
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """
        Obtener productos con stock bajo
        
        Args:
            threshold (int): Umbral de stock bajo
        
        Returns:
            List[Product]: Productos con stock bajo
        """
        return self._repository.find_with_filters({
            'stock_lte': threshold,
            'is_active': True
        })['items']
    
    def get_category_statistics(self, category_id: str) -> Dict[str, Any]:
        """
        Obtener estadísticas de productos por categoría
        
        Args:
            category_id (str): ID de la categoría
        
        Returns:
            Dict[str, Any]: Estadísticas de la categoría
        """
        products = self._repository.find_with_filters({
            'category_id': category_id,
            'is_active': True
        })['items']
        
        if not products:
            return {
                'total_products': 0,
                'average_price': 0,
                'total_stock': 0,
                'price_range': {'min': 0, 'max': 0}
            }
        
        prices = [product.price for product in products]
        
        return {
            'total_products': len(products),
            'average_price': sum(prices) / len(prices),
            'total_stock': sum(product.stock for product in products),
            'price_range': {
                'min': min(prices),
                'max': max(prices)
            }
        }
```

### ✅ Criterios de Evaluación
- [ ] Separación clara entre modelos, servicios y repositorios
- [ ] Manejo de errores de negocio personalizado
- [ ] Validación de datos robusta
- [ ] API de servicios bien diseñada
- [ ] Repositorios con abstracción de datos
- [ ] CLI funcional para administración

---

## 💪 Exercise 4: Framework de Plugins Dinámicos

### 🔌 Descripción
Desarrolla un framework que permita cargar y gestionar plugins dinámicamente, demostrando técnicas avanzadas de programación modular.

### 📋 Estructura del Proyecto
```
plugin_framework/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── plugin_manager.py
│   ├── plugin_interface.py
│   └── event_system.py
├── discovery/
│   ├── __init__.py
│   ├── plugin_loader.py
│   └── dependency_resolver.py
├── registry/
│   ├── __init__.py
│   └── plugin_registry.py
├── plugins/
│   ├── __init__.py
│   ├── example_plugin/
│   │   ├── __init__.py
│   │   └── plugin.py
│   └── math_plugin/
│       ├── __init__.py
│       └── plugin.py
└── examples/
    ├── basic_usage.py
    └── advanced_usage.py
```

### 🔧 Implementación Clave

#### 1. **Plugin Manager `core/plugin_manager.py`**
```python
"""
Gestor principal de plugins
Maneja carga, activación, desactivación y comunicación entre plugins
"""

import importlib
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any, Type
from ..registry.plugin_registry import PluginRegistry
from ..discovery.plugin_loader import PluginLoader
from ..core.event_system import EventSystem
from .plugin_interface import PluginInterface

class PluginManager:
    """Gestor central de plugins del framework"""
    
    def __init__(self, plugin_directories: List[str] = None):
        """
        Inicializar gestor de plugins
        
        Args:
            plugin_directories (List[str]): Directorios donde buscar plugins
        """
        self._registry = PluginRegistry()
        self._loader = PluginLoader()
        self._event_system = EventSystem()
        
        self._plugin_directories = plugin_directories or []
        self._active_plugins: Dict[str, PluginInterface] = {}
        self._plugin_dependencies: Dict[str, List[str]] = {}
        
        # Configurar directorios por defecto
        self._setup_default_directories()
    
    def _setup_default_directories(self) -> None:
        """Configurar directorios por defecto para buscar plugins"""
        # Directorio plugins del framework
        framework_plugins = Path(__file__).parent.parent / "plugins"
        if framework_plugins.exists():
            self._plugin_directories.append(str(framework_plugins))
        
        # Directorio plugins del usuario
        user_plugins = Path.cwd() / "plugins"
        if user_plugins.exists():
            self._plugin_directories.append(str(user_plugins))
    
    def discover_plugins(self) -> List[str]:
        """
        Descubrir plugins disponibles en los directorios configurados
        
        Returns:
            List[str]: Lista de nombres de plugins descubiertos
        """
        discovered = []
        
        for directory in self._plugin_directories:
            plugin_names = self._loader.discover_plugins_in_directory(directory)
            discovered.extend(plugin_names)
        
        return discovered
    
    def load_plugin(self, plugin_name: str) -> bool:
        """
        Cargar plugin por nombre
        
        Args:
            plugin_name (str): Nombre del plugin
        
        Returns:
            bool: True si se cargó correctamente
        """
        try:
            # Buscar plugin en directorios
            plugin_path = self._find_plugin_path(plugin_name)
            if not plugin_path:
                raise PluginNotFoundError(f"Plugin '{plugin_name}' not found")
            
            # Cargar módulo del plugin
            plugin_module = self._loader.load_plugin_module(plugin_path)
            
            # Obtener clase del plugin
            plugin_class = self._loader.get_plugin_class(plugin_module)
            
            # Validar que implementa la interfaz
            if not issubclass(plugin_class, PluginInterface):
                raise PluginInterfaceError(f"Plugin '{plugin_name}' does not implement PluginInterface")
            
            # Crear instancia del plugin
            plugin_instance = plugin_class()
            
            # Registrar plugin
            plugin_info = {
                'name': plugin_name,
                'version': getattr(plugin_instance, 'version', '1.0.0'),
                'description': getattr(plugin_instance, 'description', ''),
                'dependencies': getattr(plugin_instance, 'dependencies', []),
                'class': plugin_class,
                'instance': plugin_instance,
                'path': plugin_path
            }
            
            self._registry.register_plugin(plugin_name, plugin_info)
            
            # Guardar dependencias
            self._plugin_dependencies[plugin_name] = plugin_info['dependencies']
            
            return True
            
        except Exception as e:
            print(f"Error loading plugin '{plugin_name}': {e}")
            return False
    
    def activate_plugin(self, plugin_name: str) -> bool:
        """
        Activar plugin cargado
        
        Args:
            plugin_name (str): Nombre del plugin
        
        Returns:
            bool: True si se activó correctamente
        """
        if plugin_name in self._active_plugins:
            return True  # Ya está activo
        
        if not self._registry.is_registered(plugin_name):
            if not self.load_plugin(plugin_name):
                return False
        
        try:
            # Verificar y activar dependencias
            dependencies = self._plugin_dependencies.get(plugin_name, [])
            for dependency in dependencies:
                if not self.activate_plugin(dependency):
                    raise DependencyError(f"Failed to activate dependency '{dependency}' for '{plugin_name}'")
            
            # Obtener instancia del plugin
            plugin_info = self._registry.get_plugin_info(plugin_name)
            plugin_instance = plugin_info['instance']
            
            # Configurar contexto del plugin
            plugin_context = PluginContext(
                framework=self,
                event_system=self._event_system,
                registry=self._registry
            )
            
            # Activar plugin
            plugin_instance.activate(plugin_context)
            
            # Añadir a plugins activos
            self._active_plugins[plugin_name] = plugin_instance
            
            # Emitir evento de activación
            self._event_system.emit('plugin.activated', {
                'plugin_name': plugin_name,
                'plugin_info': plugin_info
            })
            
            return True
            
        except Exception as e:
            print(f"Error activating plugin '{plugin_name}': {e}")
            return False
    
    def deactivate_plugin(self, plugin_name: str) -> bool:
        """
        Desactivar plugin activo
        
        Args:
            plugin_name (str): Nombre del plugin
        
        Returns:
            bool: True si se desactivó correctamente
        """
        if plugin_name not in self._active_plugins:
            return True  # Ya está inactivo
        
        try:
            # Verificar dependencias (otros plugins que dependen de este)
            dependent_plugins = self._find_dependent_plugins(plugin_name)
            if dependent_plugins:
                # Desactivar plugins dependientes primero
                for dependent in dependent_plugins:
                    self.deactivate_plugin(dependent)
            
            # Obtener instancia del plugin
            plugin_instance = self._active_plugins[plugin_name]
            
            # Desactivar plugin
            plugin_instance.deactivate()
            
            # Remover de plugins activos
            del self._active_plugins[plugin_name]
            
            # Emitir evento de desactivación
            self._event_system.emit('plugin.deactivated', {
                'plugin_name': plugin_name
            })
            
            return True
            
        except Exception as e:
            print(f"Error deactivating plugin '{plugin_name}': {e}")
            return False
    
    def get_active_plugins(self) -> List[str]:
        """Obtener lista de plugins activos"""
        return list(self._active_plugins.keys())
    
    def get_available_plugins(self) -> List[str]:
        """Obtener lista de plugins disponibles (registrados)"""
        return self._registry.get_registered_plugins()
    
    def get_plugin_info(self, plugin_name: str) -> Optional[Dict[str, Any]]:
        """Obtener información detallada de un plugin"""
        return self._registry.get_plugin_info(plugin_name)
    
    def call_plugin_method(self, plugin_name: str, method_name: str, *args, **kwargs) -> Any:
        """
        Llamar método específico de un plugin activo
        
        Args:
            plugin_name (str): Nombre del plugin
            method_name (str): Nombre del método
            *args: Argumentos posicionales
            **kwargs: Argumentos con nombre
        
        Returns:
            Any: Resultado del método
        """
        if plugin_name not in self._active_plugins:
            raise PluginNotActiveError(f"Plugin '{plugin_name}' is not active")
        
        plugin_instance = self._active_plugins[plugin_name]
        
        if not hasattr(plugin_instance, method_name):
            raise PluginMethodError(f"Plugin '{plugin_name}' does not have method '{method_name}'")
        
        method = getattr(plugin_instance, method_name)
        return method(*args, **kwargs)
    
    def broadcast_to_plugins(self, method_name: str, *args, **kwargs) -> Dict[str, Any]:
        """
        Llamar método en todos los plugins activos que lo tengan
        
        Args:
            method_name (str): Nombre del método
            *args: Argumentos posicionales
            **kwargs: Argumentos con nombre
        
        Returns:
            Dict[str, Any]: Resultados por plugin
        """
        results = {}
        
        for plugin_name, plugin_instance in self._active_plugins.items():
            if hasattr(plugin_instance, method_name):
                try:
                    method = getattr(plugin_instance, method_name)
                    result = method(*args, **kwargs)
                    results[plugin_name] = result
                except Exception as e:
                    results[plugin_name] = f"Error: {e}"
        
        return results
```

### ✅ Criterios de Evaluación
- [ ] Sistema de descubrimiento de plugins funcional
- [ ] Gestión de dependencias entre plugins
- [ ] Sistema de eventos para comunicación
- [ ] Carga dinámica de módulos Python
- [ ] Interfaz de plugin bien definida
- [ ] Ejemplos de plugins funcionales

---

## 🎯 Objetivos de Aprendizaje Completados

Al terminar estos ejercicios, habrás demostrado:

### 📦 Organización Modular
- [x] Estructurar proyectos complejos en módulos
- [x] Configurar `__init__.py` para APIs limpias
- [x] Separar responsabilidades efectivamente
- [x] Crear jerarquías de módulos coherentes

### 🏗️ Arquitectura de Software
- [x] Implementar patrones de diseño con módulos
- [x] Crear sistemas extensibles y mantenibles
- [x] Diseñar APIs públicas intuitivas
- [x] Aplicar principios de separación de responsabilidades

### 📖 Documentación y Testing
- [x] Documentar módulos con docstrings profesionales
- [x] Crear tests para sistemas multi-módulo
- [x] Generar documentación automática
- [x] Mantener código limpio y legible

### 🔧 Técnicas Avanzadas
- [x] Carga dinámica de módulos
- [x] Gestión de dependencias
- [x] Sistemas de plugins
- [x] Distribución de paquetes

## 🚀 Siguientes Pasos

1. **Refactorizar** proyectos anteriores usando estructura modular
2. **Experimentar** con diferentes patrones de organización
3. **Crear** tu propio framework o librería
4. **Documentar** y compartir tu trabajo

---

**💡 Consejo**: La organización modular no es solo sobre archivos separados. Es sobre crear un sistema que sea fácil de entender, mantener y extender.

**🎯 Meta**: Cada ejercicio debe demostrar que puedes crear software bien organizado y escalable usando principios de programación modular.
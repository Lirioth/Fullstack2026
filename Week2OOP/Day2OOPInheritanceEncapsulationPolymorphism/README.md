# 🏗️ Day 2 - OOP: Inheritance, Encapsulation, Polymorphism

## 🎯 Objetivos de Aprendizaje

Al finalizar este día, podrás:
- 👨‍👩‍👧‍👦 **Implementar herencia** entre clases de manera efectiva
- 🔒 **Aplicar encapsulación** para proteger datos y métodos
- 🎭 **Utilizar polimorfismo** para crear código flexible y reutilizable
- 🏛️ **Diseñar jerarquías** de clases bien estructuradas
- 🔧 **Sobrescribir métodos** y utilizar `super()`
- 🎨 **Crear interfaces** consistentes a través del polimorfismo

## 📚 Conceptos Clave

### 👨‍👩‍👧‍👦 Herencia (Inheritance)
```python
# Clase padre (superclase)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Clase hija (subclase)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):  # Método sobrescrito
        return "Woof!"
    
    def fetch(self):  # Método específico
        return f"{self.name} is fetching the ball!"
```

### 🔒 Encapsulación (Encapsulation)
```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner  # Público
        self._account_number = self._generate_account()  # Protegido
        self.__balance = initial_balance  # Privado
    
    def _generate_account(self):  # Método protegido
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def __validate_amount(self, amount):  # Método privado
        return amount > 0
    
    def deposit(self, amount):  # Método público
        if self.__validate_amount(amount):
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):  # Getter
        return self.__balance
    
    @property
    def balance(self):  # Property
        return self.__balance
```

### 🎭 Polimorfismo (Polymorphism)
```python
# Diferentes clases con la misma interfaz
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polimorfismo en acción
def print_shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print_shape_info(shape)  # Mismo método, diferentes comportamientos
```

## 🛠️ Características Avanzadas

### 🔧 Método `super()`
```python
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Llamar al constructor padre
        self.battery_capacity = battery_capacity
    
    def start_engine(self):
        base_message = super().start_engine()  # Llamar al método padre
        return f"{base_message} (Electric mode)"
```

### 🏛️ Herencia Múltiple
```python
class Flyable:
    def fly(self):
        return "Flying in the sky"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack!"
```

### 🎨 Métodos Abstractos
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def validate_payment(self, payment_data):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def validate_payment(self, payment_data):
        return len(payment_data.get('card_number', '')) == 16
```

## 📋 Actividades del Día

### 🥉 **Nivel Principiante**
- [ ] Crear clase base `Vehicle` con clases hijas `Car`, `Motorcycle`, `Bicycle`
- [ ] Implementar encapsulación en clase `Student` con atributos privados
- [ ] Practicar sobrescritura de métodos con `__str__` y `__repr__`

### 🥈 **Nivel Intermedio**
- [ ] Diseñar jerarquía de empleados con diferentes tipos y salarios
- [ ] Implementar sistema de formas geométricas con polimorfismo
- [ ] Crear clase `BankAccount` con validaciones y encapsulación completa

### 🥇 **Nivel Avanzado**
- [ ] Sistema de animales con herencia múltiple y traits
- [ ] Implementar patrón Strategy usando polimorfismo
- [ ] Crear sistema de notificaciones con diferentes canales

### 💪 **Desafío Ninja**
- [ ] Desarrollar mini-framework OOP para juegos
- [ ] Sistema de plugins con carga dinámica de clases
- [ ] Implementar patrón Observer con herencia

## 🎮 Ejercicios Prácticos

### 📁 [Exercises](./Exercises/README.md)
- **Exercise 1**: 🏠 Sistema de Propiedades Inmobiliarias
- **Exercise 2**: 🎵 Reproductor de Música con Polimorfismo
- **Exercise 3**: 🏦 Sistema Bancario con Encapsulación
- **Exercise 4**: 🐾 Zoológico Virtual con Herencia

### 🏆 [Daily Challenge](./DailyChallenge/README.md)
**🏰 Sistema de Gestión de Reino Medieval**
- Crear jerarquía completa de personajes (Rey, Nobles, Caballeros, Campesinos)
- Implementar sistema de combate polimórfico
- Gestión de recursos del reino con encapsulación

## 🔍 Conceptos para Investigar

### 🤔 Preguntas de Reflexión
1. **¿Cuándo usar herencia vs composición?**
2. **¿Qué problemas resuelve la encapsulación?**
3. **¿Cómo mejora el polimorfismo la mantenibilidad del código?**
4. **¿Cuáles son las desventajas de la herencia múltiple?**

### 🔬 Experimentos
- Comparar rendimiento: herencia vs composición
- Analizar Method Resolution Order (MRO) en Python
- Implementar diferentes patrones de diseño con OOP

## ✅ Checklist de Progreso

### 🎯 Objetivos Completados
- [ ] Comprendo la diferencia entre herencia, encapsulación y polimorfismo
- [ ] Puedo crear jerarquías de clases efectivas
- [ ] Sé cuándo y cómo usar `super()`
- [ ] Implemento encapsulación con atributos privados y protegidos
- [ ] Aplico polimorfismo para crear código flexible
- [ ] Entiendo el MRO en herencia múltiple

### 🛠️ Habilidades Técnicas
- [ ] Sobrescritura de métodos especiales (`__str__`, `__repr__`, etc.)
- [ ] Uso de properties para getters y setters
- [ ] Implementación de métodos abstractos
- [ ] Manejo de herencia múltiple
- [ ] Aplicación de principios SOLID básicos

### 🎨 Proyecto del Día
- [ ] Diseño de arquitectura OOP completa
- [ ] Implementación de al menos 3 niveles de herencia
- [ ] Uso efectivo de encapsulación en todos los atributos críticos
- [ ] Demostración de polimorfismo en múltiples contextos

## 🚀 Preparación para Mañana

### 📖 Lecturas Recomendadas
- Patrones de diseño en Python
- Módulos y paquetes de Python
- Organización de código en proyectos grandes

### 🎯 Próximos Temas
- **Day 3**: 📦 OOP and Modules - Organización y estructura de código
- Importación de módulos y paquetes
- Creación de librerías personalizadas
- Documentación de código y APIs

## 🆘 Troubleshooting

### ❌ Errores Comunes
1. **AttributeError con herencia**
   ```python
   # ❌ Problema
   class Child(Parent):
       def __init__(self):
           self.child_attr = "value"  # Falta super().__init__()
   
   # ✅ Solución
   class Child(Parent):
       def __init__(self):
           super().__init__()
           self.child_attr = "value"
   ```

2. **Acceso a atributos privados**
   ```python
   # ❌ Problema
   account.__balance  # AttributeError
   
   # ✅ Solución
   account.get_balance()  # Usar método público
   ```

3. **Herencia múltiple confusa**
   ```python
   # ✅ Verificar MRO
   print(MyClass.__mro__)
   # ✅ Usar super() consistentemente
   ```

### 🔧 Tips de Debugging
- Usar `isinstance()` y `issubclass()` para verificar tipos
- Imprimir `__dict__` para ver atributos de instancia
- Usar `help()` para documentación de métodos
- Debugger paso a paso para entender herencia

## 📚 Recursos Adicionales

### 🎥 Videos Recomendados
- "Python OOP Tutorial: Inheritance, Encapsulation, Polymorphism"
- "Design Patterns in Python"
- "Advanced Python OOP Concepts"

### 📖 Documentación
- [Python Class Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python ABC Module](https://docs.python.org/3/library/abc.html)

### 🛠️ Herramientas
- **pylint**: Análisis de código OOP
- **mypy**: Type checking para clases
- **pydoc**: Generación de documentación

---

**💡 Recuerda**: La programación orientada a objetos es sobre modelar el mundo real en código. Piensa en objetos, sus propiedades y cómo interactúan entre sí.

**🎯 Meta del día**: Crear un sistema completo que demuestre los tres pilares de OOP trabajando juntos armoniosamente.
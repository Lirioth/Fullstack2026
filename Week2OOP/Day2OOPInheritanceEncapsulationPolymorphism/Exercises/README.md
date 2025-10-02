# 🛠️ Day 2 Exercises - OOP: Inheritance, Encapsulation, Polymorphism

## 🎯 Objetivos de los Ejercicios

Estos ejercicios te ayudarán a dominar:
- 👨‍👩‍👧‍👦 **Herencia**: Crear relaciones padre-hijo entre clases
- 🔒 **Encapsulación**: Proteger datos con atributos privados y métodos
- 🎭 **Polimorfismo**: Implementar métodos que se comportan diferente según el objeto
- 🏛️ **Diseño OOP**: Crear arquitecturas de clases bien estructuradas

---

## 🥉 Exercise 1: Sistema de Propiedades Inmobiliarias

### 🏠 Descripción
Crea un sistema para gestionar diferentes tipos de propiedades inmobiliarias utilizando herencia, encapsulación y polimorfismo.

### 📋 Requisitos

#### Clase Base: `Property`
```python
class Property:
    def __init__(self, address, price, property_type):
        """
        Inicializar propiedad base
        
        Args:
            address (str): Dirección de la propiedad
            price (float): Precio de la propiedad
            property_type (str): Tipo de propiedad
        """
        pass
    
    def get_description(self):
        """Retorna descripción básica de la propiedad"""
        pass
    
    def calculate_tax(self):
        """Calcula impuesto base (2% del precio)"""
        pass
    
    def __str__(self):
        """Representación en string de la propiedad"""
        pass
```

#### Clases Hijas
1. **`House`** - Casa residencial
   - Atributos adicionales: `bedrooms`, `bathrooms`, `garage`
   - Método específico: `get_living_space()`
   - Sobrescribir: `calculate_tax()` (1.5% del precio)

2. **`Apartment`** - Apartamento
   - Atributos adicionales: `floor`, `building_amenities`
   - Método específico: `get_monthly_maintenance()`
   - Sobrescribir: `calculate_tax()` (1.8% del precio)

3. **`Commercial`** - Propiedad comercial
   - Atributos adicionales: `business_type`, `parking_spaces`
   - Método específico: `get_rental_yield()`
   - Sobrescribir: `calculate_tax()` (3% del precio)

### 🔒 Encapsulación Requerida
- Precio debe ser privado (`__price`)
- Crear property para acceder al precio
- Validar que el precio sea positivo
- Método privado para formatear moneda

### 🎭 Polimorfismo Demostrado
```python
def print_property_info(property_obj):
    """Función que acepta cualquier tipo de propiedad"""
    print(property_obj.get_description())
    print(f"Tax: ${property_obj.calculate_tax():.2f}")
    print("-" * 30)

# Lista mixta de propiedades
properties = [
    House("123 Main St", 300000, 3, 2, True),
    Apartment("456 Oak Ave", 150000, 5, ["Pool", "Gym"]),
    Commercial("789 Business Blvd", 500000, "Restaurant", 20)
]

for prop in properties:
    print_property_info(prop)  # Polimorfismo en acción
```

### ✅ Criterios de Evaluación
- [ ] Herencia correcta implementada
- [ ] Encapsulación de precio con validación
- [ ] Polimorfismo funciona con función genérica
- [ ] Todos los métodos sobrescritos funcionan
- [ ] Métodos específicos implementados

---

## 🥈 Exercise 2: Reproductor de Música con Polimorfismo

### 🎵 Descripción
Desarrolla un sistema de reproductor de música que puede manejar diferentes formatos de audio usando polimorfismo.

### 📋 Requisitos

#### Clase Abstracta Base: `AudioFile`
```python
from abc import ABC, abstractmethod

class AudioFile(ABC):
    def __init__(self, filename, duration):
        """
        Args:
            filename (str): Nombre del archivo
            duration (int): Duración en segundos
        """
        pass
    
    @abstractmethod
    def play(self):
        """Método abstracto para reproducir audio"""
        pass
    
    @abstractmethod
    def get_file_info(self):
        """Método abstracto para obtener información del archivo"""
        pass
    
    def get_duration_formatted(self):
        """Retorna duración en formato MM:SS"""
        pass
```

#### Clases Concretas
1. **`MP3File`**
   - Atributo adicional: `bitrate`
   - Implementar: `play()` - "Playing MP3: {filename} at {bitrate}kbps"
   - Implementar: `get_file_info()` - información específica de MP3

2. **`WAVFile`**
   - Atributo adicional: `sample_rate`
   - Implementar: `play()` - "Playing WAV: {filename} at {sample_rate}Hz"
   - Implementar: `get_file_info()` - información específica de WAV

3. **`FLACFile`**
   - Atributo adicional: `compression_level`
   - Implementar: `play()` - "Playing FLAC: {filename} (compression: {level})"
   - Implementar: `get_file_info()` - información específica de FLAC

#### Clase Playlist
```python
class Playlist:
    def __init__(self, name):
        """
        Args:
            name (str): Nombre de la playlist
        """
        self.__name = name  # Privado
        self.__songs = []   # Privado
        self.__current_index = 0  # Privado
    
    def add_song(self, audio_file):
        """Añade canción a la playlist"""
        pass
    
    def play_current(self):
        """Reproduce canción actual"""
        pass
    
    def next_song(self):
        """Avanza a siguiente canción"""
        pass
    
    def get_total_duration(self):
        """Calcula duración total de la playlist"""
        pass
    
    @property
    def name(self):
        """Getter para nombre de playlist"""
        pass
    
    def __len__(self):
        """Retorna número de canciones"""
        pass
```

### 🎭 Polimorfismo en Acción
```python
# Crear playlist mixta
my_playlist = Playlist("My Favorites")
my_playlist.add_song(MP3File("song1.mp3", 180, 320))
my_playlist.add_song(WAVFile("song2.wav", 240, 44100))
my_playlist.add_song(FLACFile("song3.flac", 200, 5))

# Reproducir toda la playlist (polimorfismo)
for i in range(len(my_playlist)):
    my_playlist.play_current()
    my_playlist.next_song()
```

### ✅ Criterios de Evaluación
- [ ] Clase abstracta correctamente implementada
- [ ] Todos los métodos abstractos implementados en clases hijas
- [ ] Encapsulación en clase Playlist
- [ ] Polimorfismo demostrado en reproducción
- [ ] Properties y métodos especiales funcionando

---

## 🥇 Exercise 3: Sistema Bancario con Encapsulación

### 🏦 Descripción
Implementa un sistema bancario completo que demuestre encapsulación robusta y herencia de diferentes tipos de cuentas.

### 📋 Requisitos

#### Clase Base: `BankAccount`
```python
class BankAccount:
    # Contador de cuentas (atributo de clase)
    _account_count = 0
    
    def __init__(self, owner, initial_balance=0):
        """
        Args:
            owner (str): Nombre del propietario
            initial_balance (float): Balance inicial
        """
        # Incrementar contador
        BankAccount._account_count += 1
        
        # Atributos públicos, protegidos y privados
        self.owner = owner  # Público
        self._account_number = self._generate_account_number()  # Protegido
        self.__balance = 0  # Privado
        self.__transaction_history = []  # Privado
        
        # Depositar balance inicial si es válido
        if initial_balance > 0:
            self.deposit(initial_balance)
    
    def _generate_account_number(self):
        """Método protegido para generar número de cuenta"""
        pass
    
    def __validate_amount(self, amount):
        """Método privado para validar cantidad"""
        pass
    
    def __record_transaction(self, transaction_type, amount, description=""):
        """Método privado para registrar transacciones"""
        pass
    
    def deposit(self, amount):
        """Depositar dinero en la cuenta"""
        pass
    
    def withdraw(self, amount):
        """Retirar dinero de la cuenta"""
        pass
    
    @property
    def balance(self):
        """Property para acceder al balance"""
        pass
    
    @property
    def account_number(self):
        """Property para acceder al número de cuenta"""
        pass
    
    def get_transaction_history(self):
        """Obtener historial de transacciones"""
        pass
    
    @classmethod
    def get_total_accounts(cls):
        """Método de clase para obtener total de cuentas"""
        pass
```

#### Clases Hijas

1. **`SavingsAccount`** - Cuenta de Ahorros
   - Atributo adicional: `interest_rate`
   - Método específico: `apply_interest()`
   - Sobrescribir: `withdraw()` - máximo 3 retiros por mes
   - Atributo privado: `__withdrawal_count`

2. **`CheckingAccount`** - Cuenta Corriente
   - Atributo adicional: `overdraft_limit`
   - Método específico: `get_available_funds()`
   - Sobrescribir: `withdraw()` - permitir sobregiro hasta el límite

3. **`BusinessAccount`** - Cuenta Empresarial
   - Atributo adicional: `business_name`
   - Método específico: `generate_statement()`
   - Sobrescribir: `deposit()` - cobrar comisión en depósitos grandes
   - Atributo privado: `__monthly_fee`

### 🔒 Encapsulación Avanzada
```python
class SecureBankAccount(BankAccount):
    def __init__(self, owner, pin, initial_balance=0):
        super().__init__(owner, initial_balance)
        self.__pin = pin  # PIN encriptado
        self.__locked = False
        self.__failed_attempts = 0
    
    def __encrypt_pin(self, pin):
        """Método privado para encriptar PIN"""
        pass
    
    def __verify_pin(self, pin):
        """Método privado para verificar PIN"""
        pass
    
    def authenticate(self, pin):
        """Autenticar usuario con PIN"""
        pass
    
    def lock_account(self):
        """Bloquear cuenta por seguridad"""
        pass
    
    def unlock_account(self, admin_code):
        """Desbloquear cuenta con código de administrador"""
        pass
```

### ✅ Criterios de Evaluación
- [ ] Encapsulación completa con atributos privados, protegidos y públicos
- [ ] Herencia correcta con sobrescritura de métodos
- [ ] Properties funcionando correctamente
- [ ] Validaciones y seguridad implementadas
- [ ] Métodos de clase y contador funcionando

---

## 💪 Exercise 4: Zoológico Virtual con Herencia

### 🐾 Descripción
Desarrolla un sistema completo de zoológico que demuestre herencia múltiple, polimorfismo y encapsulación en un contexto complejo.

### 📋 Requisitos

#### Clase Base y Mixins
```python
class Animal:
    """Clase base para todos los animales"""
    def __init__(self, name, species, age, weight):
        pass
    
    def eat(self):
        """Método base para comer"""
        pass
    
    def sleep(self):
        """Método base para dormir"""
        pass
    
    def make_sound(self):
        """Método que debe ser sobrescrito"""
        raise NotImplementedError("Subclass must implement make_sound")

# Mixins para habilidades especiales
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"
    
    def land(self):
        return f"{self.name} has landed."

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"
    
    def dive(self):
        return f"{self.name} is diving deep!"

class Climbable:
    def climb(self):
        return f"{self.name} is climbing!"
```

#### Clases de Animales Específicos
1. **`Mammal`** (hereda de `Animal`)
   - Atributo adicional: `fur_color`
   - Método específico: `give_birth()`

2. **`Bird`** (hereda de `Animal` y `Flyable`)
   - Atributo adicional: `wing_span`
   - Método específico: `build_nest()`

3. **`Fish`** (hereda de `Animal` y `Swimmable`)
   - Atributo adicional: `water_type` (freshwater/saltwater)
   - Método específico: `school_behavior()`

4. **`Duck`** (hereda de `Bird` y `Swimmable`)
   - Demuestra herencia múltiple compleja
   - Sobrescribe múltiples métodos

#### Sistema de Zoológico
```python
class Zoo:
    def __init__(self, name, location):
        """
        Sistema completo de gestión de zoológico
        """
        self.__name = name  # Privado
        self.__location = location  # Privado
        self.__animals = {}  # Privado: {species: [animals]}
        self.__visitors = 0  # Privado
        self.__revenue = 0.0  # Privado
    
    def add_animal(self, animal):
        """Añadir animal al zoológico"""
        pass
    
    def remove_animal(self, animal_name):
        """Remover animal del zoológico"""
        pass
    
    def feed_all_animals(self):
        """Alimentar todos los animales (polimorfismo)"""
        pass
    
    def get_animals_by_ability(self, ability):
        """Obtener animales que pueden volar, nadar, etc."""
        pass
    
    def calculate_daily_food_cost(self):
        """Calcular costo diario de alimentación"""
        pass
    
    @property
    def animal_count(self):
        """Total de animales en el zoológico"""
        pass
    
    def generate_report(self):
        """Generar reporte completo del zoológico"""
        pass
```

#### Polimorfismo Avanzado
```python
def animal_showcase(animals):
    """Función que demuestra polimorfismo con cualquier animal"""
    for animal in animals:
        print(f"\n--- {animal.name} the {animal.species} ---")
        print(animal.make_sound())
        print(animal.eat())
        
        # Polimorfismo condicional basado en habilidades
        if hasattr(animal, 'fly'):
            print(animal.fly())
        if hasattr(animal, 'swim'):
            print(animal.swim())
        if hasattr(animal, 'climb'):
            print(animal.climb())

# Ejemplo de uso
zoo_animals = [
    Lion("Simba", 5, 180),
    Eagle("Aguila", 3, 6, 2.5),
    Dolphin("Flipper", 8, 300, "saltwater"),
    Duck("Donald", 2, 2, 0.8)
]

animal_showcase(zoo_animals)
```

### ✅ Criterios de Evaluación
- [ ] Herencia múltiple correctamente implementada
- [ ] Mixins funcionando con diferentes combinaciones
- [ ] Polimorfismo demostrado en múltiples contextos
- [ ] Encapsulación robusta en clase Zoo
- [ ] Method Resolution Order (MRO) entendido y aplicado
- [ ] Sistema completo funcionando cohesivamente

---

## 🎯 Objetivos de Aprendizaje Completados

Al terminar estos ejercicios, habrás demostrado:

### 👨‍👩‍👧‍👦 Herencia
- [x] Crear jerarquías de clases simples y complejas
- [x] Sobrescribir métodos efectivamente
- [x] Usar `super()` correctamente
- [x] Implementar herencia múltiple cuando sea apropiado

### 🔒 Encapsulación
- [x] Proteger datos con atributos privados
- [x] Crear interfaces públicas consistentes
- [x] Implementar validaciones y seguridad
- [x] Usar properties y métodos especiales

### 🎭 Polimorfismo
- [x] Crear métodos que funcionan con múltiples tipos
- [x] Implementar interfaces consistentes
- [x] Usar polimorfismo para código flexible
- [x] Entender duck typing en Python

## 🚀 Siguientes Pasos

1. **Revisar y refactorizar** tu código para aplicar principios SOLID
2. **Experimentar** con diferentes diseños de herencia
3. **Prepararte** para módulos y organización de código en Day 3
4. **Documentar** tus clases con docstrings apropiados

---

**💡 Consejo**: No sobrecompliques la herencia. Usa composición cuando la relación no sea claramente "es-un" sino "tiene-un".

**🎯 Meta**: Cada ejercicio debe demostrar los tres pilares de OOP trabajando juntos armoniosamente.
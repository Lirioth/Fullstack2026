# 🏰 Daily Challenge - Sistema de Gestión de Reino Medieval

## 🎯 Descripción del Desafío

Desarrolla un sistema completo de gestión para un reino medieval que demuestre **herencia**, **encapsulación** y **polimorfismo** en un contexto épico y divertido. Tu sistema debe manejar diferentes tipos de personajes, combates, recursos y eventos del reino.

---

## 🏛️ Arquitectura del Sistema

### 👑 Jerarquía de Personajes

#### Clase Base: `Character`
```python
from abc import ABC, abstractmethod
from enum import Enum

class CharacterClass(Enum):
    ROYALTY = "Royalty"
    NOBILITY = "Nobility"
    WARRIOR = "Warrior"
    COMMONER = "Commoner"

class Character(ABC):
    def __init__(self, name, age, health=100):
        """
        Clase base para todos los personajes del reino
        
        Args:
            name (str): Nombre del personaje
            age (int): Edad del personaje
            health (int): Salud inicial (max 100)
        """
        self._name = name  # Protegido
        self._age = age    # Protegido
        self.__health = min(health, 100)  # Privado
        self.__max_health = 100  # Privado
        self.__experience = 0  # Privado
        self.__level = 1  # Privado
        self._character_class = None  # Será definido por subclases
        
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self.__health
    
    @property
    def level(self):
        return self.__level
    
    @abstractmethod
    def get_status(self):
        """Retorna estado actual del personaje"""
        pass
    
    @abstractmethod
    def daily_activity(self):
        """Actividad diaria específica del personaje"""
        pass
    
    @abstractmethod
    def calculate_tax_contribution(self):
        """Calcula contribución de impuestos al reino"""
        pass
    
    def take_damage(self, damage):
        """Recibir daño"""
        self.__health = max(0, self.__health - damage)
        return self.__health <= 0  # Retorna True si murió
    
    def heal(self, amount):
        """Curar personaje"""
        self.__health = min(self.__max_health, self.__health + amount)
    
    def gain_experience(self, exp):
        """Ganar experiencia y subir de nivel"""
        self.__experience += exp
        new_level = (self.__experience // 100) + 1
        if new_level > self.__level:
            self.__level = new_level
            self._level_up()
    
    def _level_up(self):
        """Método protegido para manejar subida de nivel"""
        self.__max_health += 10
        self.__health = self.__max_health
    
    def __str__(self):
        return f"{self._name} ({self._character_class.value}) - Level {self.__level}"
```

### 🏰 Jerarquía Completa de Personajes

#### 1. 👑 Clase `Royalty`
```python
class Royalty(Character):
    def __init__(self, name, age, title, kingdom_wealth=10000):
        super().__init__(name, age, health=150)  # Los reyes tienen más salud
        self.__title = title  # Privado
        self.__kingdom_wealth = kingdom_wealth  # Privado
        self.__royal_decrees = []  # Privado
        self._character_class = CharacterClass.ROYALTY
        self.__popularity = 50  # Popularidad con el pueblo
    
    @property
    def title(self):
        return self.__title
    
    @property
    def kingdom_wealth(self):
        return self.__kingdom_wealth
    
    def issue_decree(self, decree):
        """Emitir decreto real"""
        self.__royal_decrees.append(decree)
        return f"His/Her Majesty {self._name} decrees: {decree}"
    
    def collect_taxes(self, subjects):
        """Recolectar impuestos de súbditos"""
        total_tax = 0
        for subject in subjects:
            if subject != self:  # El rey no se paga impuestos a sí mismo
                tax = subject.calculate_tax_contribution()
                total_tax += tax
                self.__kingdom_wealth += tax
        return total_tax
    
    def get_status(self):
        return f"👑 {self._name} the {self.__title} rules with {self.__kingdom_wealth} gold and {self.__popularity}% popularity"
    
    def daily_activity(self):
        """Actividad diaria: Gobernar el reino"""
        self.gain_experience(20)
        return f"{self._name} governs the kingdom and makes important decisions"
    
    def calculate_tax_contribution(self):
        return 0  # Los reyes no pagan impuestos
```

#### 2. 🏺 Clase `Noble`
```python
class Noble(Character):
    def __init__(self, name, age, estate_size, wealth=1000):
        super().__init__(name, age, health=120)
        self.__estate_size = estate_size  # Privado (hectáreas)
        self.__wealth = wealth  # Privado
        self.__vassals = []  # Privado (lista de campesinos)
        self._character_class = CharacterClass.NOBILITY
        self.__influence = 25  # Influencia política
    
    @property
    def estate_size(self):
        return self.__estate_size
    
    @property
    def wealth(self):
        return self.__wealth
    
    def manage_estate(self):
        """Gestionar propiedades"""
        income = self.__estate_size * 10  # 10 gold per hectare
        self.__wealth += income
        self.gain_experience(10)
        return f"{self._name} manages estate and earns {income} gold"
    
    def recruit_vassal(self, peasant):
        """Reclutar campesino como vasallo"""
        self.__vassals.append(peasant)
        self.__influence += 5
        return f"{peasant.name} now serves {self._name}"
    
    def get_status(self):
        return f"🏺 Lord/Lady {self._name} owns {self.__estate_size} hectares with {len(self.__vassals)} vassals"
    
    def daily_activity(self):
        return self.manage_estate()
    
    def calculate_tax_contribution(self):
        return self.__wealth * 0.15  # 15% de impuestos
```

#### 3. ⚔️ Clase `Knight`
```python
class Knight(Character):
    def __init__(self, name, age, weapon="sword", armor_type="chainmail"):
        super().__init__(name, age, health=130)
        self.__weapon = weapon  # Privado
        self.__armor_type = armor_type  # Privado
        self.__honor = 50  # Privado
        self.__victories = 0  # Privado
        self._character_class = CharacterClass.WARRIOR
        self.__quest_completed = 0
    
    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def honor(self):
        return self.__honor
    
    def train_combat(self):
        """Entrenar habilidades de combate"""
        self.gain_experience(15)
        self.__honor += 2
        return f"⚔️ {self._name} trains with {self.__weapon} and gains honor"
    
    def complete_quest(self, quest_difficulty):
        """Completar misión"""
        self.__quest_completed += 1
        experience = quest_difficulty * 20
        self.gain_experience(experience)
        self.__honor += quest_difficulty * 5
        return f"🗡️ {self._name} completed a quest and gained {experience} experience!"
    
    def duel(self, opponent):
        """Duelo con otro personaje"""
        import random
        
        # Cálculo de probabilidad basado en nivel y honor
        self_power = self.level * 10 + self.__honor
        opponent_power = opponent.level * 10 + getattr(opponent, '_Knight__honor', 25)
        
        if random.randint(1, 100) <= (self_power / (self_power + opponent_power)) * 100:
            self.__victories += 1
            self.__honor += 10
            self.gain_experience(25)
            opponent.take_damage(20)
            return f"⚔️ {self._name} defeats {opponent.name} in honorable combat!"
        else:
            self.take_damage(15)
            self.__honor = max(0, self.__honor - 5)
            return f"💔 {self._name} is defeated by {opponent.name}"
    
    def get_status(self):
        return f"⚔️ Sir/Dame {self._name} - Honor: {self.__honor}, Victories: {self.__victories}, Quests: {self.__quest_completed}"
    
    def daily_activity(self):
        return self.train_combat()
    
    def calculate_tax_contribution(self):
        return 50  # Los caballeros pagan una cantidad fija
```

#### 4. 🌾 Clase `Peasant`
```python
class Peasant(Character):
    def __init__(self, name, age, profession="farmer", productivity=1.0):
        super().__init__(name, age, health=80)
        self.__profession = profession  # Privado
        self.__productivity = productivity  # Privado (multiplicador)
        self.__food_produced = 0  # Privado
        self.__coins = 100  # Privado
        self._character_class = CharacterClass.COMMONER
        self.__family_size = 3  # Número de familiares
    
    @property
    def profession(self):
        return self.__profession
    
    @property
    def coins(self):
        return self.__coins
    
    def work(self):
        """Trabajar en su profesión"""
        base_production = {
            "farmer": 15,
            "blacksmith": 20,
            "merchant": 25,
            "carpenter": 18,
            "baker": 12
        }
        
        production = base_production.get(self.__profession, 10) * self.__productivity
        
        if self.__profession == "farmer":
            self.__food_produced += production
            self.__coins += production * 2
        else:
            self.__coins += production
        
        self.gain_experience(5)
        return f"🌾 {self._name} the {self.__profession} produces {production:.1f} units"
    
    def pay_rent(self, lord):
        """Pagar renta al señor feudal"""
        rent = min(self.__coins * 0.3, self.__coins)
        self.__coins -= rent
        return f"💰 {self._name} pays {rent:.1f} coins rent to {lord.name}"
    
    def get_status(self):
        return f"🌾 {self._name} the {self.__profession} - {self.__coins:.1f} coins, {self.__food_produced:.1f} food produced"
    
    def daily_activity(self):
        return self.work()
    
    def calculate_tax_contribution(self):
        return max(5, self.__coins * 0.1)  # Mínimo 5 gold o 10% de sus monedas
```

---

## 🏰 Sistema de Reino

### 🏛️ Clase `Kingdom`
```python
class Kingdom:
    def __init__(self, name, ruler):
        """
        Sistema completo de gestión del reino
        
        Args:
            name (str): Nombre del reino
            ruler (Royalty): Rey o Reina del reino
        """
        self.__name = name  # Privado
        self.__ruler = ruler  # Privado
        self.__population = [ruler]  # Privado - Lista de todos los personajes
        self.__treasury = 1000  # Privado - Tesoro del reino
        self.__food_stores = 500  # Privado - Almacenes de comida
        self.__day_count = 0  # Privado - Días transcurridos
        self.__events_log = []  # Privado - Registro de eventos
        self.__kingdom_happiness = 50  # Privado - Felicidad del reino
    
    @property
    def name(self):
        return self.__name
    
    @property
    def ruler(self):
        return self.__ruler
    
    @property
    def population_count(self):
        return len(self.__population)
    
    @property
    def treasury(self):
        return self.__treasury
    
    def add_citizen(self, character):
        """Añadir ciudadano al reino"""
        self.__population.append(character)
        self.__log_event(f"{character.name} joined the kingdom")
        return f"Welcome {character.name} to {self.__name}!"
    
    def remove_citizen(self, character_name):
        """Remover ciudadano del reino"""
        for citizen in self.__population:
            if citizen.name == character_name:
                self.__population.remove(citizen)
                self.__log_event(f"{character_name} left the kingdom")
                return f"{character_name} has left {self.__name}"
        return f"{character_name} not found in kingdom"
    
    def __log_event(self, event):
        """Método privado para registrar eventos"""
        self.__events_log.append({
            'day': self.__day_count,
            'event': event,
            'timestamp': f"Day {self.__day_count}"
        })
    
    def simulate_day(self):
        """Simular un día completo en el reino"""
        self.__day_count += 1
        daily_report = [f"\\n=== Day {self.__day_count} in {self.__name} ===\"]
        
        # Actividades diarias de cada ciudadano (polimorfismo)
        food_produced = 0
        for citizen in self.__population:
            activity_result = citizen.daily_activity()
            daily_report.append(activity_result)
            
            # Calcular producción de comida
            if isinstance(citizen, Peasant) and citizen.profession == "farmer":
                food_produced += 15 * getattr(citizen, '_Peasant__productivity', 1.0)
        
        # Actualizar almacenes de comida
        self.__food_stores += food_produced
        food_consumed = len(self.__population) * 2  # 2 unidades por persona por día
        self.__food_stores -= food_consumed
        
        # Recolectar impuestos (polimorfismo en acción)
        if self.__day_count % 7 == 0:  # Recolectar impuestos cada semana
            total_taxes = self.__ruler.collect_taxes(self.__population)
            self.__treasury += total_taxes
            daily_report.append(f"💰 Tax collection: {total_taxes:.1f} gold collected")
        
        # Eventos aleatorios
        import random
        if random.randint(1, 10) == 1:  # 10% probabilidad de evento
            event = self.__generate_random_event()
            daily_report.append(f"🎲 Random Event: {event}")
        
        # Calcular felicidad del reino
        self.__calculate_kingdom_happiness()
        
        daily_report.append(f"📊 Kingdom Status: Treasury: {self.__treasury:.1f}, Food: {self.__food_stores:.1f}, Happiness: {self.__kingdom_happiness}%")
        
        return "\\n".join(daily_report)
    
    def __generate_random_event(self):
        """Método privado para generar eventos aleatorios"""
        import random
        
        events = [
            "🌧️ Heavy rains increase crop yields!",
            "🐺 Wolf pack threatens the village!",
            "💎 Merchants discover valuable gems!",
            "🦠 Minor plague affects productivity",
            "🎪 Traveling circus boosts morale!",
            "⚡ Storm damages some buildings",
            "👥 Refugees seek shelter in the kingdom",
            "🎯 Successful hunt brings extra food"
        ]
        
        event = random.choice(events)
        
        # Aplicar efectos del evento
        if "crop yields" in event:
            self.__food_stores += 100
        elif "Wolf pack" in event:
            self.__kingdom_happiness -= 10
        elif "valuable gems" in event:
            self.__treasury += 200
        elif "plague" in event:
            self.__kingdom_happiness -= 15
        elif "circus" in event:
            self.__kingdom_happiness += 20
        
        self.__log_event(event)
        return event
    
    def __calculate_kingdom_happiness(self):
        """Método privado para calcular felicidad del reino"""
        factors = []
        
        # Factor de comida
        if self.__food_stores > 200:
            factors.append(10)
        elif self.__food_stores < 50:
            factors.append(-15)
        
        # Factor de tesoro
        if self.__treasury > 2000:
            factors.append(5)
        elif self.__treasury < 100:
            factors.append(-10)
        
        # Factor de población
        nobles = len([c for c in self.__population if isinstance(c, Noble)])
        knights = len([c for c in self.__population if isinstance(c, Knight)])
        
        if knights > nobles:  # Buena protección
            factors.append(8)
        
        # Aplicar cambios
        happiness_change = sum(factors)
        self.__kingdom_happiness = max(0, min(100, self.__kingdom_happiness + happiness_change))
    
    def get_population_by_class(self, character_class):
        """Obtener población por clase de personaje"""
        if character_class == CharacterClass.ROYALTY:
            return [c for c in self.__population if isinstance(c, Royalty)]
        elif character_class == CharacterClass.NOBILITY:
            return [c for c in self.__population if isinstance(c, Noble)]
        elif character_class == CharacterClass.WARRIOR:
            return [c for c in self.__population if isinstance(c, Knight)]
        elif character_class == CharacterClass.COMMONER:
            return [c for c in self.__population if isinstance(c, Peasant)]
        return []
    
    def organize_tournament(self):
        """Organizar torneo entre caballeros"""
        knights = self.get_population_by_class(CharacterClass.WARRIOR)
        
        if len(knights) < 2:
            return "Not enough knights for a tournament!"
        
        tournament_report = ["\\n🏆 ROYAL TOURNAMENT 🏆"]
        
        import random
        participants = random.sample(knights, min(4, len(knights)))
        
        for i in range(len(participants) - 1):
            match_result = participants[i].duel(participants[i + 1])
            tournament_report.append(match_result)
        
        # Premios del torneo
        winner = max(participants, key=lambda k: k.honor)
        prize = 100
        tournament_report.append(f"👑 Tournament Winner: {winner.name} receives {prize} gold!")
        
        self.__treasury -= prize
        self.__kingdom_happiness += 15
        self.__log_event(f"Tournament held, won by {winner.name}")
        
        return "\\n".join(tournament_report)
    
    def generate_kingdom_report(self):
        """Generar reporte completo del reino"""
        report = [f"\\n📜 KINGDOM OF {self.__name.upper()} - FULL REPORT 📜"]
        report.append(f"👑 Ruler: {self.__ruler.name} ({self.__ruler.title})")
        report.append(f"📅 Day: {self.__day_count}")
        report.append(f"💰 Treasury: {self.__treasury:.1f} gold")
        report.append(f"🌾 Food Stores: {self.__food_stores:.1f} units")
        report.append(f"😊 Kingdom Happiness: {self.__kingdom_happiness}%")
        report.append(f"👥 Total Population: {len(self.__population)}")
        
        # Desglose por clase
        for char_class in CharacterClass:
            population = self.get_population_by_class(char_class)
            report.append(f"  {char_class.value}: {len(population)}")
        
        # Eventos recientes
        recent_events = self.__events_log[-5:] if self.__events_log else []
        if recent_events:
            report.append("\\n📰 Recent Events:")
            for event in recent_events:
                report.append(f"  Day {event['day']}: {event['event']}")
        
        return "\\n".join(report)
    
    def simulate_multiple_days(self, days):
        """Simular múltiples días"""
        results = []
        for day in range(days):
            day_result = self.simulate_day()
            results.append(day_result)
            
            # Eventos especiales en días específicos
            if self.__day_count % 10 == 0:  # Cada 10 días
                tournament = self.organize_tournament()
                results.append(tournament)
        
        return "\\n\\n".join(results)
```

---

## 🎯 Objetivos del Desafío

### 🏗️ Requisitos Técnicos Obligatorios

#### 1. **Herencia** (30 puntos)
- [ ] Implementar jerarquía completa de 5+ clases
- [ ] Usar `super()` correctamente en todos los constructores
- [ ] Sobrescribir métodos abstractos en todas las subclases
- [ ] Implementar herencia múltiple en al menos una clase
- [ ] Demostrar Method Resolution Order (MRO)

#### 2. **Encapsulación** (30 puntos)
- [ ] Atributos privados (`__attribute`) para datos sensibles
- [ ] Atributos protegidos (`_attribute`) para datos internos
- [ ] Properties para acceso controlado a datos
- [ ] Métodos privados para lógica interna
- [ ] Validaciones en setters y métodos

#### 3. **Polimorfismo** (30 puntos)
- [ ] Métodos abstractos implementados diferentemente
- [ ] Función que acepta cualquier tipo de Character
- [ ] Sobrescritura de métodos especiales (`__str__`, `__repr__`)
- [ ] Duck typing demostrado
- [ ] Interfaces consistentes entre clases

#### 4. **Funcionalidad Completa** (10 puntos)
- [ ] Sistema Kingdom funcional completamente
- [ ] Simulación de días funcional
- [ ] Eventos aleatorios implementados
- [ ] Reportes detallados generados
- [ ] Interacciones entre personajes

---

## 🎮 Casos de Uso para Probar

### 📝 Script de Prueba Sugerido
```python
def main():
    # Crear reino
    king = Royalty("Arthur", 35, "King", 5000)
    kingdom = Kingdom("Camelot", king)
    
    # Añadir población diversa
    kingdom.add_citizen(Noble("Lord Gawain", 30, 50, 2000))
    kingdom.add_citizen(Knight("Sir Lancelot", 28, "excalibur", "plate"))
    kingdom.add_citizen(Knight("Dame Joan", 25, "bow", "leather"))
    kingdom.add_citizen(Peasant("Farmer Bob", 40, "farmer", 1.2))
    kingdom.add_citizen(Peasant("Blacksmith Joe", 35, "blacksmith", 1.0))
    kingdom.add_citizen(Peasant("Baker Mary", 30, "baker", 0.8))
    
    # Simular una semana
    print("🏰 SIMULATION START 🏰")
    week_result = kingdom.simulate_multiple_days(7)
    print(week_result)
    
    # Organizar torneo
    print("\\n" + "="*50)
    tournament = kingdom.organize_tournament()
    print(tournament)
    
    # Reporte final
    print("\\n" + "="*50)
    final_report = kingdom.generate_kingdom_report()
    print(final_report)
    
    # Demostrar polimorfismo
    print("\\n🎭 POLYMORPHISM DEMONSTRATION 🎭")
    all_citizens = kingdom._Kingdom__population  # Para acceso de prueba
    for citizen in all_citizens:
        print(f"Status: {citizen.get_status()}")
        print(f"Daily Activity: {citizen.daily_activity()}")
        print(f"Tax Contribution: {citizen.calculate_tax_contribution():.1f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```

---

## ✅ Criterios de Evaluación Detallados

### 🎖️ Rubrica de Evaluación

#### **Excelente (90-100 puntos)**
- Todos los conceptos OOP implementados perfectamente
- Código limpio, bien documentado y eficiente
- Funcionalidades adicionales creativas implementadas
- Manejo de errores robusto
- Principios SOLID aplicados

#### **Bueno (75-89 puntos)**
- Conceptos OOP implementados correctamente
- Funcionalidad completa trabajando
- Código bien estructurado
- Documentación básica presente

#### **Satisfactorio (60-74 puntos)**
- Conceptos principales OOP presentes
- Funcionalidad básica funcionando
- Estructura de clases correcta
- Algunos errores menores

#### **Necesita Mejora (0-59 puntos)**
- Conceptos OOP mal implementados
- Funcionalidad incompleta o con errores
- Estructura de código deficiente

---

## 🚀 Extensiones Opcionales (Puntos Extra)

### 🌟 Funcionalidades Adicionales
1. **Sistema de Magia** (10 puntos)
   - Crear clase `Wizard` con hechizos
   - Sistema de maná y cooldowns
   - Efectos mágicos en el reino

2. **Comercio Internacional** (10 puntos)
   - Intercambio con otros reinos
   - Sistema de caravanas y comerciantes
   - Fluctuación de precios

3. **Sistema de Construcción** (10 puntos)
   - Edificios con diferentes funciones
   - Costos de construcción y mantenimiento
   - Efectos en la productividad del reino

4. **Diplomacia** (10 puntos)
   - Relaciones con reinos vecinos
   - Tratados y alianzas
   - Amenazas externas

### 🎨 Mejoras de Interface
- Sistema de menús interactivos
- Guardado y carga de juegos
- Visualización ASCII del reino
- Colores en la terminal

---

## 📚 Recursos de Apoyo

### 🔍 Conceptos a Investigar
- **SOLID Principles**: Especialmente Single Responsibility y Open/Closed
- **Design Patterns**: Observer, Strategy, Factory
- **Python Magic Methods**: `__len__`, `__iter__`, `__contains__`
- **Composition vs Inheritance**: Cuándo usar cada uno

### 🛠️ Herramientas Útiles
```python
# Para debugging OOP
print(ClassName.__mro__)  # Method Resolution Order
print(instance.__dict__)  # Atributos de instancia
print(ClassName.__dict__)  # Atributos de clase

# Para testing
import unittest
# Crear tests para cada clase

# Para documentación
"""Docstrings detallados para cada método"""
```

---

## 🎯 Entregables

### 📁 Estructura de Archivos Esperada
```
DailyChallenge/
├── kingdom_system.py          # Sistema principal
├── characters.py              # Todas las clases de personajes
├── kingdom.py                 # Clase Kingdom
├── enums.py                   # Enumeraciones y constantes
├── test_kingdom.py            # Tests unitarios
├── main.py                    # Script de demostración
└── README.md                  # Este archivo
```

### 📋 Documentación Requerida
1. **Diagrama de Clases**: Mostrar relaciones de herencia
2. **Explicación de Decisiones**: Por qué elegiste cierta estructura
3. **Casos de Uso**: Cómo usar el sistema
4. **Limitaciones Conocidas**: Qué falta o se puede mejorar

---

**🏆 Meta Final**: Crear un sistema que demuestre que dominas los tres pilares de OOP y puedes aplicarlos en un contexto complejo y divertido.

**💡 Consejo Principal**: No te enfoques solo en completar requisitos. Piensa como un arquitecto de software y diseña un sistema que sea extensible y mantenible.

**🎮 ¡Que comience la aventura medieval!** 🏰⚔️👑
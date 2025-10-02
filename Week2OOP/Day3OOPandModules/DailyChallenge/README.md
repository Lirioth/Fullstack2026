# 🏗️ Daily Challenge - Sistema de Gestión de Biblioteca Digital

## 🎯 Descripción del Desafío

Desarrolla un **Sistema de Gestión de Biblioteca Digital** completo que demuestre arquitectura modular avanzada, patrones de diseño, y mejores prácticas de organización de código. El sistema debe manejar múltiples tipos de recursos, usuarios, préstamos, reservas y generar reportes detallados.

---

## 🏛️ Arquitectura del Sistema

### 📂 Estructura de Proyecto Completa
```
digital_library/
├── __init__.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── database.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   ├── resource.py
│   ├── book.py
│   ├── magazine.py
│   ├── multimedia.py
│   ├── loan.py
│   └── reservation.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── resource_service.py
│   ├── loan_service.py
│   ├── reservation_service.py
│   ├── notification_service.py
│   └── report_service.py
├── repositories/
│   ├── __init__.py
│   ├── base_repository.py
│   ├── user_repository.py
│   ├── resource_repository.py
│   ├── loan_repository.py
│   └── reservation_repository.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── security.py
│   ├── date_helpers.py
│   ├── file_helpers.py
│   └── formatters.py
├── exceptions/
│   ├── __init__.py
│   ├── library_exceptions.py
│   └── validation_exceptions.py
├── plugins/
│   ├── __init__.py
│   ├── barcode_scanner/
│   ├── email_notifications/
│   └── late_fee_calculator/
├── cli/
│   ├── __init__.py
│   ├── admin_cli.py
│   ├── librarian_cli.py
│   └── user_cli.py
├── web/
│   ├── __init__.py
│   ├── api.py
│   └── routes/
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   ├── test_services/
│   ├── test_repositories/
│   └── test_integration/
└── docs/
    ├── api.md
    ├── architecture.md
    └── user_guide.md
```

---

## 🔧 Implementación Requerida

### 🏗️ 1. Sistema de Configuración

#### `config/settings.py`
```python
"""
Configuración centralizada del sistema de biblioteca
Maneja todas las configuraciones de la aplicación
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import timedelta

class Settings:
    """Configuración principal del sistema"""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Inicializar configuración
        
        Args:
            config_file (str, optional): Archivo de configuración personalizado
        """
        self._config: Dict[str, Any] = {}
        self._load_default_config()
        
        if config_file:
            self._load_config_file(config_file)
        
        self._load_environment_variables()
    
    def _load_default_config(self) -> None:
        """Cargar configuración por defecto"""
        self._config = {
            # Configuración de la biblioteca
            'library': {
                'name': 'Digital Library System',
                'max_loans_per_user': 5,
                'loan_duration_days': 14,
                'max_renewals': 2,
                'late_fee_per_day': 0.50,
                'max_reservations_per_user': 3,
                'reservation_hold_days': 3
            },
            
            # Configuración de base de datos
            'database': {
                'type': 'sqlite',
                'path': 'library.db',
                'backup_enabled': True,
                'backup_interval_hours': 24
            },
            
            # Configuración de seguridad
            'security': {
                'password_min_length': 8,
                'session_timeout_minutes': 30,
                'max_login_attempts': 5,
                'lockout_duration_minutes': 15
            },
            
            # Configuración de notificaciones
            'notifications': {
                'email_enabled': True,
                'sms_enabled': False,
                'reminder_days_before_due': 3,
                'overdue_notification_interval_days': 7
            },
            
            # Configuración de reportes
            'reports': {
                'auto_generate': True,
                'output_directory': 'reports',
                'formats': ['pdf', 'csv', 'json'],
                'retention_days': 90
            },
            
            # Configuración de plugins
            'plugins': {
                'enabled': True,
                'auto_load': True,
                'directories': ['plugins', 'external_plugins']
            },
            
            # Configuración de logging
            'logging': {
                'level': 'INFO',
                'file': 'library.log',
                'max_size_mb': 10,
                'backup_count': 5
            }
        }
    
    def _load_config_file(self, config_file: str) -> None:
        """Cargar configuración desde archivo"""
        try:
            import json
            config_path = Path(config_file)
            
            if config_path.suffix == '.json':
                with open(config_path, 'r') as f:
                    file_config = json.load(f)
                    self._merge_config(file_config)
            
            elif config_path.suffix in ['.yml', '.yaml']:
                import yaml
                with open(config_path, 'r') as f:
                    file_config = yaml.safe_load(f)
                    self._merge_config(file_config)
                    
        except Exception as e:
            print(f"Warning: Could not load config file {config_file}: {e}")
    
    def _load_environment_variables(self) -> None:
        """Cargar configuración desde variables de entorno"""
        env_mappings = {
            'LIBRARY_NAME': 'library.name',
            'DB_PATH': 'database.path',
            'MAX_LOANS': 'library.max_loans_per_user',
            'LOAN_DURATION': 'library.loan_duration_days',
            'EMAIL_ENABLED': 'notifications.email_enabled',
            'LOG_LEVEL': 'logging.level'
        }
        
        for env_var, config_path in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value:
                self._set_nested_config(config_path, env_value)
    
    def _merge_config(self, new_config: Dict[str, Any]) -> None:
        """Fusionar nueva configuración con la existente"""
        def merge_dict(base: Dict, update: Dict) -> Dict:
            for key, value in update.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    merge_dict(base[key], value)
                else:
                    base[key] = value
            return base
        
        merge_dict(self._config, new_config)
    
    def _set_nested_config(self, path: str, value: Any) -> None:
        """Establecer valor de configuración usando path con puntos"""
        keys = path.split('.')
        current = self._config
        
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # Convertir tipos básicos
        if isinstance(value, str):
            if value.lower() in ['true', 'false']:
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)
            elif value.replace('.', '').isdigit():
                value = float(value)
        
        current[keys[-1]] = value
    
    def get(self, path: str, default: Any = None) -> Any:
        """
        Obtener valor de configuración
        
        Args:
            path (str): Path con puntos (ej: 'library.max_loans_per_user')
            default (Any): Valor por defecto si no existe
        
        Returns:
            Any: Valor de configuración
        """
        keys = path.split('.')
        current = self._config
        
        try:
            for key in keys:
                current = current[key]
            return current
        except KeyError:
            return default
    
    def set(self, path: str, value: Any) -> None:
        """Establecer valor de configuración"""
        self._set_nested_config(path, value)
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """Obtener sección completa de configuración"""
        return self._config.get(section, {}).copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Obtener toda la configuración como diccionario"""
        return self._config.copy()
    
    def save_to_file(self, filename: str) -> None:
        """Guardar configuración actual en archivo"""
        import json
        config_path = Path(filename)
        
        with open(config_path, 'w') as f:
            json.dump(self._config, f, indent=2, default=str)

# Instancia global de configuración
settings = Settings()

# Funciones de conveniencia
def get_setting(path: str, default: Any = None) -> Any:
    """Función de conveniencia para obtener configuración"""
    return settings.get(path, default)

def set_setting(path: str, value: Any) -> None:
    """Función de conveniencia para establecer configuración"""
    settings.set(path, value)
```

### 📚 2. Modelos de Recursos

#### `models/resource.py`
```python
"""
Clase base para todos los recursos de la biblioteca
Define interfaz común para libros, revistas, multimedia, etc.
"""

from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import Dict, Any, List, Optional
from enum import Enum
from decimal import Decimal

from .base import BaseModel

class ResourceType(Enum):
    """Tipos de recursos disponibles"""
    BOOK = "book"
    MAGAZINE = "magazine" 
    DVD = "dvd"
    CD = "cd"
    EBOOK = "ebook"
    AUDIOBOOK = "audiobook"
    JOURNAL = "journal"
    NEWSPAPER = "newspaper"

class ResourceStatus(Enum):
    """Estados de un recurso"""
    AVAILABLE = "available"
    LOANED = "loaned"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"
    LOST = "lost"
    DAMAGED = "damaged"
    RETIRED = "retired"

class Resource(BaseModel):
    """
    Clase base abstracta para todos los recursos de la biblioteca
    
    Define la interfaz común que deben implementar todos los tipos
    de recursos (libros, revistas, DVDs, etc.)
    """
    
    def __init__(self, title: str, resource_type: ResourceType, 
                 isbn_or_id: str, acquisition_date: date = None):
        """
        Inicializar recurso base
        
        Args:
            title (str): Título del recurso
            resource_type (ResourceType): Tipo de recurso
            isbn_or_id (str): ISBN, ISSN, o identificador único
            acquisition_date (date): Fecha de adquisición
        """
        super().__init__()
        
        self.title = title
        self.resource_type = resource_type
        self.isbn_or_id = isbn_or_id
        self.acquisition_date = acquisition_date or date.today()
        
        # Información bibliográfica común
        self.authors: List[str] = []
        self.publishers: List[str] = []
        self.publication_date: Optional[date] = None
        self.language = "en"
        self.subjects: List[str] = []
        self.description = ""
        
        # Estado y ubicación
        self.status = ResourceStatus.AVAILABLE
        self.location_code = ""
        self.shelf_number = ""
        self.copy_number = 1
        
        # Información financiera
        self.acquisition_cost: Optional[Decimal] = None
        self.replacement_cost: Optional[Decimal] = None
        
        # Metadatos adicionales
        self.keywords: List[str] = []
        self.notes = ""
        self.barcode = ""
        
        # Estadísticas de uso
        self.total_loans = 0
        self.total_reservations = 0
        self.last_loan_date: Optional[datetime] = None
        
        # Información física
        self.condition = "good"  # excellent, good, fair, poor
        self.pages: Optional[int] = None
        self.dimensions = ""  # "25x18x2 cm"
        self.weight: Optional[Decimal] = None
    
    @property
    def is_available(self) -> bool:
        """Verificar si el recurso está disponible para préstamo"""
        return self.status == ResourceStatus.AVAILABLE
    
    @property
    def is_loanable(self) -> bool:
        """Verificar si el recurso puede ser prestado"""
        return self.status in [ResourceStatus.AVAILABLE, ResourceStatus.RESERVED]
    
    @property
    def age_in_days(self) -> int:
        """Calcular edad del recurso en días desde adquisición"""
        return (date.today() - self.acquisition_date).days
    
    @abstractmethod
    def get_loan_duration_days(self) -> int:
        """
        Obtener duración de préstamo en días para este tipo de recurso
        
        Returns:
            int: Número de días del préstamo
        """
        pass
    
    @abstractmethod
    def get_max_renewals(self) -> int:
        """
        Obtener número máximo de renovaciones permitidas
        
        Returns:
            int: Número máximo de renovaciones
        """
        pass
    
    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> Decimal:
        """
        Calcular tarifa por días de retraso
        
        Args:
            days_overdue (int): Días de retraso
        
        Returns:
            Decimal: Monto de la tarifa
        """
        pass
    
    @abstractmethod
    def get_resource_specific_info(self) -> Dict[str, Any]:
        """
        Obtener información específica del tipo de recurso
        
        Returns:
            Dict[str, Any]: Información específica
        """
        pass
    
    def add_author(self, author: str) -> None:
        """Añadir autor al recurso"""
        if author and author not in self.authors:
            self.authors.append(author)
    
    def add_subject(self, subject: str) -> None:
        """Añadir materia/tema al recurso"""
        if subject and subject not in self.subjects:
            self.subjects.append(subject)
    
    def add_keyword(self, keyword: str) -> None:
        """Añadir palabra clave al recurso"""
        if keyword and keyword not in self.keywords:
            self.keywords.append(keyword)
    
    def update_status(self, new_status: ResourceStatus, notes: str = "") -> None:
        """
        Actualizar estado del recurso
        
        Args:
            new_status (ResourceStatus): Nuevo estado
            notes (str): Notas sobre el cambio de estado
        """
        old_status = self.status
        self.status = new_status
        self.update_timestamp()
        
        if notes:
            self.notes += f"\\n{datetime.now()}: Status changed from {old_status.value} to {new_status.value}. {notes}"
    
    def record_loan(self) -> None:
        """Registrar préstamo del recurso"""
        self.total_loans += 1
        self.last_loan_date = datetime.now()
        self.update_status(ResourceStatus.LOANED)
    
    def record_return(self) -> None:
        """Registrar devolución del recurso"""
        self.update_status(ResourceStatus.AVAILABLE)
    
    def record_reservation(self) -> None:
        """Registrar reserva del recurso"""
        self.total_reservations += 1
        if self.status == ResourceStatus.AVAILABLE:
            self.update_status(ResourceStatus.RESERVED)
    
    def get_usage_statistics(self) -> Dict[str, Any]:
        """Obtener estadísticas de uso del recurso"""
        return {
            'total_loans': self.total_loans,
            'total_reservations': self.total_reservations,
            'last_loan_date': self.last_loan_date.isoformat() if self.last_loan_date else None,
            'age_in_days': self.age_in_days,
            'loans_per_year': self.total_loans / max(1, self.age_in_days / 365),
            'current_status': self.status.value,
            'condition': self.condition
        }
    
    def search_match(self, query: str) -> bool:
        """
        Verificar si el recurso coincide con una búsqueda
        
        Args:
            query (str): Término de búsqueda
        
        Returns:
            bool: True si hay coincidencia
        """
        query = query.lower()
        search_fields = [
            self.title.lower(),
            self.isbn_or_id.lower(),
            self.description.lower(),
            ' '.join(self.authors).lower(),
            ' '.join(self.subjects).lower(),
            ' '.join(self.keywords).lower()
        ]
        
        return any(query in field for field in search_fields)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir recurso a diccionario"""
        base_dict = super().to_dict()
        
        resource_dict = {
            'title': self.title,
            'resource_type': self.resource_type.value,
            'isbn_or_id': self.isbn_or_id,
            'acquisition_date': self.acquisition_date.isoformat(),
            'authors': self.authors,
            'publishers': self.publishers,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'language': self.language,
            'subjects': self.subjects,
            'description': self.description,
            'status': self.status.value,
            'location_code': self.location_code,
            'shelf_number': self.shelf_number,
            'copy_number': self.copy_number,
            'acquisition_cost': str(self.acquisition_cost) if self.acquisition_cost else None,
            'replacement_cost': str(self.replacement_cost) if self.replacement_cost else None,
            'keywords': self.keywords,
            'notes': self.notes,
            'barcode': self.barcode,
            'total_loans': self.total_loans,
            'total_reservations': self.total_reservations,
            'last_loan_date': self.last_loan_date.isoformat() if self.last_loan_date else None,
            'condition': self.condition,
            'pages': self.pages,
            'dimensions': self.dimensions,
            'weight': str(self.weight) if self.weight else None
        }
        
        # Añadir información específica del tipo de recurso
        resource_dict.update(self.get_resource_specific_info())
        
        base_dict.update(resource_dict)
        return base_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Resource':
        """
        Crear recurso desde diccionario
        
        Note: Este método debe ser sobrescrito por subclases
        """
        raise NotImplementedError("Subclasses must implement from_dict method")
    
    def __str__(self) -> str:
        """Representación en string del recurso"""
        authors_str = ", ".join(self.authors) if self.authors else "Unknown Author"
        return f"{self.title} by {authors_str} ({self.resource_type.value.title()})"
    
    def __repr__(self) -> str:
        """Representación técnica del recurso"""
        return f"Resource(id='{self.id}', title='{self.title}', type='{self.resource_type.value}', status='{self.status.value}')"
```

#### `models/book.py`
```python
"""
Modelo específico para libros
Extiende Resource con características específicas de libros
"""

from datetime import date
from typing import Dict, Any, Optional, List
from decimal import Decimal
from enum import Enum

from .resource import Resource, ResourceType
from ..config.settings import get_setting

class BookFormat(Enum):
    """Formatos de libro"""
    HARDCOVER = "hardcover"
    PAPERBACK = "paperback"
    EBOOK = "ebook"
    AUDIOBOOK = "audiobook"

class BookGenre(Enum):
    """Géneros de libros"""
    FICTION = "fiction"
    NON_FICTION = "non_fiction"
    BIOGRAPHY = "biography"
    HISTORY = "history"
    SCIENCE = "science"
    TECHNOLOGY = "technology"
    ARTS = "arts"
    LITERATURE = "literature"
    PHILOSOPHY = "philosophy"
    RELIGION = "religion"
    CHILDREN = "children"
    YOUNG_ADULT = "young_adult"
    TEXTBOOK = "textbook"
    REFERENCE = "reference"

class Book(Resource):
    """
    Modelo para libros físicos y digitales
    
    Extiende Resource con características específicas de libros
    como género, formato, ISBN, editorial, etc.
    """
    
    def __init__(self, title: str, isbn: str, acquisition_date: date = None):
        """
        Inicializar libro
        
        Args:
            title (str): Título del libro
            isbn (str): ISBN del libro
            acquisition_date (date): Fecha de adquisición
        """
        super().__init__(title, ResourceType.BOOK, isbn, acquisition_date)
        
        # Información específica de libros
        self.isbn = isbn
        self.isbn13 = ""
        self.edition = ""
        self.volume = ""
        self.series = ""
        self.genre = BookGenre.FICTION
        self.format = BookFormat.PAPERBACK
        
        # Información editorial
        self.publisher = ""
        self.publication_year: Optional[int] = None
        self.copyright_year: Optional[int] = None
        
        # Información física/técnica
        self.pages = 0
        self.chapters: List[str] = []
        self.table_of_contents: List[str] = []
        
        # Información de contenido
        self.abstract = ""
        self.target_audience = ""  # children, young_adult, adult, academic
        self.reading_level = ""    # beginner, intermediate, advanced
        
        # Para libros digitales
        self.file_format = ""      # pdf, epub, mobi, etc.
        self.file_size_mb: Optional[Decimal] = None
        self.drm_protected = False
        
        # Para audiolibros
        self.narrator = ""
        self.duration_minutes: Optional[int] = None
        
        # Clasificación
        self.dewey_decimal = ""
        self.lc_classification = ""  # Library of Congress
        
        # Reviews y calificaciones
        self.average_rating: Optional[Decimal] = None
        self.total_reviews = 0
        
        # Premios y reconocimientos
        self.awards: List[str] = []
        
    def get_loan_duration_days(self) -> int:
        """Duración de préstamo para libros"""
        if self.format == BookFormat.EBOOK:
            return get_setting('library.ebook_loan_duration_days', 7)
        elif self.format == BookFormat.AUDIOBOOK:
            return get_setting('library.audiobook_loan_duration_days', 14)
        else:
            return get_setting('library.book_loan_duration_days', 21)
    
    def get_max_renewals(self) -> int:
        """Número máximo de renovaciones para libros"""
        if self.format in [BookFormat.EBOOK, BookFormat.AUDIOBOOK]:
            return get_setting('library.digital_max_renewals', 1)
        else:
            return get_setting('library.book_max_renewals', 2)
    
    def calculate_late_fee(self, days_overdue: int) -> Decimal:
        """Calcular tarifa por retraso en libros"""
        if self.format in [BookFormat.EBOOK, BookFormat.AUDIOBOOK]:
            # Los recursos digitales no tienen tarifa por retraso
            return Decimal('0.00')
        
        daily_rate = Decimal(str(get_setting('library.book_late_fee_per_day', 0.25)))
        max_fee = Decimal(str(get_setting('library.book_max_late_fee', 10.00)))
        
        calculated_fee = daily_rate * days_overdue
        return min(calculated_fee, max_fee)
    
    def get_resource_specific_info(self) -> Dict[str, Any]:
        """Información específica de libros"""
        info = {
            'isbn': self.isbn,
            'isbn13': self.isbn13,
            'edition': self.edition,
            'volume': self.volume,
            'series': self.series,
            'genre': self.genre.value,
            'format': self.format.value,
            'publisher': self.publisher,
            'publication_year': self.publication_year,
            'copyright_year': self.copyright_year,
            'chapters_count': len(self.chapters),
            'abstract': self.abstract,
            'target_audience': self.target_audience,
            'reading_level': self.reading_level,
            'dewey_decimal': self.dewey_decimal,
            'lc_classification': self.lc_classification,
            'average_rating': str(self.average_rating) if self.average_rating else None,
            'total_reviews': self.total_reviews,
            'awards': self.awards
        }
        
        # Información específica por formato
        if self.format in [BookFormat.EBOOK]:
            info.update({
                'file_format': self.file_format,
                'file_size_mb': str(self.file_size_mb) if self.file_size_mb else None,
                'drm_protected': self.drm_protected
            })
        
        elif self.format == BookFormat.AUDIOBOOK:
            info.update({
                'narrator': self.narrator,
                'duration_minutes': self.duration_minutes,
                'file_format': self.file_format
            })
        
        return info
    
    def add_chapter(self, chapter_title: str) -> None:
        """Añadir capítulo al libro"""
        if chapter_title and chapter_title not in self.chapters:
            self.chapters.append(chapter_title)
    
    def add_award(self, award: str) -> None:
        """Añadir premio al libro"""
        if award and award not in self.awards:
            self.awards.append(award)
    
    def update_rating(self, new_rating: Decimal, review_count: int = 1) -> None:
        """
        Actualizar calificación promedio del libro
        
        Args:
            new_rating (Decimal): Nueva calificación
            review_count (int): Número de nuevas reseñas
        """
        if self.average_rating is None:
            self.average_rating = new_rating
            self.total_reviews = review_count
        else:
            total_points = self.average_rating * self.total_reviews + new_rating * review_count
            self.total_reviews += review_count
            self.average_rating = total_points / self.total_reviews
    
    def is_academic(self) -> bool:
        """Verificar si es un libro académico"""
        academic_genres = [BookGenre.TEXTBOOK, BookGenre.REFERENCE]
        academic_audiences = ['academic', 'graduate', 'undergraduate']
        
        return (self.genre in academic_genres or 
                self.target_audience in academic_audiences or
                'textbook' in self.keywords or
                'academic' in self.keywords)
    
    def is_children_book(self) -> bool:
        """Verificar si es un libro para niños"""
        return (self.genre == BookGenre.CHILDREN or
                self.target_audience == 'children' or
                'children' in self.keywords)
    
    def get_estimated_reading_time(self) -> Optional[int]:
        """
        Estimar tiempo de lectura en minutos
        Basado en 200-250 palabras por minuto promedio
        """
        if not self.pages:
            return None
        
        # Estimación: 250 palabras por página, 200 palabras por minuto
        estimated_words = self.pages * 250
        reading_time_minutes = estimated_words / 200
        
        return int(reading_time_minutes)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Book':
        """Crear libro desde diccionario"""
        book = cls(
            title=data['title'],
            isbn=data['isbn_or_id'],
            acquisition_date=date.fromisoformat(data['acquisition_date'])
        )
        
        # Aplicar datos del diccionario
        for key, value in data.items():
            if hasattr(book, key) and value is not None:
                if key == 'genre':
                    book.genre = BookGenre(value)
                elif key == 'format':
                    book.format = BookFormat(value)
                elif key in ['average_rating', 'file_size_mb']:
                    setattr(book, key, Decimal(value) if value else None)
                else:
                    setattr(book, key, value)
        
        return book
    
    def __str__(self) -> str:
        """Representación en string del libro"""
        authors_str = ", ".join(self.authors) if self.authors else "Unknown Author"
        format_str = f" ({self.format.value.title()})" if self.format != BookFormat.PAPERBACK else ""
        return f"'{self.title}' by {authors_str}{format_str}"
```

### 📋 3. Servicios de Negocio

#### `services/loan_service.py`
```python
"""
Servicio para gestión de préstamos
Maneja toda la lógica de negocio relacionada con préstamos de recursos
"""

from datetime import datetime, date, timedelta
from typing import List, Optional, Dict, Any, Tuple
from decimal import Decimal

from ..models.loan import Loan, LoanStatus
from ..models.user import User, UserType
from ..models.resource import Resource, ResourceStatus
from ..repositories.loan_repository import LoanRepository
from ..repositories.user_repository import UserRepository
from ..repositories.resource_repository import ResourceRepository
from ..exceptions.library_exceptions import (
    LoanError, ResourceNotAvailableError, UserNotEligibleError,
    LoanNotFoundError, LoanAlreadyReturnedError
)
from ..utils.date_helpers import calculate_due_date, is_library_open_day
from ..config.settings import get_setting

class LoanService:
    """
    Servicio para gestión de préstamos de la biblioteca
    
    Maneja toda la lógica de negocio relacionada con:
    - Crear nuevos préstamos
    - Renovar préstamos existentes
    - Procesar devoluciones
    - Calcular multas por retraso
    - Generar reportes de préstamos
    """
    
    def __init__(self, loan_repository: LoanRepository, 
                 user_repository: UserRepository,
                 resource_repository: ResourceRepository):
        """
        Inicializar servicio de préstamos
        
        Args:
            loan_repository (LoanRepository): Repositorio de préstamos
            user_repository (UserRepository): Repositorio de usuarios
            resource_repository (ResourceRepository): Repositorio de recursos
        """
        self._loan_repo = loan_repository
        self._user_repo = user_repository
        self._resource_repo = resource_repository
    
    def create_loan(self, user_id: str, resource_id: str, 
                   librarian_id: str = None) -> Loan:
        """
        Crear nuevo préstamo
        
        Args:
            user_id (str): ID del usuario
            resource_id (str): ID del recurso
            librarian_id (str, optional): ID del bibliotecario que procesa
        
        Returns:
            Loan: Préstamo creado
            
        Raises:
            UserNotEligibleError: Si el usuario no puede tomar préstamos
            ResourceNotAvailableError: Si el recurso no está disponible
            LoanError: Si hay otros problemas con el préstamo
        """
        # Obtener usuario y recurso
        user = self._user_repo.find_by_id(user_id)
        if not user:
            raise LoanError(f"User with ID {user_id} not found")
        
        resource = self._resource_repo.find_by_id(resource_id)
        if not resource:
            raise LoanError(f"Resource with ID {resource_id} not found")
        
        # Validar elegibilidad del usuario
        self._validate_user_eligibility(user)
        
        # Validar disponibilidad del recurso
        self._validate_resource_availability(resource)
        
        # Verificar límites de préstamo
        self._check_loan_limits(user, resource)
        
        # Calcular fechas del préstamo
        loan_date = datetime.now()
        loan_duration = resource.get_loan_duration_days()
        due_date = calculate_due_date(loan_date, loan_duration)
        
        # Crear préstamo
        loan = Loan(
            user_id=user_id,
            resource_id=resource_id,
            loan_date=loan_date,
            due_date=due_date,
            librarian_id=librarian_id
        )
        
        # Guardar préstamo
        saved_loan = self._loan_repo.save(loan)
        
        # Actualizar estado del recurso
        resource.record_loan()
        self._resource_repo.save(resource)
        
        # Actualizar estadísticas del usuario
        user.record_loan()
        self._user_repo.save(user)
        
        return saved_loan
    
    def renew_loan(self, loan_id: str, librarian_id: str = None) -> Loan:
        """
        Renovar préstamo existente
        
        Args:
            loan_id (str): ID del préstamo
            librarian_id (str, optional): ID del bibliotecario
        
        Returns:
            Loan: Préstamo renovado
            
        Raises:
            LoanNotFoundError: Si el préstamo no existe
            LoanError: Si no se puede renovar
        """
        loan = self._loan_repo.find_by_id(loan_id)
        if not loan:
            raise LoanNotFoundError(f"Loan with ID {loan_id} not found")
        
        if loan.status != LoanStatus.ACTIVE:
            raise LoanError("Can only renew active loans")
        
        # Verificar si se puede renovar
        if loan.renewals >= loan.max_renewals:
            raise LoanError(f"Maximum renewals ({loan.max_renewals}) reached")
        
        # Obtener usuario y recurso
        user = self._user_repo.find_by_id(loan.user_id)
        resource = self._resource_repo.find_by_id(loan.resource_id)
        
        # Verificar elegibilidad del usuario
        self._validate_user_eligibility(user)
        
        # Verificar que no haya reservas pendientes
        if self._has_pending_reservations(resource):
            raise LoanError("Cannot renew: resource has pending reservations")
        
        # Calcular nueva fecha de vencimiento
        current_due_date = loan.due_date
        extension_days = resource.get_loan_duration_days()
        new_due_date = calculate_due_date(current_due_date, extension_days)
        
        # Actualizar préstamo
        loan.renew(new_due_date, librarian_id)
        
        # Guardar cambios
        updated_loan = self._loan_repo.save(loan)
        
        return updated_loan
    
    def return_resource(self, loan_id: str, librarian_id: str = None,
                       condition_notes: str = "") -> Tuple[Loan, Optional[Decimal]]:
        """
        Procesar devolución de recurso
        
        Args:
            loan_id (str): ID del préstamo
            librarian_id (str, optional): ID del bibliotecario
            condition_notes (str): Notas sobre condición del recurso
        
        Returns:
            Tuple[Loan, Optional[Decimal]]: Préstamo y multa por retraso
            
        Raises:
            LoanNotFoundError: Si el préstamo no existe
            LoanAlreadyReturnedError: Si ya fue devuelto
        """
        loan = self._loan_repo.find_by_id(loan_id)
        if not loan:
            raise LoanNotFoundError(f"Loan with ID {loan_id} not found")
        
        if loan.status != LoanStatus.ACTIVE:
            raise LoanAlreadyReturnedError("Loan is already returned or cancelled")
        
        # Obtener recurso
        resource = self._resource_repo.find_by_id(loan.resource_id)
        
        # Procesar devolución
        return_date = datetime.now()
        late_fee = None
        
        # Calcular multa por retraso si aplica
        if return_date.date() > loan.due_date.date():
            days_overdue = (return_date.date() - loan.due_date.date()).days
            late_fee = resource.calculate_late_fee(days_overdue)
        
        # Actualizar préstamo
        loan.return_resource(return_date, late_fee, librarian_id, condition_notes)
        
        # Actualizar estado del recurso
        resource.record_return()
        
        # Si hay notas de condición, actualizarlas
        if condition_notes:
            resource.notes += f"\\n{return_date.strftime('%Y-%m-%d')}: Return condition - {condition_notes}"
        
        # Guardar cambios
        self._loan_repo.save(loan)
        self._resource_repo.save(resource)
        
        # Actualizar estadísticas del usuario
        user = self._user_repo.find_by_id(loan.user_id)
        if late_fee and late_fee > 0:
            user.add_fine(late_fee)
            self._user_repo.save(user)
        
        return loan, late_fee
    
    def get_active_loans_by_user(self, user_id: str) -> List[Loan]:
        """Obtener préstamos activos de un usuario"""
        return self._loan_repo.find_by_user_and_status(user_id, LoanStatus.ACTIVE)
    
    def get_overdue_loans(self, as_of_date: date = None) -> List[Loan]:
        """
        Obtener préstamos vencidos
        
        Args:
            as_of_date (date): Fecha de referencia (por defecto hoy)
        
        Returns:
            List[Loan]: Lista de préstamos vencidos
        """
        check_date = as_of_date or date.today()
        return self._loan_repo.find_overdue_loans(check_date)
    
    def get_loans_due_soon(self, days_ahead: int = 3) -> List[Loan]:
        """
        Obtener préstamos que vencen pronto
        
        Args:
            days_ahead (int): Días hacia adelante para verificar
        
        Returns:
            List[Loan]: Lista de préstamos que vencen pronto
        """
        future_date = date.today() + timedelta(days=days_ahead)
        return self._loan_repo.find_loans_due_between(date.today(), future_date)
    
    def calculate_user_fines(self, user_id: str) -> Decimal:
        """
        Calcular multas totales de un usuario
        
        Args:
            user_id (str): ID del usuario
        
        Returns:
            Decimal: Monto total de multas
        """
        active_loans = self.get_active_loans_by_user(user_id)
        total_fines = Decimal('0.00')
        
        for loan in active_loans:
            if loan.is_overdue():
                resource = self._resource_repo.find_by_id(loan.resource_id)
                days_overdue = loan.get_days_overdue()
                fine = resource.calculate_late_fee(days_overdue)
                total_fines += fine
        
        return total_fines
    
    def get_loan_statistics(self, start_date: date = None, 
                           end_date: date = None) -> Dict[str, Any]:
        """
        Generar estadísticas de préstamos
        
        Args:
            start_date (date): Fecha de inicio
            end_date (date): Fecha de fin
        
        Returns:
            Dict[str, Any]: Estadísticas de préstamos
        """
        if not start_date:
            start_date = date.today() - timedelta(days=30)
        if not end_date:
            end_date = date.today()
        
        loans = self._loan_repo.find_by_date_range(start_date, end_date)
        
        if not loans:
            return {
                'total_loans': 0,
                'period': f"{start_date} to {end_date}"
            }
        
        # Calcular estadísticas
        total_loans = len(loans)
        returned_loans = len([l for l in loans if l.status == LoanStatus.RETURNED])
        overdue_loans = len([l for l in loans if l.is_overdue()])
        renewed_loans = len([l for l in loans if l.renewals > 0])
        
        # Calcular multas
        total_fines = sum(l.late_fee or Decimal('0') for l in loans)
        
        # Recursos más prestados
        resource_counts = {}
        for loan in loans:
            resource_counts[loan.resource_id] = resource_counts.get(loan.resource_id, 0) + 1
        
        most_loaned_resource = max(resource_counts.items(), key=lambda x: x[1]) if resource_counts else None
        
        return {
            'period': f"{start_date} to {end_date}",
            'total_loans': total_loans,
            'returned_loans': returned_loans,
            'return_rate': (returned_loans / total_loans * 100) if total_loans > 0 else 0,
            'overdue_loans': overdue_loans,
            'overdue_rate': (overdue_loans / total_loans * 100) if total_loans > 0 else 0,
            'renewed_loans': renewed_loans,
            'renewal_rate': (renewed_loans / total_loans * 100) if total_loans > 0 else 0,
            'total_fines': str(total_fines),
            'average_fine': str(total_fines / overdue_loans) if overdue_loans > 0 else '0.00',
            'most_loaned_resource_id': most_loaned_resource[0] if most_loaned_resource else None,
            'most_loaned_count': most_loaned_resource[1] if most_loaned_resource else 0
        }
    
    def _validate_user_eligibility(self, user: User) -> None:
        """Validar si el usuario puede tomar préstamos"""
        if not user.is_active:
            raise UserNotEligibleError("User account is not active")
        
        if user.account_status == "suspended":
            raise UserNotEligibleError("User account is suspended")
        
        # Verificar multas pendientes
        max_fines = Decimal(str(get_setting('library.max_outstanding_fines', 50.00)))
        if user.outstanding_fines > max_fines:
            raise UserNotEligibleError(f"Outstanding fines exceed limit: ${user.outstanding_fines}")
        
        # Verificar límite de préstamos
        active_loans = len(self.get_active_loans_by_user(user.id))
        max_loans = user.get_max_loans()
        
        if active_loans >= max_loans:
            raise UserNotEligibleError(f"User has reached maximum loans limit ({max_loans})")
    
    def _validate_resource_availability(self, resource: Resource) -> None:
        """Validar si el recurso está disponible"""
        if not resource.is_loanable:
            raise ResourceNotAvailableError(f"Resource is not available for loan. Status: {resource.status.value}")
    
    def _check_loan_limits(self, user: User, resource: Resource) -> None:
        """Verificar límites específicos de préstamo"""
        # Aquí se pueden agregar validaciones específicas
        # como límites por tipo de recurso, tipo de usuario, etc.
        pass
    
    def _has_pending_reservations(self, resource: Resource) -> bool:
        """Verificar si el recurso tiene reservas pendientes"""
        # Esta lógica se implementaría consultando el servicio de reservas
        # Por ahora retornamos False
        return False
```

---

## 🎯 Objetivos del Desafío

### 🏗️ Requisitos Técnicos Obligatorios

#### 1. **Arquitectura Modular** (25 puntos)
- [ ] Estructura de directorios bien organizada
- [ ] Separación clara de responsabilidades (models, services, repositories)
- [ ] Configuración centralizada y flexible
- [ ] Sistema de plugins funcional
- [ ] Imports relativos y absolutos correctos

#### 2. **Modelos y Datos** (25 puntos)
- [ ] Jerarquía de clases Resource con al menos 3 tipos
- [ ] Modelos User con diferentes tipos y permisos
- [ ] Sistema de préstamos y reservas completo
- [ ] Validación de datos robusta
- [ ] Serialización/deserialización consistente

#### 3. **Servicios de Negocio** (25 puntos)
- [ ] Lógica de negocio encapsulada en servicios
- [ ] Manejo de errores personalizado
- [ ] Validaciones de reglas de negocio
- [ ] Cálculo de multas y fechas
- [ ] Generación de reportes y estadísticas

#### 4. **Funcionalidad Completa** (25 puntos)
- [ ] CLI funcional para administradores y usuarios
- [ ] Sistema de búsqueda avanzada
- [ ] Notificaciones automatizadas
- [ ] Tests unitarios comprehensivos
- [ ] Documentación completa

---

## 🎮 Casos de Uso para Probar

### 📝 Script de Demostración
```python
def main():
    """Demostración completa del sistema de biblioteca"""
    
    # Inicializar sistema
    from digital_library import LibrarySystem
    
    library = LibrarySystem()
    
    # Crear usuarios
    admin = library.user_service.create_user(
        username="admin",
        email="admin@library.com",
        user_type=UserType.ADMIN,
        full_name="System Administrator"
    )
    
    librarian = library.user_service.create_user(
        username="librarian1",
        email="librarian@library.com", 
        user_type=UserType.LIBRARIAN,
        full_name="Jane Smith"
    )
    
    student = library.user_service.create_user(
        username="student1",
        email="student@university.edu",
        user_type=UserType.STUDENT,
        full_name="John Doe"
    )
    
    # Crear recursos
    book1 = library.resource_service.create_book(
        title="Python Programming",
        isbn="978-0123456789",
        authors=["Jane Author"],
        genre=BookGenre.TECHNOLOGY
    )
    
    ebook = library.resource_service.create_ebook(
        title="Digital Libraries",
        isbn="978-9876543210", 
        file_format="pdf",
        file_size_mb=15.5
    )
    
    # Procesar préstamos
    loan1 = library.loan_service.create_loan(
        user_id=student.id,
        resource_id=book1.id,
        librarian_id=librarian.id
    )
    
    print(f"Loan created: {loan1}")
    
    # Crear reservas
    reservation = library.reservation_service.create_reservation(
        user_id=student.id,
        resource_id=ebook.id
    )
    
    print(f"Reservation created: {reservation}")
    
    # Generar reportes
    stats = library.report_service.generate_library_statistics()
    print(f"Library Statistics: {stats}")
    
    # Demostrar búsqueda
    search_results = library.resource_service.search_resources(
        query="python",
        filters={'resource_type': 'book'}
    )
    
    print(f"Search results: {len(search_results)} items found")
    
    # Simular devolución
    returned_loan, late_fee = library.loan_service.return_resource(
        loan_id=loan1.id,
        librarian_id=librarian.id
    )
    
    print(f"Resource returned. Late fee: ${late_fee or 0}")

if __name__ == "__main__":
    main()
```

---

## ✅ Criterios de Evaluación Detallados

### 🎖️ Rubrica de Evaluación

#### **Excelente (90-100 puntos)**
- Arquitectura modular impecable y extensible
- Código limpio siguiendo todas las mejores prácticas
- Tests comprehensivos con alta cobertura
- Documentación profesional completa
- Funcionalidades adicionales creativas

#### **Bueno (75-89 puntos)**
- Arquitectura modular bien implementada
- Código bien estructurado y documentado
- Tests básicos funcionando
- Funcionalidad completa operativa

#### **Satisfactorio (60-74 puntos)**
- Estructura modular básica correcta
- Funcionalidad principal funcionando
- Documentación básica presente
- Algunos tests implementados

#### **Necesita Mejora (0-59 puntos)**
- Arquitectura modular mal implementada
- Funcionalidad incompleta o con errores
- Documentación insuficiente
- Tests faltantes o fallando

---

## 🚀 Extensiones Opcionales (Puntos Extra)

### 🌟 Funcionalidades Adicionales
1. **API REST** (15 puntos)
   - Endpoints RESTful para todas las operaciones
   - Autenticación JWT
   - Documentación OpenAPI/Swagger

2. **Sistema de Plugins Avanzado** (15 puntos)
   - Carga dinámica de plugins
   - Sistema de hooks y eventos
   - Marketplace de plugins

3. **Interfaz Web** (15 puntos)
   - Dashboard para administradores
   - Portal para usuarios
   - Diseño responsive

4. **Integración Externa** (10 puntos)
   - APIs de bibliotecas externas
   - Sistemas de catalogación
   - Servicios de notificación

### 🎨 Mejoras Técnicas
- Sistema de caché distribuido
- Base de datos real (PostgreSQL/MongoDB)
- Containerización con Docker
- CI/CD automatizado
- Monitoreo y logging avanzado

---

## 📚 Recursos de Apoyo

### 🔍 Patrones a Implementar
- **Repository Pattern**: Abstracción de acceso a datos
- **Service Layer**: Lógica de negocio centralizada
- **Factory Pattern**: Creación de recursos
- **Observer Pattern**: Sistema de eventos
- **Strategy Pattern**: Diferentes algoritmos de cálculo

### 🛠️ Herramientas Recomendadas
```python
# Para testing
import unittest
import pytest
import coverage

# Para documentación  
import sphinx
import mkdocs

# Para validación
import pydantic
import cerberus

# Para configuración
import configparser
import python-decouple
```

---

## 🎯 Entregables

### 📁 Estructura de Entrega
```
submission/
├── digital_library/          # Código fuente
├── tests/                    # Tests completos
├── docs/                     # Documentación
├── config/                   # Archivos de configuración
├── requirements.txt          # Dependencias
├── setup.py                  # Instalación
├── README.md                 # Guía principal
├── ARCHITECTURE.md           # Documentación de arquitectura
└── DEMO.md                   # Guía de demostración
```

### 📋 Documentación Requerida
1. **README.md**: Instalación y uso básico
2. **ARCHITECTURE.md**: Decisiones de diseño y estructura
3. **API.md**: Documentación de APIs públicas
4. **USER_GUIDE.md**: Manual de usuario
5. **DEVELOPER_GUIDE.md**: Guía para desarrolladores

---

**🏆 Meta Final**: Crear un sistema de biblioteca que demuestre dominio completo de arquitectura modular, patrones de diseño, y mejores prácticas de desarrollo de software.

**💡 Consejo Principal**: Enfócate en crear un sistema que sea fácil de mantener, extender y entender. La arquitectura modular debe hacer que añadir nuevas funcionalidades sea intuitivo.

**🎮 ¡Que comience la construcción de tu biblioteca digital!** 📚🏗️💻
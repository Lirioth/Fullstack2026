# 🚀 Day 5 - Mini Project: Integrating OOP and Data Concepts

## 🎯 Goal of the Day

Develop a **complete project** that integrates all the concepts learned during the week:
- Advanced object-oriented programming
- Modular organization and packages
- File and external data handling (CSV, JSON, APIs)
- Validation, testing, and documentation

---

## 🏆 Main Challenge: "Comprehensive Digital Library Management System"

### 📚 General Description
Create a digital library system that allows you to:
- Manage users, books, loans, and returns
- Integrate book data from CSV files and external APIs (e.g., Google Books)
- Store and query information in JSON files
- Generate usage reports and statistics
- Validate data and handle errors robustly

---

## 🏗️ Suggested Architecture

```
Day5MiniProject/
├── data/
│   ├── books.csv
│   ├── users.json
│   └── loans.json
├── src/
│   ├── models/
│   │   ├── user.py
│   │   ├── book.py
│   │   └── loan.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── book_service.py
│   │   └── loan_service.py
│   ├── api/
│   │   └── google_books.py
│   ├── utils/
│   │   ├── validators.py
│   │   └── file_manager.py
│   ├── main.py
│   └── report.py
├── tests/
│   ├── test_users.py
│   ├── test_books.py
│   └── test_loans.py
└── README.md
```

---

## 📋 Technical Requirements

- Implement OOP classes for users, books, and loans
- Read and load book data from CSV and/or external API
- Store users and loans in JSON
- Validate input data and handle errors
- Generate reports for most borrowed books, active users, etc.
- Unit testing for main modules
- Document the system and its modules

---

## 📝 Suggested Workflow

1. **Class and Module Design**: Define the main classes and their relationships.
2. **Data Loading**: Implement book import from CSV and API.
3. **User and Loan Management**: Methods for adding, removing, loaning, and returning.
4. **Persistence**: Save and load data in JSON.
5. **Reports**: Generate useful reports and statistics.
6. **Testing**: Create unit tests for key modules.
7. **Documentation**: Explain the design, usage, and decisions.

---

## ✅ Evaluation Criteria
- [ ] Integration of all weekly concepts
- [ ] Modular, clean, and well-documented code
- [ ] Robust validation and error handling
- [ ] Functional testing
- [ ] Useful and well-presented reports

---

**💡 Tip**: Prioritize clarity and maintainability. Document each module and justify your design decisions.

**🎯 Goal**: Deliver a functional, professional, and well-documented system that demonstrates mastery of OOP, data handling, and development best practices.
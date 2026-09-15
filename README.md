# pure_python_streak

![Status](https://img.shields.io/badge/status-In%20Progress-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Pure Python Advanced Streak - 7 Projects in 7 Days

This repository contains 7 working Python projects built using **pure Python only**. No Pandas. No SQL. No external data libraries. Just classes, objects, APIs, and logic.

After building production-level bioinformatics projects, I'm returning to Python fundamentals to master core concepts: OOP, data structures, APIs, and file I/O—without relying on third-party libraries.

---

## 📋 Projects Overview

| # | Project | Core Concepts | Status |
|---|---------|--------------|--------|
| 1 | Library Management System | OOP, Classes, State Management, Error Handling | ⏳ |
| 2 | Weather Data Fetcher | API Integration, JSON Parsing, HTTP Requests | ⏳ |
| 3 | ETL Data Pipeline | Data Processing, Transformation, Pure Python | ⏳ |
| 4 | Task Scheduler with Priority Queue | Heaps, Priority Queues, Data Structures | ⏳ |
| 5 | Simple Web Scraper | HTML Parsing, Web Requests, Regex | ⏳ |
| 6 | Automated Report Generator | File I/O, String Formatting, Templates | ⏳ |
| 7 | Bioinformatics Tool Integrator | System Integration, Multi-tool Orchestration | ⏳ |

### Project Details

**1. Library Management System (OOP)**
- Demonstrates: Classes, objects, inheritance, encapsulation, state management
- Features: Add/borrow/return books, member management, exception handling
- Key Skills: try/except blocks, data validation

**2. Weather Data Fetcher (API)**
- Demonstrates: REST API integration, JSON parsing, error handling
- Features: Fetch real-time weather data from OpenWeatherMap API, format & display
- Key Skills: HTTP requests, JSON manipulation, API key management

**3. ETL Data Pipeline (Pure Python)**
- Demonstrates: Extract, Transform, Load without external libraries
- Features: Read data, apply transformations, output results
- Key Skills: File handling, data manipulation, algorithm design

**4. Task Scheduler with Priority Queue**
- Demonstrates: Heap data structure, priority queue implementation
- Features: Schedule tasks with priorities, execute in order
- Key Skills: Heap operations, task management, sorting algorithms

**5. Simple Web Scraper**
- Demonstrates: HTML parsing, web requests, regex patterns
- Features: Scrape website content, extract specific data
- Key Skills: HTML structure understanding, regex, request handling

**6. Automated Report Generator**
- Demonstrates: File I/O, string formatting, text generation
- Features: Generate formatted reports from data, save as text/markdown
- Key Skills: File operations, string manipulation, template generation

**7. Bioinformatics Tool Integrator**
- Demonstrates: System integration, combining multiple tools
- Features: Orchestrate previous projects into one cohesive system
- Key Skills: Architecture design, modular programming, integration patterns

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- `requests` library (for API and web scraping projects)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/CodeXSourabhsingh/pure_python_streak.git
cd pure_python_streak

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if needed)
pip install requests
```

### Running a Project

```bash
# Run any project
python3 1_library_management.py
python3 2_weather_fetcher.py
# ... and so on
```

---

## 📁 Project Structure

```
pure_python_streak/
├── 1_library_management.py
├── 2_weather_fetcher.py
├── 3_etl_pipeline.py
├── 4_task_scheduler.py
├── 5_web_scraper.py
├── 6_report_generator.py
├── 7_bioinformatics_integrator.py
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Paradigm**: Object-Oriented Programming, Functional Programming
- **Libraries**: Pure Python + `requests` (for API calls)
- **No**: Pandas, SQL, NumPy, Django, or other abstractions
- **Version Control**: Git / GitHub

---

## 💡 Learning Outcomes

By exploring this repository, you'll understand:

✅ **Object-Oriented Programming** - Classes, inheritance, encapsulation, polymorphism  
✅ **Data Structures** - Lists, dictionaries, heaps, queues  
✅ **APIs & HTTP** - Making requests, parsing JSON, error handling  
✅ **File I/O** - Reading, writing, and processing files  
✅ **Algorithm Design** - Priority queues, sorting, searching  
✅ **Error Handling** - try/except, custom exceptions  
✅ **Web Scraping** - HTML parsing, regex patterns  
✅ **System Design** - Integrating multiple modules into cohesive systems  

---

## 📖 Usage Examples

### Library Management System
```python
from library_management import Library, Member

lib = Library()
lib.add_book("The Hobbit", "J.R.R. Tolkien")
lib.add_member("Sourabh", "M001")

lib.borrow_book("M001", "The Hobbit")
lib.return_book("M001", "The Hobbit")
```

### Weather Data Fetcher
```python
from weather_fetcher import WeatherFetcher

fetcher = WeatherFetcher(api_key="your_api_key")
weather = fetcher.get_weather("London")
print(weather)
```

### ETL Pipeline
```python
from etl_pipeline import ETLPipeline

pipeline = ETLPipeline("input_data.csv")
pipeline.extract()
pipeline.transform()
pipeline.load("output_data.csv")
```

---

## 🧬 Purpose

After spending 6 days building 10 advanced bioinformatics projects with heavy library dependencies, I realized the importance of **mastering fundamentals**. This challenge rebuilds my Python foundation using:

- **Pure logic** instead of library shortcuts
- **Core data structures** instead of abstractions
- **First principles thinking** to deeply understand how systems work

This isn't about being anti-library. It's about building a solid foundation so that when I *do* use libraries, I understand what's happening under the hood.

---

## 📊 Progress Tracker

- [ ] Project 1 - Library Management System
- [ ] Project 2 - Weather Data Fetcher
- [ ] Project 3 - ETL Data Pipeline
- [ ] Project 4 - Task Scheduler
- [ ] Project 5 - Web Scraper
- [ ] Project 6 - Report Generator
- [ ] Project 7 - Bioinformatics Integrator

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Sourabh Singh**
- 🔗 [LinkedIn](https://www.linkedin.com/in/sourabh-singh-7b124934/)
- 🐙 [GitHub](https://github.com/CodeXSourabhsingh)
- 📧 Email: [Add your email if you want]

---

## 🙏 Acknowledgments

This challenge is inspired by the principle of **learning fundamentals deeply** before applying advanced concepts. Thanks to everyone who believes in building strong foundations.

---

**Last Updated**: September 2026  
**Streak Days Completed**: 0/7 ✨

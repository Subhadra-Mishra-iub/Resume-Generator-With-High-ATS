# 🎯 ATS Resume Optimizer

**Generate highly optimized resumes tailored to specific job descriptions**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

- **90%+ ATS Compatibility**: Automatically optimized for Applicant Tracking Systems
- **Job-Specific Optimization**: Tailors content based on job description keywords
- **Professional Formatting**: Always generates exactly 1-page resumes
- **Multiple Job Types**: Supports Software Engineer, Data Engineer, Data Analyst roles
- **LaTeX Output**: Professional formatting ready for Overleaf compilation

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Download required NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Usage
1. **Edit job description**: Open `quick_optimizer.py` and replace the job description
2. **Run optimizer**: `python quick_optimizer.py`
3. **Get resume**: Upload generated `.tex` file to [Overleaf](https://overleaf.com)
4. **Compile to PDF**: Ready for job applications!

## 📁 Project Structure

```
resume-optimizer/
├── quick_optimizer.py      # Main interface (edit this)
├── resume_optimizer.py     # Core optimization engine
├── requirements.txt        # Dependencies
├── USAGE_GUIDE.md         # Detailed usage instructions
└── src/                   # Your LaTeX resume sections
    ├── heading.tex        # Contact information
    ├── education.tex      # Education background
    ├── skills.tex         # Technical skills
    ├── experience.tex     # Work experience
    └── projects.tex       # Projects
```

## 🎯 Optimization Features

- **Automatic Job Type Detection**: Identifies role type from job description
- **Strategic Keyword Placement**: Incorporates relevant terms naturally
- **Content Enhancement**: Improves descriptions without fabricating experience
- **Format Enforcement**: Max 2 lines per bullet point, compact headings
- **Project Selection**: Chooses 3 most relevant projects automatically

## 📊 Expected Results

- **ATS Scores**: 85-95% compatibility
- **Processing Time**: 30 seconds per optimization
- **Format**: Professional 1-page LaTeX resume
- **Accuracy**: 100% based on actual experience

## 🔧 Supported Job Types

- **Software Engineer**: Web development, APIs, frontend/backend
- **Data Engineer**: Data pipelines, ETL, cloud platforms
- **Data Analyst**: Analytics, visualization, business intelligence
- **General**: Flexible optimization for other roles

## 📖 Documentation

For detailed usage instructions, examples, and troubleshooting, see [USAGE_GUIDE.md](USAGE_GUIDE.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Subhadra Mishra**
- GitHub: [@Subhadra-Mishra-iub](https://github.com/Subhadra-Mishra-iub)
- LinkedIn: [subhadra-mishra](https://linkedin.com/in/subhadra-mishra)

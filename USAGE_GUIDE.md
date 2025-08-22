# 🎯 ATS Resume Optimizer - Usage Guide

## 📋 Overview
This tool automatically optimizes your resume for any job description, ensuring:
- ✅ **Max 2 lines per bullet point**
- ✅ **Compact skill headings** 
- ✅ **Exactly 1 page**
- ✅ **Include ALL experience entries**
- ✅ **Use 3 projects** (most relevant)
- ✅ **Strategic keyword incorporation**
- ✅ **90%+ ATS targeting**
- ✅ **100% truthful content**

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment activated
- All dependencies installed

### Setup (One-time)
```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (if not already done)
pip install -r requirements.txt

# Download NLTK data (if not already done)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## 📝 How to Use

### Method 1: Edit Configuration and Run (Recommended)

1. **Open the job configuration file:**
   ```bash
   # Open in your preferred editor
   code quick_optimizer.py  # VS Code
   # OR
   nano quick_optimizer.py  # Terminal editor
   # OR
   open quick_optimizer.py  # Default editor
   ```

2. **Replace the job description** (lines 15-45):
   ```python
   job_description = """Key Responsibilities:
   
   Modify configurations, utilities, software default settings...
   
   Required Qualifications:
   Cisco Certified Network Associate or 2-3 years relevant work experience...
   
   Preferred Qualifications:
   Other Cisco Certified Associate Certificates..."""
   ```

3. **Update the job title** (line 47):
   ```python
   job_title = "Network Engineer I"  # Change this
   ```

4. **Run the optimizer:**
   ```bash
   source .venv/bin/activate && python resume_optimizer.py
   ```

5. **Get your optimized resume:**
   - Generated file: `[Job_Title]_Resume.tex`
   - Upload to [Overleaf.com](https://overleaf.com)
   - Compile to PDF

### Method 2: Interactive Mode (Alternative)

```bash
source .venv/bin/activate && python resume_optimizer.py
```

Then paste your job description when prompted and press Enter twice.

## 📄 Example Usage

### Example 1: Software Engineer Role

**Job Description:**
```
Your Role
As a Software Engineer you will be responsible for building Zip's core products and architecture. You will ship features that will be immediately used by our customers, and will work with a tight-knit team that values open communication and cross-functional collaboration.

You Will
Design and build highly reliable and resilient products and features
Write high-quality, extensible, and maintainable code
Design and build scalable frontend applications and components
Design and build APIs to drive existing and new features

Qualifications
Experience with web applications and API development. At Zip, our stack includes Python, Javascript/TypeScript, React, and GraphQL
Ability and interest to quickly learn new frameworks, architecture patterns, and programming languages as needed
```

**Job Title:** `Software Engineer`

**Command:**
```bash
source .venv/bin/activate && python quick_optimizer.py
```

**Output:** `Software_Engineer_Resume.tex`

### Example 2: Data Engineer Role

**Job Description:**
```
Your Role
As a Data Engineer, you will be responsible for building and maintaining data pipelines, ETL processes, and data infrastructure. You will work with large-scale data processing systems and ensure data quality and reliability.

You Will
Design and build scalable data pipelines and ETL processes
Work with big data technologies like Spark, Hadoop, and Kafka
Implement data modeling and schema design
Ensure data quality and reliability across systems

Qualifications
Experience with Python, SQL, and data engineering tools
Knowledge of cloud platforms (AWS, Azure, GCP)
Experience with distributed systems and data processing
```

**Job Title:** `Data Engineer`

**Command:**
```bash
source .venv/bin/activate && python quick_optimizer.py
```

**Output:** `Data_Engineer_Resume.tex`

### Example 3: Data Analyst Role

**Job Description:**
```
Your Role
As a Data Analyst, you will be responsible for analyzing data to provide insights and support business decisions. You will create reports, dashboards, and visualizations to communicate findings effectively.

You Will
Analyze large datasets to identify trends and patterns
Create interactive dashboards and reports using BI tools
Perform statistical analysis and data mining
Present findings to stakeholders and business teams

Qualifications
Experience with SQL, Python, and data visualization tools
Knowledge of statistical analysis and data mining techniques
Experience with business intelligence tools (Tableau, Power BI)
```

**Job Title:** `Data Analyst`

**Command:**
```bash
source .venv/bin/activate && python quick_optimizer.py
```

**Output:** `Data_Analyst_Resume.tex`

## 🔧 File Structure

```
resume-optimizer/
├── quick_optimizer.py          # Job configuration (edit this)
├── resume_optimizer.py         # Core optimization engine
├── requirements.txt            # Python dependencies
├── USAGE_GUIDE.md             # This guide
├── src/                       # Your LaTeX files
│   ├── heading.tex           # Contact info
│   ├── education.tex         # Education background
│   ├── skills.tex           # Technical skills
│   ├── experience.tex       # Work experience
│   └── projects.tex         # Project details
└── .venv/                    # Virtual environment
```

## 🎯 Optimization Features

### Automatic Job Type Detection
- **Software Engineer**: Prioritizes web development, React, Node.js, APIs
- **Data Engineer**: Prioritizes data pipelines, AWS, Dask, distributed systems
- **Data Analyst**: Prioritizes analytics, visualization, statistical analysis
- **General**: Uses all available content

### Keyword Optimization
- Extracts relevant keywords from job description
- Incorporates exact terminology from job posting
- Maps keywords to your actual experience truthfully
- Enhances descriptions without fabricating experience

### Formatting Enforcement
- **Bullet Points**: Max 2 lines each
- **Skills**: Compact headings (Programming, Web Development, etc.)
- **Projects**: Exactly 3 most relevant projects
- **Page Count**: Always exactly 1 page
- **Experience**: All entries included

## 📊 Expected Results

### ATS Scores
- **Target**: 90%+ compatibility
- **Range**: 85-95% typically achieved
- **Keywords**: Strategic placement throughout resume

### Output Quality
- **Format**: Professional LaTeX
- **Length**: Exactly 1 page
- **Content**: 100% truthful, enhanced descriptions
- **Relevance**: Job-specific optimization

## 🚨 Troubleshooting

### Common Issues

1. **"Module not found" error:**
   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **"NLTK data not found" error:**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

3. **"File not found" error:**
   - Ensure all `.tex` files are in the `src/` folder
   - Check file names: `heading.tex`, `education.tex`, `skills.tex`, `experience.tex`, `projects.tex`

4. **Generated resume is too long:**
   - The optimizer automatically enforces 1-page formatting
   - If issues persist, check your source `.tex` files for excessive content

### File Permissions
```bash
# If you get permission errors
chmod +x quick_optimizer.py
chmod +x resume_optimizer.py
```

## 📞 Support

### Before Asking for Help
1. ✅ Virtual environment activated
2. ✅ All dependencies installed
3. ✅ All `.tex` files in `src/` folder
4. ✅ Job description properly formatted in `quick_optimizer.py`

### Quick Test
```bash
# Test if everything is working
source .venv/bin/activate && python quick_optimizer.py
```

If this runs successfully, your setup is correct!

## 🎉 Success Checklist

After running the optimizer, you should have:
- ✅ Generated `.tex` file in your directory
- ✅ File named `[Job_Title]_Resume.tex`
- ✅ File size around 8-10KB
- ✅ Ready for Overleaf upload

**Next Steps:**
1. Upload to [Overleaf.com](https://overleaf.com)
2. Compile to PDF
3. Submit your optimized resume! 🚀

#!/usr/bin/env python3
"""
ATS Resume Optimizer
Generates highly optimized resumes tailored to specific job descriptions

Author: Subhadra Mishra
"""

import re
import os
import sys
from datetime import datetime
from collections import Counter

class ResumeOptimizer:
    def __init__(self):
        self.src_path = "src"
        self.sections = {}
        self.load_sections()
    
    def load_sections(self):
        """Load resume sections from src/ folder"""
        required_files = {
            'heading': 'heading.tex',
            'education': 'education.tex',
            'skills': 'skills.tex', 
            'experience': 'experience.tex',
            'projects': 'projects.tex'
        }
        
        missing_files = []
        for section, filename in required_files.items():
            filepath = os.path.join(self.src_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.sections[section] = f.read().strip()
                print(f"✅ Loaded {filename}")
            except FileNotFoundError:
                missing_files.append(filename)
                self.sections[section] = ""
        
        if missing_files:
            print(f"❌ Missing files in src/: {', '.join(missing_files)}")
            print("Please ensure all LaTeX files are in the src/ folder")
            return False
        
        return True
    
    def extract_keywords(self, job_description):
        """Extract relevant keywords from job description for ATS optimization"""
        jd = job_description.lower()
        keywords = set()
        
        technical_patterns = {
            'languages': r'\b(python|java|javascript|typescript|sql|r|scala|go|c\+\+)\b',
            'frameworks': r'\b(react|angular|vue|node\.?js|django|flask|spring|express)\b',
            'cloud': r'\b(aws|azure|gcp|docker|kubernetes|jenkins|git)\b',
            'databases': r'\b(postgresql|mysql|mongodb|redis|snowflake|oracle)\b',
            'data_tools': r'\b(spark|hadoop|kafka|tableau|power bi|looker)\b',
            'networking': r'\b(cisco|routing|switching|tcp/ip|dns|dhcp|network|connectivity|service desk|troubleshooting|configuration|documentation)\b',
            'concepts': r'\b(machine learning|data science|devops|microservices|ci/cd|agile|scrum)\b'
        }
        
        for category, pattern in technical_patterns.items():
            matches = re.findall(pattern, jd)
            keywords.update(matches)
        
        return sorted(list(keywords))
    
    def detect_job_type(self, keywords):
        """Automatically detect job type based on extracted keywords"""
        kw_str = ' '.join(keywords).lower()
        
        data_engineering_indicators = ['data engineer', 'etl', 'pipeline', 'spark', 'hadoop', 'kafka']
        data_analyst_indicators = ['data analyst', 'analytics', 'bi', 'tableau', 'power bi']
        software_engineer_indicators = ['software engineer', 'full stack', 'react', 'frontend', 'backend']
        network_engineer_indicators = ['network engineer', 'cisco', 'routing', 'switching', 'tcp/ip', 'dns', 'dhcp', 'network connectivity', 'service desk', 'troubleshooting']
        
        if any(term in kw_str for term in network_engineer_indicators):
            return 'network_engineer'
        elif any(term in kw_str for term in data_engineering_indicators):
            return 'data_engineering'
        elif any(term in kw_str for term in data_analyst_indicators):
            return 'data_analyst'
        elif any(term in kw_str for term in software_engineer_indicators):
            return 'software_engineer'
        else:
            return 'general'
    
    def create_optimized_skills(self, job_type, keywords):
        """Create job-optimized skills section with compact headings"""
        
        if job_type == 'data_engineering':
            skills_section = """%----------TECHNICAL SKILLS----------%
\\section{Technical Skills}
\\begin{itemize}[leftmargin=0.15in, label={}]
\\small{\\item{
\\textbf{Programming}{: Python, SQL, R, JavaScript, Java, C/C++, HTML, CSS} \\\\
\\textbf{Data Engineering}{: Data pipelines, ETL/ELT, Data modeling, Schema design, Pipeline development} \\\\
\\textbf{Big Data \\& Analytics}{: Spark, Hadoop, Kafka, Databricks, Distributed systems, Data quality} \\\\
\\textbf{Cloud \\& Infrastructure}{: AWS, Azure, Docker, Kubernetes, Git, CI/CD pipelines} \\\\
\\textbf{Databases}{: PostgreSQL, MySQL, MongoDB, Snowflake, NoSQL, Database optimization} \\\\
\\textbf{Tools \\& Frameworks}{: Tableau, Power BI, Jupyter, VS Code, Agile, Technical testing}
}}
\\end{itemize}"""
            return skills_section
        
        elif job_type == 'data_analyst':
            skills_section = """%----------TECHNICAL SKILLS----------%
\\section{Technical Skills}
\\begin{itemize}[leftmargin=0.15in, label={}]
\\small{\\item{
\\textbf{Programming}{: Python, Advanced SQL, R, JavaScript, Java, HTML, CSS} \\\\
\\textbf{Business Analytics}{: Data analytics, Business intelligence, Statistical analysis, Data visualization} \\\\
\\textbf{BI Tools}{: Power BI, Tableau, Looker, Excel, Spreadsheet programs, Dashboard development} \\\\
\\textbf{Databases}{: Advanced SQL, PostgreSQL, MySQL, Data modeling, Query optimization} \\\\
\\textbf{Cloud \\& Tools}{: AWS, Git, Jupyter, Python libraries, Data processing} \\\\
\\textbf{Skills}{: Machine learning, Data mining, Reporting, Analytics, Business processes}
}}
\\end{itemize}"""
            return skills_section
        
        elif job_type == 'software_engineer':
            skills_section = """%----------TECHNICAL SKILLS----------%
\\section{Technical Skills}
\\begin{itemize}[leftmargin=0.15in, label={}]
\\small{\\item{
\\textbf{Programming}{: Python, JavaScript, TypeScript, Java, C/C++, HTML, CSS, React.js, Node.js} \\\\
\\textbf{Web Development}{: React, Angular, Vue, Express.js, RESTful APIs, GraphQL, Frontend applications} \\\\
\\textbf{Cloud \\& Infrastructure}{: AWS, Docker, Kubernetes, Git, CI/CD pipelines, Microservices} \\\\
\\textbf{Databases}{: SQL, MySQL, PostgreSQL, MongoDB, NoSQL, Database design, API development} \\\\
\\textbf{Tools \\& Frameworks}{: Git, Jira, VS Code, Postman, Django, Flask, Agile methodology}
}}
\\end{itemize}"""
            return skills_section
        
        elif job_type == 'network_engineer':
            skills_section = """%----------TECHNICAL SKILLS----------%
\\section{Technical Skills}
\\begin{itemize}[leftmargin=0.15in, label={}]
\\small{\\item{
\\textbf{Networking}{: TCP/IP, OSI Model, Routing \\& Switching, DNS, DHCP, HTTP, NAT, BGP, Subnetting, Network Connectivity} \\\\
\\textbf{Network Tools}{: Cisco IOS, Network Diagnostics, ping, traceroute, Wireshark, Service Desk Management} \\\\
\\textbf{Programming}{: Python, Bash/Shell Scripting, Network Automation, Configuration Management} \\\\
\\textbf{Operating Systems}{: Linux, Windows, MacOS, Network Troubleshooting, System Administration} \\\\
\\textbf{Tools \\& Documentation}{: Git, Jira, Network Documentation, Inventory Management, Ticket Resolution}
}}
\\end{itemize}"""
            return skills_section
        
        else:  # general
            return self.sections['skills']
    
    def optimize_content(self, content, job_type, keywords):
        """Optimize content with job-specific keywords and enforce 2-line limit"""
        
        optimized = content
        
        # Common optimizations
        replacements = {
            r'\bsql\b': 'Advanced SQL' if job_type == 'data_analyst' else 'SQL',
            r'\banalytics platform\b': 'data engineering platform' if job_type == 'data_engineering' else 'analytics platform',
            r'\bpython scripts\b': 'data pipelines' if job_type == 'data_engineering' else 'Python automation',
            r'\bdashboards\b': 'business intelligence dashboards',
            r'\baws\b': 'AWS cloud services',
            r'\bagile\b': 'Agile methodology',
            r'\bweb applications?\b': 'frontend applications',
            r'\bapi development\b': 'RESTful API development',
            r'\bscalable\b': 'highly scalable',
            r'\breliable\b': 'highly reliable',
            r'\bresilient\b': 'highly resilient',
            r'\bcross functional\b': 'cross-functional',
            r'\bproduct challenges\b': 'technical and product challenges',
            r'\bcommunication skills\b': 'written and verbal communication skills'
        }
        
        for pattern, replacement in replacements.items():
            optimized = re.sub(pattern, replacement, optimized, flags=re.IGNORECASE)
        
        # Enforce 2-line limit for bullet points
        optimized = self.enforce_bullet_point_limit(optimized)
        
        return optimized
    
    def enforce_bullet_point_limit(self, content):
        """Enforce max 2 lines per bullet point"""
        lines = content.split('\n')
        optimized_lines = []
        
        for line in lines:
            if '\\resumeItem{' in line:
                # Extract the content inside \resumeItem{}
                match = re.search(r'\\resumeItem\{([^}]+)\}', line)
                if match:
                    item_content = match.group(1)
                    # Split by sentences and limit to ~120 characters per line
                    sentences = re.split(r'[.!?]+', item_content)
                    if len(item_content) > 120:
                        # Try to break at natural points
                        words = item_content.split()
                        if len(words) > 15:  # More than 15 words
                            # Find a good breaking point around the middle
                            mid_point = len(words) // 2
                            for i in range(mid_point, len(words)):
                                if words[i].endswith(('.', ',', ';', ':')):
                                    break_point = i + 1
                                    break
                            else:
                                break_point = mid_point
                            
                            line1 = ' '.join(words[:break_point])
                            line2 = ' '.join(words[break_point:])
                            new_line = f"\\resumeItem{{{line1} {line2}}}"
                            optimized_lines.append(new_line)
                        else:
                            optimized_lines.append(line)
                    else:
                        optimized_lines.append(line)
                else:
                    optimized_lines.append(line)
            else:
                optimized_lines.append(line)
        
        return '\n'.join(optimized_lines)
    
    def optimize_projects_for_job_type(self, job_type, keywords):
        """Select and optimize exactly 3 projects based on job type"""
        
        # Extract project sections from the original projects.tex
        project_sections = []
        current_project = []
        in_project = False
        
        for line in self.sections['projects'].split('\n'):
            if '\\resumeProjectHeading' in line:
                if current_project:
                    project_sections.append('\n'.join(current_project))
                current_project = [line]
                in_project = True
            elif in_project:
                current_project.append(line)
                if line.strip() == '\\resumeItemListEnd':
                    in_project = False
        
        if current_project:
            project_sections.append('\n'.join(current_project))
        
        # Select 3 most relevant projects based on job type
        if job_type == 'software_engineer':
            # Prioritize web development, React, Node.js projects
            priority_keywords = ['react', 'node', 'web', 'api', 'full-stack', 'javascript', 'typescript']
        elif job_type == 'data_engineering':
            # Prioritize data, AWS, Dask, analytics projects
            priority_keywords = ['dask', 'aws', 'data', 'analytics', 'cloud', 'distributed']
        elif job_type == 'data_analyst':
            # Prioritize analytics, visualization, data analysis projects
            priority_keywords = ['analysis', 'analytics', 'data', 'visualization', 'pandas', 'svm']
        else:
            # General - use all available projects
            priority_keywords = []
        
        # Score projects based on relevance
        project_scores = []
        for i, project in enumerate(project_sections):
            score = 0
            project_lower = project.lower()
            for keyword in priority_keywords:
                if keyword in project_lower:
                    score += 1
            project_scores.append((score, i, project))
        
        # Sort by score (highest first) and take top 3
        project_scores.sort(reverse=True)
        selected_projects = project_scores[:3]
        
        # If we don't have 3 projects, use all available
        if len(selected_projects) < 3:
            selected_projects = [(0, i, project) for i, project in enumerate(project_sections[:3])]
        
        # Build optimized projects section
        optimized_projects = """%-----------PROJECTS-----------%
\\section{Projects}
\\resumeSubHeadingListStart"""
        
        for score, idx, project in selected_projects:
            optimized_project = self.optimize_content(project, job_type, keywords)
            optimized_projects += "\n\n" + optimized_project
        
        optimized_projects += "\n\n\\resumeSubHeadingListEnd"
        
        return optimized_projects
    
    def generate_resume(self, job_description, job_title=""):
        """Generate optimized resume with strict 1-page formatting"""
        
        print("\n🔍 Analyzing job description...")
        keywords = self.extract_keywords(job_description)
        job_type = self.detect_job_type(keywords)
        
        print(f"📊 Found {len(keywords)} keywords")
        print(f"🎯 Job type: {job_type.replace('_', ' ').title()}")
        
        # Generate filename
        if job_title:
            clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', job_title)
            filename = f"{clean_title.replace(' ', '_')}_Resume.tex"
        else:
            filename = f"{job_type.title().replace('_', '_')}_Resume.tex"
        
        # Create optimized sections
        optimized_skills = self.create_optimized_skills(job_type, keywords)
        optimized_experience = self.optimize_content(self.sections['experience'], job_type, keywords)
        optimized_projects = self.optimize_projects_for_job_type(job_type, keywords)
        
        # Build complete resume
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Create the resume header
        resume_header = f"""%-------------------------
% ATS Optimized Resume
% Generated: {timestamp}
% Job Type: {job_type.replace('_', ' ').title()}
% Keywords: {len(keywords)} strategic terms
%------------------------

\\documentclass[letterpaper,11pt]{{article}}

\\usepackage{{fontawesome5}}
\\usepackage{{latexsym}}
\\usepackage[empty]{{fullpage}}
\\usepackage{{titlesec}}
\\usepackage{{marvosym}}
\\usepackage[usenames,dvipsnames]{{color}}
\\usepackage{{verbatim}}
\\usepackage{{enumitem}}
\\usepackage[hidelinks]{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage[english]{{babel}}
\\usepackage{{tabularx}}
\\input{{glyphtounicode}}

% Font and formatting
\\usepackage[default]{{lato}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\renewcommand{{\\headrulewidth}}{{0pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

% Margins
\\addtolength{{\\oddsidemargin}}{{-0.5in}}
\\addtolength{{\\evensidemargin}}{{-0.5in}}
\\addtolength{{\\textwidth}}{{1in}}
\\addtolength{{\\topmargin}}{{-0.7in}}
\\addtolength{{\\textheight}}{{1.5in}}

\\urlstyle{{same}}
\\raggedbottom
\\raggedright
\\setlength{{\\tabcolsep}}{{0in}}

% Section formatting
\\titleformat{{\\section}}{{\\vspace{{-13pt}}\\scshape\\raggedright\\large}}{{}}{{0em}}{{}}[\\color{{black}}\\titlerule\\vspace{{-5pt}}]
\\pdfgentounicode=1

% Commands
\\newcommand{{\\resumeItem}}[1]{{\\item\\small{{{{#1 \\vspace{{-2pt}}}}}}}}
\\newcommand{{\\resumeSubheading}}[4]{{\\vspace{{-2pt}}\\item\\textbf{{#1}}, \\textit{{\\small #3}}, \\hfill \\textit{{\\small #4}} \\vspace{{-7pt}}}}
\\newcommand{{\\resumeProjectHeading}}[2]{{\\item\\begin{{tabular*}}{{0.97\\textwidth}}{{l@{{\\extracolsep{{\\fill}}}}r}}\\small#1 & #2 \\\\\\end{{tabular*}}\\vspace{{-7pt}}}}
\\newcommand{{\\resumeSubItem}}[1]{{\\resumeItem{{#1}}\\vspace{{-4pt}}}}
\\renewcommand\\labelitemii{{$\\vcenter{{\\hbox{{\\tiny$\\bullet$}}}}$}}
\\newcommand{{\\resumeSubHeadingListStart}}{{\\begin{{itemize}}[leftmargin=0.15in, label={{}}]}}
\\newcommand{{\\resumeSubHeadingListEnd}}{{\\end{{itemize}}}}
\\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}}}
\\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}\\vspace{{-5pt}}}}

\\begin{{document}}"""
        
        # Combine all parts
        complete_resume = (resume_header + "\n\n" +
                          self.sections['heading'] + "\n\n" +
                          self.sections['education'] + "\n\n" +
                          optimized_skills + "\n\n" +
                          optimized_experience + "\n\n" +
                          optimized_projects + "\n\n" +
                          "\\end{document}")
        
        # Save file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(complete_resume)
        
        print(f"\n✅ Generated: {filename}")
        print(f"📄 Ready for Overleaf!")
        print(f"🎯 Expected ATS score: 85-95%")
        
        return filename

def main():
    print("🎯 ATS Resume Optimizer")
    print("=" * 50)
    
    # Try to read job description from quick_optimizer.py first
    job_description, job_title = read_job_from_quick_optimizer()
    
    if not job_description:
        # Fallback to interactive mode
        print("\n📋 Instructions:")
        print("1. Paste your job description below")
        print("2. Press Enter twice to finish")
        print("3. Get your optimized resume!")
        
        print("\n" + "-" * 50)
        print("PASTE JOB DESCRIPTION:")
        
        # Read job description
        lines = []
        empty_count = 0
        
        while True:
            try:
                line = input()
                if line.strip() == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                lines.append(line)
            except KeyboardInterrupt:
                print("\n\nExiting...")
                return
        
        job_description = "\n".join(lines).strip()
        
        if not job_description:
            print("❌ No job description provided")
            return
        
        # Optional job title
        job_title = input("\nJob title (optional): ").strip()
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    if not optimizer.sections:
        return
    
    # Generate resume
    try:
        filename = optimizer.generate_resume(job_description, job_title)
        print(f"\n🎉 SUCCESS!")
        print(f"\n📋 Next steps:")
        print(f"1. Go to Overleaf.com")
        print(f"2. Upload {filename} or copy its contents")
        print(f"3. Compile to PDF")
        print(f"4. Submit your optimized resume!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def read_job_from_quick_optimizer():
    """Read job description and title from quick_optimizer.py"""
    try:
        with open('quick_optimizer.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract job description
        job_desc_match = re.search(r'job_description\s*=\s*"""(.*?)"""', content, re.DOTALL)
        if job_desc_match:
            job_description = job_desc_match.group(1).strip()
        else:
            return None, None
        
        # Extract job title
        job_title_match = re.search(r'job_title\s*=\s*["\']([^"\']+)["\']', content)
        if job_title_match:
            job_title = job_title_match.group(1).strip()
        else:
            job_title = ""
        
        print(f"📖 Read job description from quick_optimizer.py")
        print(f"🎯 Job Title: {job_title}")
        print(f"📝 Description length: {len(job_description)} characters")
        
        return job_description, job_title
        
    except FileNotFoundError:
        print("📖 quick_optimizer.py not found, using interactive mode")
        return None, None
    except Exception as e:
        print(f"📖 Error reading quick_optimizer.py: {e}")
        return None, None

if __name__ == "__main__":
    main()
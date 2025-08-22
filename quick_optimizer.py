#!/usr/bin/env python3
"""
Quick Resume Optimizer
Easy-to-use interface for generating optimized resumes

Author: Subhadra Mishra
"""

import sys
import os
sys.path.append('.')

from resume_optimizer import ResumeOptimizer

def quick_optimize(job_description, job_title):
    """Quick optimization for any job description"""
    
    print(f"🎯 Optimizing for: {job_title}")
    print("=" * 50)
    
    optimizer = ResumeOptimizer()
    if not optimizer.sections:
        print("❌ Failed to load resume sections")
        return None
    
    try:
        filename = optimizer.generate_resume(job_description, job_title)
        print(f"\n✅ SUCCESS! Generated: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    # Replace this with your job description
    job_description = """Your Role
As a Software Engineer you will be responsible for building Zip's core products and architecture. You will ship features that will be immediately used by our customers, and will work with a tight-knit team that values open communication and cross-functional collaboration. We move quickly to solve a wide range of complex technical and product challenges. While we are an experienced team that can provide constant guidance and mentorship, we value engineers who can scope and solve difficult technical challenges.

You Will
Design and build highly reliable and resilient products and features

Work closely with cross functional product and customer-facing teams to understand requirements and ship thoughtful solutions

Write high-quality, extensible, and maintainable code

Design and build scalable frontend applications and components

Design and build APIs to drive existing and new features for a web-based application

Qualifications
Pursuing a BS or MS in Computer Science or related technical field involving coding (e.g. physics or math), with a graduation date between December 2025 - June 2026

Experience with web applications and API development. At Zip, our stack includes Python, Javascript/TypeScript, React, and GraphQL

Ability and interest to quickly learn new frameworks, architecture patterns, and programming languages as needed

Fantastic written and verbal communication skills

Prior internships in high-growth startup environment"""

    job_title = "Software Engineer"
    
    print("🚀 Quick Resume Optimizer")
    print("=" * 50)
    print("📝 Instructions:")
    print("1. Replace the job_description variable with your job description")
    print("2. Update the job_title variable")
    print("3. Run: python quick_optimizer.py")
    print("4. Get your optimized .tex file!")
    print("=" * 50)
    
    result = quick_optimize(job_description, job_title)
    
    if result:
        print(f"\n📄 Your optimized resume: {result}")
        print("🌐 Upload to Overleaf.com to compile to PDF")
    else:
        print("\n❌ Optimization failed")

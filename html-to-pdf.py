from weasyprint import HTML, CSS
import os
import re

# Read the content from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content_html = f.read()
    
    # Extract the CSS from the original document
    css_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL)
    css_match = css_pattern.search(content_html)
    original_css = css_match.group(1) if css_match else ""
    
    # Extract just the body content from index.html
    body_start = content_html.find('<body')
    body_start = content_html.find('>', body_start) + 1
    body_end = content_html.rfind('</body>')
    
    if body_start > 0 and body_end > 0:
        body_content = content_html[body_start:body_end].strip()
    else:
        # If we can't find body tags, use the whole content
        body_content = content_html

# Create custom CSS with page numbering and preserve original styles
custom_css = '''
    /* Basic page setup */
    @page {
        size: a4;
        margin: 1cm;
        padding-left: 20px;
        padding-right: 20px;
        
        /* Add page numbering in the footer */
        @bottom-center {
            content: "Page " counter(page);
            font-family: Arial, sans-serif;
            font-size: 10pt;
        }
    }
    
    /* First page (cover) has no page number */
    @page :first {
        @bottom-center {
            content: none;
        }
    }
    
    /* Cover page styling */
    .cover-page {
        page-break-after: always;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    
    .cover-title {
        font-family: Arial, sans-serif;
        font-size: 28pt;
        font-weight: bold;
        margin-bottom: 40px;
        color: #2c3e50;
    }
    
    .cover-subtitle {
        font-family: Arial, sans-serif;
        font-size: 16pt;
        margin-bottom: 60px;
        color: #34495e;
    }
    
    .cover-authors {
        font-family: Arial, sans-serif;
        font-size: 14pt;
        margin-bottom: 20px;
    }
    
    .cover-date {
        font-family: Arial, sans-serif;
        font-size: 12pt;
        margin-top: 40px;
        color: #7f8c8d;
    }
    
    .cover-image {
        max-width: 60%;
        margin: 30px 0;
    }
    
    /* Table of contents styling */
    .toc {
        page-break-after: always;
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    
    .toc-title {
        font-family: Arial, sans-serif;
        font-size: 18pt;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .toc-entry {
        font-family: Arial, sans-serif;
        margin-bottom: 8px;
    }
    
    .toc-section {
        font-weight: bold;
    }
    
    .toc-subsection {
        margin-left: 20px;
    }
    
    /* Ensure page breaks don't occur in the middle of important sections */
    h1, h2, h3 {
        page-break-after: avoid;
    }
    
    table, figure {
        page-break-inside: avoid;
    }
    
    /* Ensure references start on a new page */
    .references-section {
        page-break-before: always;
    }
    
    /* Original CSS from index.html */
''' + original_css

# Create a complete HTML document with cover, TOC, and content
complete_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Stroke Prediction Analysis</title>
    <style>
''' + custom_css + '''
    </style>
</head>
<body>
    <!-- Cover Page -->
    <div class="cover-page">
        <div class="cover-title">Stroke Prediction Using Machine Learning</div>
        <div class="cover-subtitle">A Comparative Analysis of Logistic Regression and XGBoost Models</div>
        <img src="visualize-chart-img/age-distribution-by-stroke.png" class="cover-image" alt="Stroke Analysis">
        <div class="cover-authors">By: Tung Lam & Hoan</div>
        <div class="cover-date">May 2023</div>
    </div>
    
    <!-- Table of Contents -->
    <div class="toc">
        <div class="toc-title">Table of Contents</div>
        <div class="toc-entry toc-section">1. Introduction</div>
        <div class="toc-entry toc-section">2. Dataset Overview and Preprocessing</div>
        <div class="toc-entry toc-section">3. Descriptive Statistics</div>
        <div class="toc-entry toc-section">4. Model Comparison: Logistic Regression vs. XGBoost</div>
        <div class="toc-entry toc-subsection">4.1 Logistic Regression for Stroke Prediction</div>
        <div class="toc-entry toc-subsection">4.2 XGBoost for Stroke Prediction</div>
        <div class="toc-entry toc-subsection">4.3 Model Performance Analysis</div>
        <div class="toc-entry toc-subsection">4.4 What This Means for Patient Care</div>
        <div class="toc-entry toc-section">5. Recommendations</div>
        <div class="toc-entry toc-section">6. References</div>
    </div>
    
    <!-- Main Content -->
    <div class="container">
''' + body_content + '''
    </div>
</body>
</html>
'''

# Write the complete HTML to a temporary file
with open('complete_document.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

# Create the PDF with proper page numbering
try:
    HTML('complete_document.html').write_pdf('stroke_prediction_analysis.pdf')
    
    # Clean up temporary file
    os.remove('complete_document.html')
    
    print("PDF successfully created with cover page, table of contents, and page numbers!")
    
except Exception as e:
    print(f"Error creating PDF: {e}")
    print("Falling back to basic PDF creation...")
    
    # Fallback to just converting the index.html file
    HTML('index.html').write_pdf('stroke_prediction_analysis.pdf')

from weasyprint import HTML, CSS

# Create custom CSS to handle table sizing
css = CSS(string='''
    @page {
        size: letter landscape;
        margin: 1cm;
        padding: 30px
    }
    table {
        width: 100%;
        max-width: 100%;
        font-size: 10px;
        table-layout: fixed;
        page-break-inside: auto;
    }
    th, td {
        word-wrap: break-word;
        overflow-wrap: break-word;
        padding: 4px;
    }
    .chart-container img {
        max-width: 100%;
        height: auto;
    }
''')

# Apply the CSS when generating the PDF
HTML('index.html').write_pdf('stroke_prediction_analysis.pdf', stylesheets=[css])

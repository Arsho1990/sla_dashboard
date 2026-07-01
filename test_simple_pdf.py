#!/usr/bin/env python
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime

try:
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=landscape(A4))
    elements = []
    
    # Add title
    styles = getSampleStyleSheet()
    title = Paragraph(f"<b>Test Report</b><br/><font size=10>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</font>", 
                    styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 0.2*inch))
    
    # Create simple table
    table_data = [['Header1', 'Header2'], ['Data1', 'Data2']]
    table = Table(table_data)
    
    # Style table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (75/255, 0/255, 130/255)),  # Purple
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, (245/255, 245/255, 245/255)]),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    elements.append(table)
    doc.build(elements)
    output.seek(0)
    
    with open('test_simple.pdf', 'wb') as f:
        f.write(output.getvalue())
    
    print(f"✓ PDF created successfully: test_simple.pdf ({len(output.getvalue())} bytes)")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()

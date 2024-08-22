from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, Image

def create_cv(file_path):
    # Skapa ett dokument
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    # Definiera stilar
    title_style = ParagraphStyle(
        name='Title',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1a1a1a"),
        spaceAfter=20
    )

    header_style = ParagraphStyle(
        name='Header',
        fontSize=15,
        leading=22,
        textColor=colors.HexColor("#333333"),
        spaceAfter=10
    )

    normal_style = ParagraphStyle(
        name='Normal',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#4d4d4d"),
        spaceAfter=5
    )

    job_title_style = ParagraphStyle(
        name='JobTitle',
        fontSize=12,
        leading=18,
        textColor=colors.HexColor("#1a1a1a"),
        spaceAfter=5
    )

    # Innehåll för CV
    content = []

 # Lägg till en tabell för titel och bild
    profile_picture = Image("im2.png", 2*inch, 2*inch)
    title = Paragraph("Curriculum Vitae", title_style)

    title_and_image_table = Table(
        [[title, profile_picture]],
        colWidths=[None, 2*inch]
    )
    title_and_image_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]))
    content.append(title_and_image_table)
    content.append(Spacer(1, 20))

    # Personlig information
    personal_info = Table(
        [[
            Paragraph("<b>Name:</b> Add information", normal_style),
            Paragraph("<b>Adress:</b> Add information", normal_style)
        ], [
            Paragraph("<b>Phone:</b> Add information", normal_style),
            Paragraph("<b>Email:</b> Add information", normal_style)
        ]],
        colWidths=[200, 200]
    )
    personal_info.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LINEABOVE', (0, 0), (1, 0), 1, colors.HexColor("#cccccc")),
        ('LINEBELOW', (0, 1), (1, 1), 1, colors.HexColor("#cccccc")),
    ]))
    content.append(personal_info)
    content.append(Spacer(1, 12))

    # Utbildning
    education = Paragraph("<b>Education</b>", header_style)
    content.append(education)

    education_details = Paragraph(
        "Add information<br/>"
        "Add information<br/>",
        job_title_style
    )
    content.append(education_details)
    content.append(Spacer(1, 12))

    # Arbetslivserfarenhet
    experience = Paragraph("<b>Professional experience</b>", header_style)
    content.append(experience)

    job1 = Paragraph("2023 - Current: Add information", job_title_style)
    job1_details = Paragraph(
       Add information
    )
    content.append(job1)
    content.append(job1_details)
    content.append(Spacer(1, 10))

    job2 = Paragraph("2021 - 2023: Add information", job_title_style)
    job2_details = Paragraph(
        Add information
        normal_style
    )
    content.append(job2)
    content.append(job2_details)
    content.append(Spacer(1, 10))
    
    job3 = Paragraph("2019 - 2021: Add information", job_title_style)
    job3_details = Paragraph(
        Add information
        normal_style
    )
    content.append(job3)
    content.append(job3_details)
    content.append(Spacer(1, 10))
    
    job4 = Paragraph("2018 - 2019: Add information", job_title_style)
    job4_details = Paragraph(
        Add information
        normal_style
    )
    content.append(job4)
    content.append(job4_details)
    content.append(Spacer(1, 10))
    
    job5 = Paragraph("2017 - 2019: Add information", job_title_style)
    job5_details = Paragraph(
        Add information
        normal_style
    )
    content.append(job5)
    content.append(job5_details)
    content.append(Spacer(1, 10))
    
    # Färdigheter
    skills = Paragraph("<b>Technical skills</b>", header_style)
    content.append(skills)

    skills_details = Paragraph(
        "<b>Superb skills in</b>: Python, R, JavaScript, SQL<br/>"
        "<b>Proficient in</b>: STATA, SPSS, HTML, XML, CSS<br/>"
        "<b>Familiar with</b>: C++, C#, Java, Matlab, Eviews<br/>"
        "<b>Tools</b>: Git, Docker/Kubernetes, Azure DevOps, Microsoft Office<br/>",
        job_title_style
    )
    content.append(skills_details)
    content.append(Spacer(1, 12))

    # Bygg dokumentet
    doc.build(content)

# Skapa CV och spara det som en PDF-fil
create_cv("Add information.pdf")

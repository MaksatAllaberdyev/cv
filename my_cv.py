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
            Paragraph("<b>Name:</b> Maksat Allaberdyev", normal_style),
            Paragraph("<b>Adress:</b> Anna Whitlocks Gata 13, 11366 Stockholm", normal_style)
        ], [
            Paragraph("<b>Phone:</b> 076-826 97 94", normal_style),
            Paragraph("<b>Email:</b> maksatallaberdyev91@gmail.com", normal_style)
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
        "2017 - 2019: Master of Science in Economics<br/>"
        "2014 - 2017: Bachelor of Science in Economics<br/>",
        job_title_style
    )
    content.append(education_details)
    content.append(Spacer(1, 12))

    # Arbetslivserfarenhet
    experience = Paragraph("<b>Professional experience</b>", header_style)
    content.append(experience)

    riksbank = Paragraph("2023 - Current: Economist/Systems manager, Sveriges Riksbank", job_title_style)
    riksbank_details = Paragraph(
        "Responsible for collecting and publishing the reference rate Swestr and International Banking Statistics for BIS. "
        "I have automated and streamlined data and models in monetary policy forecasting.",
        normal_style
    )
    content.append(riksbank)
    content.append(riksbank_details)
    content.append(Spacer(1, 10))

    scb = Paragraph("2021 - 2023: Economist, Statistics Sweden", job_title_style)
    scb_details = Paragraph(
        "Collected data from MFIs to produce Financial Market Statistics. "
        "Product owner and project manager implementing new ECB regulations.",
        normal_style
    )
    content.append(scb)
    content.append(scb_details)
    content.append(Spacer(1, 10))
    
    ski = Paragraph("2019 - 2021: Analyst, Svenskt Kvalitetsindex/EPSI Rating", job_title_style)
    ski_details = Paragraph(
        "Worked as an analyst, project manager and consultant in "
        "branches such as banking, insurance and public sector.",
        normal_style
    )
    content.append(ski)
    content.append(ski_details)
    content.append(Spacer(1, 10))
    
    umu = Paragraph("2018 - 2019: Teaching assistant, Umeå Universitet", job_title_style)
    umu_details = Paragraph(
        "Teaching assistant and lecturer in Macroeconomics at the beginner level.",
        normal_style
    )
    content.append(umu)
    content.append(umu_details)
    content.append(Spacer(1, 10))
    
    lf = Paragraph("2017 - 2019: Bank clerk, Länsförsäkringar Västerbotten", job_title_style)
    lf_details = Paragraph(
        "Bank clerk with experience in Backoffice and AML.",
        normal_style
    )
    content.append(lf)
    content.append(lf_details)
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

# Skapa ett stylat CV med bild och spara det som en PDF-fil
create_cv("CV_Maksat Allaberdyev.pdf")

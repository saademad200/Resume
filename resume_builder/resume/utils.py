from .resume_template import template


from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, cm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Spacer, Table, TableStyle, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from django.conf import settings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import reportlab.lib.pagesizes as pagesizes
from datetime import datetime
from reportlab.lib import colors

styles = getSampleStyleSheet()
styleN = styles["Normal"]
style = getSampleStyleSheet()
styleH = styles["Heading1"]


def getPDF(resume):
    doc = SimpleDocTemplate(
        f"media/resume/resume_template{datetime.now().strftime('%H%M%S')}.pdf",
        leftMargin=template["left_margin"] * cm,
        rightMargin=template["right_margin"] * cm,
        bottomMargin=template["bottom_margin"] * cm,
        topMargin=template["top_margin"] * cm,
        pagesize=pagesizes.A4,
        # showBoundary=1,
    )

    elements = []

    width = doc.width
    height = doc.height - 12 - 10

    gutter = template["column_gutter_size"] * cm
    col = (width - gutter * 10) / 12
    colWithGutter = col + gutter
    gutter = template["row_gutter_size"] * cm
    row = (height - gutter * 14) / 16
    rowWithGutter = row + gutter
    image = Image(resume["photo"], colWithGutter * 8 + 10, row + rowWithGutter * 8)
    hr = HRFlowable(
        width="100%",
        thickness=5,
        lineCap="square",
        color="#123",
        spaceBefore=-2,
        spaceAfter=0,
        hAlign="LEFT",
        vAlign="BOTTOM",
        dash=None,
    )
    pdfmetrics.registerFont(TTFont("RobotoBold", settings.MEDIA_ROOT+"/fonts/"+"Roboto-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoItalic", settings.MEDIA_ROOT+"/fonts/"+"Roboto-Italic.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoLight", settings.MEDIA_ROOT+"/fonts/"+"Roboto-Light.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoLightItalic", settings.MEDIA_ROOT+"/fonts/"+"Roboto-LightItalic.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoMedium",settings.MEDIA_ROOT+"/fonts/"+ "Roboto-Medium.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoMediumItalic", settings.MEDIA_ROOT+"/fonts/"+"Roboto-MediumItalic.ttf"))
    pdfmetrics.registerFont(TTFont("RobotoRegular",settings.MEDIA_ROOT+"/fonts/"+ "Roboto-Regular.ttf"))
    styles = getSampleStyleSheet()
    titleStyle = ParagraphStyle(
        "title",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoMedium",
        fontSize=template["block_title_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=0,
        spaceBefore=0,
        textColor=template["block_title_color"],
        leading=template["block_title_line_height"],
        textTransform=template["block_title_case"],
        wordWrap=None,
    )
    subtitleStyle = ParagraphStyle(
        "subtitle",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoMedium",
        fontSize=template["block_subtitle_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=8,
        spaceBefore=1,
        textColor=template["block_subtitle_color"],
        leading=template["block_title_line_height"],
        textTransform="CAPITALIZE",
        wordWrap=None,
    )
    descStyle = ParagraphStyle(
        "desc",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoRegular",
        fontSize=template["block_description_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=0,
        spaceBefore=0,
        textColor=template["block_description_color"],
        leading=template["block_description_line_height"],
        wordWrap=None,
    )
    headingStyle = ParagraphStyle(
        "title",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoMedium",
        fontSize=template["block_title_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=8,
        spaceBefore=0,
        textColor=template["block_title_color"],
        leading=template["block_title_line_height"],
        textTransform=template["block_title_case"],
        wordWrap=None,
    )
    infoStyle = ParagraphStyle(
        "desc",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoRegular",
        fontSize=template["block_description_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=0,
        spaceBefore=0,
        textColor=template["block_description_color"],
        leading=template["block_description_line_height"],
        wordWrap=None,
        textTransform="CAPITALIZE",
    )
    paragraphsIntro = []
    titlePara = Paragraph(resume["title"], style=titleStyle)
    paragraphsIntro.append(titlePara)
    subtitlePara = Paragraph(resume["subtitle"], style=subtitleStyle)
    paragraphsIntro.append(subtitlePara)
    descriptionPara = Paragraph(resume["description"], style=descStyle)
    paragraphsIntro.append(descriptionPara)
    paragraphsIntro.append(Spacer(10, 10))
    paragraphsContact = []
    titlePara = Paragraph("Contact", style=headingStyle)
    paragraphsContact.append(titlePara)
    for i in resume["contact"]:
        key = list(i.keys())[0]
        value = i[key]
        content = f"{key}: {value}"
        paragraphsContact.append(Paragraph(content, style=infoStyle))
    paragraphsPersonal = []
    titlePara = Paragraph("Personal Info", style=headingStyle)
    paragraphsPersonal.append(titlePara)
    for i in resume["personal_info"]:
        key = list(i.keys())[0]
        value = i[key]
        if type(value) is list:
            value = ",".join(value)
        content = f"{key}: {value}"
        paragraphsPersonal.append(Paragraph(content, style=infoStyle))
    data = [
        ["", "", [image, hr], "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", paragraphsIntro, "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        [
            "",
            "",
            paragraphsContact,
            "",
            "",
            "",
            "",
            paragraphsPersonal,
            "",
            "",
            "",
            "",
            "",
        ],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", ""],
    ]
    # data = [[logo, '', '', '', '', '', '', '', '', '', '', '']]
    table = Table(
        data,
        colWidths=[
            col,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            10,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            colWithGutter,
            col,
        ],
        rowHeights=[
            row,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            rowWithGutter,
            10,
            rowWithGutter,
            rowWithGutter,
            row,
        ],
        style=[
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("SPAN", (2, 0), (10, 8)),
            ("SPAN", (2, 9), (10, 12)),
            ("BACKGROUND", (2, 9), (10, 12), template["block_background_color"]),
            ("SPAN", (2, 14), (5, 16)),
            ("BACKGROUND", (2, 14), (5, 16), template["block_background_color"]),
            ("SPAN", (7, 14), (10, 16)),
            ("BACKGROUND", (7, 14), (10, 16), template["block_background_color"]),
            # ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ],
    )

    elements.append(table)

    categoryStyle = ParagraphStyle(
        "category",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoMedium",
        fontSize=template["cv_category_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=15,
        spaceBefore=2,
        textColor=template["cv_category_color"],
        leading=template["cv_category_line_height"],
        textTransform=template["cv_category_case"],
        wordWrap=None,
    )

    cvtitleStyle = ParagraphStyle(
        "CV title",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLight",
        fontSize=template["cv_title_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=3,
        spaceBefore=8,
        textColor=template["cv_title_color"],
        backColor=template["cv_highlight_color"],
        leading=template["cv_title_line_height"],
        textTransform=template["cv_title_case"],
        wordWrap=None,
    )

    cvtitleHighlightStyle = ParagraphStyle(
        "CV title highlight",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLight",
        fontSize=template["cv_title_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=3,
        spaceBefore=8,
        textColor=colors.white,
        backColor=template["highlight_color"],
        leading=template["cv_title_line_height"],
        textTransform=template["cv_title_case"],
        wordWrap=None,
    )

    cvsubtitleStyle = ParagraphStyle(
        "CV subtitle",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLightItalic",
        fontSize=template["cv_subtitle_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=5,
        spaceBefore=0,
        textColor=template["cv_subtitle_color"],
        leading=template["cv_title_line_height"],
        textTransform="Capitalize",
        wordWrap=None,
    )

    cvdescStyle = ParagraphStyle(
        "CV description",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoRegular",
        fontSize=template["cv_description_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=20,
        spaceBefore=0,
        textColor=template["cv_description_color"],
        textTransform="Capitalize",
        wordWrap=None,
    )

    dateStyleHighlight = ParagraphStyle(
        "CV date heighlight",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoLight",
        fontSize=template["cv_date_size"],
        leftIndent=15,
        rightIndent=0,
        spaceAfter=5,
        spaceBefore=0,
        textColor=template["highlight_color"],
        textTransform="Capitalize",
        wordWrap=None,
    )

    dateStyle = ParagraphStyle(
        "CV date heighlight",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoLight",
        fontSize=template["cv_date_size"],
        leftIndent=15,
        rightIndent=0,
        spaceAfter=5,
        spaceBefore=0,
        textColor=template["cv_date_color"],
        textTransform="Capitalize",
        wordWrap=None,
    )

    hr = HRFlowable(
        width="100%",
        thickness=5,
        lineCap="square",
        color=template["divider_color"],
        spaceBefore=0,
        spaceAfter=10,
        hAlign="LEFT",
        vAlign="BOTTOM",
        dash=None,
    )

    titlePara = Paragraph("RED Studio", style=cvtitleStyle)
    subtitlePara = Paragraph("Senior web designer", style=cvsubtitleStyle)
    descriptionPara = Paragraph(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur perdiet, dolor eget porta scelerisque, ex lectus ultricies lorem, a porttitor sapien ipsum at augue",
        style=cvdescStyle,
    )
    date = resume["curriculum"][0]["Experience"][1]["date"]
    datePara = Paragraph(date, style=dateStyleHighlight)

    data = []

    for i, value in enumerate(resume["curriculum"]):
        val = list(value.keys())[0]
        para = Paragraph(val, style=categoryStyle)
        data.append(["", [hr, para], ""])
        data.append(["", Spacer(10, 10), ""])
        for index, j in enumerate(resume["curriculum"][i][val]):
            if index == 0:
                titlePara = Paragraph(j["title"], style=cvtitleHighlightStyle)
                subtitlePara = Paragraph(j["subtitle"], style=cvsubtitleStyle)
                descriptionPara = Paragraph(
                    j["description"],
                    style=cvdescStyle,
                )
                date = j["date"]
                datePara = Paragraph(date, style=dateStyleHighlight)
            else:
                titlePara = Paragraph(j["title"], style=cvtitleStyle)
                subtitlePara = Paragraph(j["subtitle"], style=cvsubtitleStyle)
                descriptionPara = Paragraph(
                    j["description"],
                    style=cvdescStyle,
                )
                date = j["date"]
                datePara = Paragraph(date, style=dateStyle)
            data.append([datePara, [titlePara, subtitlePara, descriptionPara], ""])
            data.append(["", Spacer(10, 10), ""])

    table2 = Table(
        data,
        colWidths=[
            col + colWithGutter,
            colWithGutter * 8,
            colWithGutter + col,
        ],
        style=[
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            # ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ],
    )
    elements.append(table2)

    elements.append(PageBreak())

    letterDateStyle = ParagraphStyle(
        "letter date",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLightItalic",
        fontSize=template["letter_date_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=8,
        spaceBefore=8,
        textColor=template["letter_date_color"],
        textTransform=template["letter_date_case"],
        wordWrap=None,
    )

    letterReceiverStyle = ParagraphStyle(
        "letter receiver",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLight",
        fontSize=template["letter_receiver_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=5,
        spaceBefore=5,
        textColor=template["letter_receiver_color"],
        leading=template["letter_receiver_line_height"],
        textTransform=template["letter_receiver_case"],
        wordWrap=None,
    )

    date = Paragraph(resume["letter"]["date"], style=letterDateStyle)
    recipient = Paragraph(
        f"To {resume['letter']['recipient']}", style=letterReceiverStyle
    )

    data = [["", hr, ""], [date, "", ""], ["", recipient, ""], ["", "", ""]]

    table3 = Table(
        data,
        colWidths=[
            col + colWithGutter,
            colWithGutter * 8,
            colWithGutter + col,
        ],
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("ALIGN", (0, 0), (0, 0), "LEFT"),
            # ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ],
    )
    elements.append(table3)

    elements.append(Spacer(10, 20))

    lettertextStyle = ParagraphStyle(
        "letter text",
        parent=styles["Normal"],
        alignment=4,
        fontName="RobotoRegular",
        fontSize=template["letter_text_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=10,
        spaceBefore=10,
        textColor=template["letter_text_color"],
        leading=template["letter_text_line_height"],
        textTransform="Capitalize",
        wordWrap=None,
        firstLineIndent=24,
    )

    textPara = Paragraph(resume["letter"]["text"], style=lettertextStyle)

    data = [["", textPara, ""]]

    table4 = Table(
        data,
        colWidths=[
            col + colWithGutter,
            colWithGutter * 8,
            colWithGutter + col,
        ],
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            # ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ],
    )
    elements.append(table4)

    elements.append(Spacer(10, 20))

    letterFormulationStyle = ParagraphStyle(
        "letter date",
        parent=styles["Normal"],
        alignment=0,
        fontName="RobotoLightItalic",
        fontSize=template["letter_date_size"],
        leftIndent=12,
        rightIndent=12,
        spaceAfter=0,
        spaceBefore=5,
        textColor=template["letter_date_color"],
        textTransform="Capitalize",
        wordWrap=None,
    )

    formulation = Paragraph(
        resume["letter"]["formulation"], style=letterFormulationStyle
    )
    recipient = Paragraph(resume["letter"]["author"], style=letterReceiverStyle)

    stamp = Image(resume["letter"]["stamp"], colWithGutter * 2, rowWithGutter * 2)

    data = [[[formulation, recipient], stamp, ""]]

    table5 = Table(
        data,
        colWidths=[
            col + colWithGutter,
            colWithGutter * 8,
            colWithGutter + col,
        ],
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("ALIGN", (0, 0), (0, 0), "RIGHT"),
            # ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ],
    )
    elements.append(table5)

    doc.build(elements)



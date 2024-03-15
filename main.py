from pprint import pprint

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from typing import List, Tuple, Optional

from reportlab.platypus import SimpleDocTemplate

font_name = 'Arial'

# Регистрация шрифта с поддержкой кириллицы
pdfmetrics.registerFont(TTFont(font_name, 'C:\\Windows\\Fonts\\ARIALN.TTF'))


def create_pdf(output_filename: str, personal_data: List[Tuple[str, str]], image_path: Optional[str] = None) -> None:
    pdf = SimpleDocTemplate(output_filename, pagesize=A4)
    flowables = []

    table = Table(personal_data, colWidths=[4 * cm, 4 * cm, 4 * cm], rowHeights=2 * cm)

    # Стилизация таблицы
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)
    flowables.append(table)

    # Сохранение PDF
    pdf.build(flowables)


# Пример данных и вызов функции
personal_info = [
    ("Фамилия", "Иванов"),
    ("Имя", "Иван"),
    # Добавьте остальные данные
]

create_pdf("output.pdf", personal_info)

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from typing import List, Tuple, Optional

font_name = 'Arial'

# Регистрация шрифта с поддержкой кириллицы
pdfmetrics.registerFont(TTFont(font_name, 'C:\\Windows\\Fonts\\ARIALN.TTF'))


def create_pdf(output_filename: str, personal_data: List[Tuple[str, str]], image_path: Optional[str] = None) -> None:
    # Создаем объект canvas для рисования PDF
    c = canvas.Canvas(output_filename, pagesize=A4)

    # Заголовок, выравнивание по центру
    c.setFont(font_name, 14)
    c.drawCentredString(10.5 * cm, 29 * cm, "Личный лист")

    # Таблица данных
    c.setFont(font_name, 12)
    table_top = 27 * cm
    for index, (label, value) in enumerate(personal_data):
        c.drawString(2 * cm, table_top - index * 1 * cm, f"{label}: {value}")

    # Место для фотографии
    c.rect(16 * cm, table_top - 1 * cm, 3 * cm, 4 * cm)

    # Вставка фотографии, если путь к изображению предоставлен
    if image_path is not None:
        c.drawImage(image_path, 16 * cm, table_top - 1 * cm, 3 * cm, 4 * cm)

    # Текст в нижней части страницы
    c.setFont(font_name, 10)
    c.drawString(2 * cm, 5 * cm, "Текст снизу страницы, который должен быть точно таким же, как на фото.")

    # Сохраняем PDF
    c.save()


# Пример данных и вызов функции
personal_info = [
    ("Фамилия", "Иванов"),
    ("Имя", "Иван"),
    # Добавьте остальные данные
]

create_pdf("output.pdf", personal_info)

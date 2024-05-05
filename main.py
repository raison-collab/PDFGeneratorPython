import pdfkit
from pdfkit.configuration import Configuration


def html_to_pdf(html: str, output_filename: str, config: Configuration):
    """
    Преобразовать html в pdf
    :param html: HTML код строкой (нужно, чтобы применить конфиг к pdfkit)
    :param output_filename: путь к выходному файлу
    :param config: конфиг pdfkit
    :return:
    """
    # Настройки для pdfkit
    options = {
        'encoding': 'UTF-8',
    }

    pdfkit.from_string(html, output_filename, options=options, configuration=config)


# Установка пути к wkhtmltopdf (путь до усполняемого файла в Windows это .exe)
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

with open('input.html', encoding='utf-8') as f:
    input_html = f.read()

    html_to_pdf(input_html, 'output.pdf', config)

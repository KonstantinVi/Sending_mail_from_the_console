"""
Работа с почтой.
Отправка писем.
"""
# Многокомпонентный объект.
from email.mime.multipart import MIMEMultipart
# Текст / HTML.
from email.mime.text import MIMEText
# Изображения.
from email.mime.image import MIMEImage
# Импорт библиотеки по работе с SMTP.
import smtplib
# Импорт настроек.
import _config


def send_email(to_add, subject, mail_text):
    """Создание и отправка письма"""
    msg = MIMEMultipart()
    msg['From'] = _config.user_name_from
    msg['To'] = to_add
    msg['Subject'] = subject
    msg.attach(MIMEText(mail_text, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    # server.set_debuglevel(True)
    server.login(_config.user_name_from, _config.pass_name_from)
    server.auth_plain()
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    try:
        # Создаём
        url_user = input('Введите Электронный адрес: ')
        message_header = input('Введите заголовок сообщения: ')
        message_body = input('Введите текст сообщения: ')

        send_email(url_user, message_header, message_body)
        print('Письмо успешно отправлено!')
    except Exception as e:
        print(f'Ошибка при отправке письма: {e}')

from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Разработка Telegram и MAX-ботов | Автоматизация бизнеса</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #333; line-height: 1.6; }
        .container { max-width: 800px; margin: 0 auto; padding: 40px 20px; }
        .hero { text-align: center; padding: 60px 20px; background: white; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 30px; }
        h1 { font-size: 32px; margin-bottom: 15px; color: #1a1a1a; }
        .subtitle { font-size: 18px; color: #666; margin-bottom: 30px; }
        .btn { display: inline-block; padding: 15px 30px; background: #4a90e2; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; transition: background 0.3s; }
        .btn:hover { background: #357abd; }
        .features { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
        .feature { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .feature h3 { margin-top: 0; color: #4a90e2; }
        .price-section { background: white; padding: 40px; border-radius: 12px; text-align: center; margin-bottom: 30px; }
        .price { font-size: 36px; font-weight: bold; color: #1a1a1a; margin: 10px 0; }
        .footer { text-align: center; color: #888; font-size: 14px; margin-top: 40px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>Боты и AI-агенты для вашего бизнеса</h1>
            <p class="subtitle">Автоматизирую общение с клиентами, сбор заявок и документооборот. Работаю с Telegram и MAX.</p>
            <a href="https://telegram-ai-bot-production-9af44adb.up.railway.app" class="btn">Посмотреть демо-бота</a>
        </div>

        <div class="features">
            <div class="feature">
                <h3>🤖 Бот-администратор</h3>
                <p>Отвечает на вопросы клиентов 24/7, записывает на услуги и собирает контакты.</p>
            </div>
            <div class="feature">
                <h3>📄 AI-агент</h3>
                <p>Создает счета, акты и договоры. Экономит время на рутине.</p>
            </div>
            <div class="feature">
                <h3>🔗 Интеграция с CRM</h3>
                <p>Все заявки автоматически падают в вашу amoCRM.</p>
            </div>
            <div class="feature">
                <h3>💬 Чат на сайте</h3>
                <p>Красивое окно общения прямо на вашем сайте.</p>
            </div>
        </div>

        <div class="price-section">
            <h2>Стоимость</h2>
            <div class="price">от 15 000 ₽</div>
            <p>Базовая настройка бота с ответами на вопросы и сбором заявок.</p>
            <p><em>Точная цена зависит от сложности проекта.</em></p>
            <a href="mailto:motor.adv@yandex.ru" class="btn" style="margin-top: 20px;">Написать мне</a>
        </div>

        <div class="footer">
            <p>Дмитрий | MOTOR-MEDIA | motor.adv@yandex.ru</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5001))
    print(f"Лендинг запущен на порту {port}")
    app.run(host="0.0.0.0", port=port)
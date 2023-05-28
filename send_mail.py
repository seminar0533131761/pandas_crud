from flask import Flask
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.office365.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='chaniSeminar@gmail.com',
    MAIL_PASSWORD='chani113',
    # MAIL_DEFAULT_SENDER='chani0533131761@gmail.com'
)
mail = Mail(app)
scheduler = BackgroundScheduler(daemon=True)


def send_email():
    with app.app_context():
        # Get the number of people who entered the system today (you need to implement this logic)
        number_of_people = 19

        # Compose the email
        subject = 'Daily Report'
        body = f'The number of people who entered the system today: {number_of_people}'
        recipients = ['chani0533131761@gmail.com']

        # Create and send the email message
        msg = Message(subject=subject, body=body, recipients=recipients)
        mail.send(msg)


@app.route('/start_scheduler')
def start_scheduler():
    scheduler.add_job(send_email, 'cron', hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute+1)  # Schedule the job to run at 7:00 AM
    scheduler.start()
    return 'Scheduler started.'


app.run(debug=True)

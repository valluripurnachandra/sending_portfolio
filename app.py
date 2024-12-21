from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'purnavalluri03@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'yuea lemf prow fcsa'  # Your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'purnavalluri03@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create email message
        msg = Message(
            subject='New Portfolio Contact Form Submission',
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
New contact form submission:

Name: {name}
Email: {email}
Message: {message}
            """,
            sender=app.config['MAIL_DEFAULT_SENDER']
        )
        
        # Send email
        mail.send(msg)
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        print(f"Error sending email: {str(e)}")  # For debugging
        flash('Sorry, there was an error sending your message. Please try again.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request

app = Flask(__name__)

# --- CONFIGURATION ---
# The email that will SEND the message (Your personal Gmail)
SENDER_EMAIL = "ifediaso15@gmail.com" 
# The App Password you generated (NOT your normal login password)
SENDER_PASSWORD = "zzio ysfa xqzr guoy" 

# The email that will RECEIVE the message (Your school mail)
RECEIVER_EMAIL = "iobi.2301688@stu.cu.edu.ng"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # 1. Get data from the form
    name = request.form.get('name')
    user_email = request.form.get('email')
    message_content = request.form.get('message')

    # 2. Prepare the Email
    subject = f"New Drone Inquiry from {name}"
    body = f"""
    You have received a new message from your website!
    
    Name: {name}
    Email: {user_email}
    
    Message:
    {message_content}
    """

    # Create the email structure
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # 3. Connect to Gmail Server and Send
    try:
        # 587 is the port for TLS (Transport Layer Security)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login using the App Password
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        # Send the email
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully!")
        
        # 4. Show the Success Page
        return render_template('success.html')
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        return f"Error sending message: {e}"

if __name__ == '__main__':
    app.run(debug=True)
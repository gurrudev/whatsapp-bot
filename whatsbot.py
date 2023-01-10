from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Connected!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    usr_msg = request.form.get('Body').lower()
    
    # Create reply
    bot_resp = MessagingResponse()
    msg = bot_resp.message();
    
    if 'hello' in usr_msg:
        msg.body("Hi there!, How may I help you?")
    else:
        msg.body("Sorry, I didn't get what you said!")

    return str(bot_resp)

if __name__ == "__main__":
    app.run(debug=True)

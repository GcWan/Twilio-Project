from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# export FLASK_APP
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
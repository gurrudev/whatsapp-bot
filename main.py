#WhatsApp + Telegram

#Libraries for whatsapp
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

#Libraries for telegram 
import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


def telegram():  
    bot = aiogram.Bot(token='API_KEY')
    dsp = Dispatcher(bot)

    # Define a function to handle messages
    @dsp.message_handler()
    async def handle_message(message: types.Message):
        # Get the text of the message
        text = message.text.lower()
    
        # Check if the message is a command
        if text.startswith('/'):
            # If it is a command, handle it
            if text == '/start':
                await message.reply("Hello, I am a Telegram bot! I can do the following:\n\n"
                                   "/start - Show this message\n"
                                   "/help - Show a list of commands\n"
                                   "/echo - Repeat a message\n")

            elif text == '/help':
                await message.reply("I can do the following:\n\n"
                                   "/start - Show a list of commands\n"
                                   "/help - Show this message\n"
                                   "/echo - Repeat a message\n")

            elif text.startswith('/echo'):
                # Get the text to repeat
                repeat = text[6:]
            
                # Check if there is any text
                if repeat:
                    # If there is text, repeat it
                    await message.reply(repeat)
                else:
                    # If there is no text, show an error message
                    await message.reply("Error: No message to repeat")
        
            else:
                # If the command is not recognized, show an error message
                await message.reply("Error: Unrecognized command")

        elif 'hello' in text or 'hi' in text:
            await message.reply("Hello, I am a Telegram bot! I can do the following:\n\n"
                                "/start - Show this message\n"
                                "/help - Show a list of commands\n"
                                "/echo - Repeat a message\n")

        elif 'who are you' in text:
            await message.reply("I am a Telegram bot!, how can I help you")

        else:
            # If the message is not a command, show a default response
            await message.reply("I'm sorry, I don't know how to respond to that")

    # Start the bot and listen for updates
    executor.start_polling(dsp)

   
  
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
    
    if 'hello' in usr_msg  or 'hi' in usr_msg or 'helo' in usr_msg:
        msg.body("Hi there, How may I help you?")

    elif 'who are you' in usr_msg:
        msg.body("I am a Whatsapp bot, how may I help you?")

    elif 'how are you' in usr_msg:
        msg.body("I am good, thank you!")
        msg.body("What can I do for you")

    else:
        msg.body("Sorry, I didn't get what you said!")

    return str(bot_resp)


def whatsapp():
  app.run(debug=True)


  
  
  
if __name__ == "__main__":
    while True:
        print("1. WhatsApp")
        print("2. Telegram")
        print("3. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            whatsapp()
            #app.run(debug=True)
            
        elif choice == 2:
            telegram()
            break
        elif choice == 3:
            break
        else:
            print("Invalid input!")


#!/usr/bin/env python3
import RPi.GPIO as GPIO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging time signal sys


GPIO_PIN = 2
TOKEN = os.getenv("BOT_TOKEN")
 
def terminateProcess(signalNumber, frame):
        print('Cleaning GPIO')
        GPIO.cleanup()
        sys.exit(0)

def openDoor(update, context):
        GPIO.output(GPIO_PIN, GPIO.LOW)
        context.bot.send_message(chat_id=update.message.chat_id, text='Entre poto')
        time.sleep(3)
        GPIO.output(GPIO_PIN, GPIO.HIGH)

def ioSetup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIO_PIN,GPIO.OUT)
        GPIO.output(GPIO_PIN, GPIO.HIGH)

def main():
        ioSetup()
        signal.signal(signal.SIGINT, terminateProcess)
        updater = Updater(token=TOKEN, use_context=True)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('open', openDoor))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
        main()

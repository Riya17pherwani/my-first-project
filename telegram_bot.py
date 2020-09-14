from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client,Data
import os

def turnoffthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="OK,turning off the light")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg')
  send_value(0)
def turnonthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="OK,turning on the light")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
  send_value(1)

ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
def send_value(value):
  bot = aio.feeds('bot')
  aio.send_data(bot.key,value)
  

def input_message(update, context):
  text=update.message.text
  if text == 'turnonthelight':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="OK,turning on the light")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
       
  elif text == 'turnoffthelight':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="OK,turning off the light")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg')
    
    
def start(update,context):
  start_message='''
/turnoffthelight or 'turn off':To turn off the led
/turnonthelight or 'turn on'  :To turn on the led 
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)


TOKEN =os.getenv('TOKEN')

u=Updater(TOKEN,use_context=True)
dp= u.dispatcher
dp.add_handler(CommandHandler('turnoffthelight',turnoffthelight))
dp.add_handler(CommandHandler('turnonthelight',turnonthelight))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
u.start_polling()
u.idle()
 

#import required libraries for telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



#import required libraries for adafruit
from Adafruit_IO import Client, Feed ,Data



#make a telegram bot using botfather and enter the API key here
app = ApplicationBuilder().token("5454771209:AAEYDCjO_qKbQ2sCMDcxfgKZsKAWDnE6I18").build()


#make commands using telegram bot and follow through adafruit API_IO_KEY and give specified value to feeds

#for lights to turn  on
async def turn_on_lights(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Lights turned on")
    aio = Client('vardhan11445', 'aio_eswW77cGORK72xNm7or4b8sLHL33')
    aio.send('light', 1)
    data = aio.receive('light')


#for lights to turn off
async def turn_off_lights(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Lights turned off")
    aio = Client('vardhan11445', 'aio_eswW77cGORK72xNm7or4b8sLHL33')
    aio.send('light', 0)
    data = aio.receive('light')




#for lights to fan off
async def turn_on_fan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("fan turned on")
    aio = Client('vardhan11445', 'aio_eswW77cGORK72xNm7or4b8sLHL33')
    aio.send('fan', 1)
    data = aio.receive('fan')


    
#for lights to fan off
async def turn_off_fan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("fan turned off")
    aio = Client('vardhan11445', 'aio_eswW77cGORK72xNm7or4b8sLHL33')
    aio.send('fan', 0)
    data = aio.receive('fan')
async def turn_on_fan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("fan turned on")
    aio = Client('vardhan11445', 'aio_eswW77cGORK72xNm7or4b8sLHL33')
    aio.send('fan', 1)
    data = aio.receive('fan')





#to read commands from bot channel
app.add_handler(CommandHandler("turnonlights",turn_on_lights))
app.add_handler(CommandHandler("turnofflights",turn_off_lights))
app.add_handler(CommandHandler("turnofffan",turn_off_fan))
app.add_handler(CommandHandler("turnonfan",turn_on_fan))



app.run_polling()


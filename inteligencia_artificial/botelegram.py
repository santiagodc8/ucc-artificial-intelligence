import logging
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

API_KEY = "Token telegramBot"
openai.api_key = "token API OpenAI"

messages = [{"role": "system", "content": "You are a kind helpful assistant"}]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def call_ChatGPT(message):
    if message:
        messages.append({"role": "user", "content": message})
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt="".join([msg["content"] for msg in messages]),
            max_tokens=150
        )
        reply = response.choices[0].text.strip()
        messages.append({"role": "assistant", "content": reply})
        return reply

def remove_first_word(s):
    words = s.split()
    if len(words) > 1:
        return ' '.join(words[1:])
    else:
        return ''

async def handle_text(update: Update, context: CallbackContext):
    message = update.message.text
    chat_id = update.message.chat_id
    if message.lower().startswith("dibuja"):
        await context.bot.send_message(chat_id=chat_id, text="Dibujando...")
        try:
            response = openai.Image.create(
                prompt=remove_first_word(message),
                n=1,
                size="1024x1024"
            )
            reply = response['data'][0]['url']
        except Exception as e:
            reply = "Error llamando al servicio de Image"
            logger.error(f"Error llamando al servicio de Image: {e}")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Pensando...")
        try:
            reply = call_ChatGPT(message)
        except Exception as e:
            reply = "Error llamando al servicio de ChatCompletion"
            logger.error(f"Error llamando al servicio de ChatCompletion: {e}")
        
    await context.bot.send_message(chat_id=chat_id, text=reply)

def main():
    application = Application.builder().token(API_KEY).build()

    application.add_handler(MessageHandler(filters.TEXT, handle_text))

    application.run_polling()

if __name__ == '__main__':
    main()

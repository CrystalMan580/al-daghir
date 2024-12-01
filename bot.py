from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
TOKEN: Final = '8146338670:AAGG89rQyPSNZz5u8zEF2APSMbzWdN6YmFE'
BOT_USERNAME: Final = '@mycubebot'

async  def satrt_command(update: Update, contex: ContexTypes.DEFAULT_TYPE ):
    await update.message.reply_text("halo do you need something from me ?")

async  def satrt_command(update: Update, contex: ContexTypes.DEFAULT_TYPE):
    await update.message.reply_text("halo do you need something from me ?")

async  def satrt_command(update: Update, contex: ContexTypes.DEFAULT_TYPE):
    await update.message.reply_text("halo do you need something from me ?")

async def nasheed_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Type the nasheed name you're looking for.")

# List all music files in a directory
def list_all_music(directory="music/"):
    try:
        music_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
        return music_files
    except FileNotFoundError:
        print("Directory not found!")
        return []

# Provide a song if it exists in the directory
def provide_song(song_name, directory="music/"):
    all_songs = list_all_music(directory)
    
    if song_name in all_songs:
        song_path = os.path.join(directory, song_name)
        return song_path
    else:
        return None

# Handle the song request from the user
async def handle_song_request(update: Update, context: CallbackContext):
    # Get the song name from the user's message
    song_name = update.message.text.strip()

    # List all available songs
    all_songs = list_all_music()
    available_songs = "\n".join(all_songs) if all_songs else "No songs available."

    # Check if the requested song is available
    song_path = provide_song(song_name)
    
    if song_path:
        # Send the song file (if possible) or a confirmation message
        await update.message.reply_text(f"Here is your song: {song_path}")
    else:
        # Respond with available songs if not found
        await update.message.reply_text(f"Song not found. Here are the available songs:\n{available_songs}")

def main():
    # Create an Updater instance using the bot token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers for the `/start` command and song requests
    dispatcher.add_handler(CommandHandler("start", nasheed_command))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_song_request))

    # Start the bot
    updater.start_polling()
    updater.idle()
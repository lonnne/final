MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

HOME_DIR = '/home/student/final'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token

BOT_TOKEN = "7000986103:AAEtQsp7WaWLLq2l1lJZLCndKZUKk4gKGfI"
FOLDER_ID = "b1gguda9iv0ev79trqvm"
IAM_TOKEN = "t1.9euelZrHl8ubycmPlpCVmI6Rz8yPl-3rnpWaxpeVyoqTm5aTy5XKi42SmM3l8_d_MBJO-e97ZjYr_N3z9z9fD07573tmNiv8zef1656Vms-Sk5vNjI7Pz42ZyJbOyJeO7_zF656Vms-Sk5vNjI7Pz42ZyJbOyJeOveuelZqJzsaJlpzJnZSbyZKZj8eblbXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.7ijLyZOuQKMyyG2YF0yWpdLHASkjJwDrq9wEYcfe4cy2QQ1rH8X57CoNEQL1KG2RNUOZfNLLnUgq8a2rqOe8BA"

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов
MAX_TTS_SYMBOLS = 500

LOGS = 'logs.txt'  # файл для логов
DB_FILE = 'messages.db'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом
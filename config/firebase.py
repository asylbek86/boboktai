import os

import firebase_admin
from firebase_admin import credentials

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Можно задать путь через переменную окружения FIREBASE_CREDENTIALS,
# иначе по умолчанию берем firebase-service-account.json в корне проекта.
FIREBASE_CRED_PATH = os.environ.get(
    "FIREBASE_CREDENTIALS",
    os.path.join(BASE_DIR, "firebase-service-account.json"),
)

if not firebase_admin._apps and os.path.exists(FIREBASE_CRED_PATH):
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)


import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://localhost"

if DATABASE_URL[7:10] != 'sql':
    DATABASE_URL = DATABASE_URL[:8] + 'ql' + DATABASE_URL[8:]

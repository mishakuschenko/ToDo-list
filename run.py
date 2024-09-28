from init import app
from routes import *

if __name__ == "__main__":
    try:
        dotenv.load_dotenv()
        app.debug=True
        app.run()
    except:
        print("ОШИБКА СТАРТА")


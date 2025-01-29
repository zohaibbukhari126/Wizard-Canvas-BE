from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'localhost'
PORT = '8900'
ENV = 'dev' 
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = '0.0.0.0'  # Render requires this for external access
PORT = '10000'  # Render uses port 10000 by default for Python apps
ENV = 'prod'  # Change to 'prod' for production
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Use environment variable
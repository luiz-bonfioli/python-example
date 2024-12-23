from src.common.config import WEB_SERVER_HOST, WEB_SERVER_PORT
from src.controller.app import app

# To run locally
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
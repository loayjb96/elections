import uvicorn

from elections_app.app.routers.main import app

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8010)

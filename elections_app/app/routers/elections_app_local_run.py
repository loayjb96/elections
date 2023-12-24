import uvicorn

from elections_app.app.routers.main import elections_app

if __name__ == '__main__':
    uvicorn.run(app=elections_app, host='0.0.0.0', port=8010)

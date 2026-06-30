from fastapi import FastAPI
from interface.api.routes import router
from chainlit.utils import mount_chainlit

app = FastAPI()
app.include_router(router)
mount_chainlit(app=app, target="interface/chat/my_cl_app.py", path='/chat')

def main() -> None:
    return None


if __name__ == '__main__':
    main()
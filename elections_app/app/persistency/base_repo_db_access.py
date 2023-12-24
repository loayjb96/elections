from abc import abstractmethod
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class BaseDbAccess:

    def __init__(self, db_config: Optional[dict] = None, db_url: Optional[str] = None, echo: bool = False):
        # db_config - used for running in actual env
        # db_url - used for running DB tests
        username: str = db_config.get('username', 'default')
        password: str = db_config.get('password', 'J1cGL3KPoBUt')
        host: str = db_config.get('dbhost', 'ep-calm-union-38725535-pooler.us-east-1.postgres.vercel-storage.com')
        port: str = db_config.get('dbport', '5432')
        database: str = db_config.get('database', 'verceldb')
        db_url = f'postgresql://{username}:{password}@{host}:{port}/{database}'

        self.engine: Engine = create_engine(db_url, echo=echo)
        self.session: Session = None

    def __del__(self):
        if self.session:
            self.session.close()
        self.engine.dispose()

    @staticmethod
    @abstractmethod
    def get_schema_name():
        pass

    def insert(self, entity):
        if self.session is None:
            self.session = Session(bind=self.engine)
        self.session.merge(entity)
        self.session.commit()

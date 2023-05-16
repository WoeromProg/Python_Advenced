if __name__ == '__main__':
    from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String
    from sqlalchemy.orm import sessionmaker, mapper, registry

    engine = create_engine("sqlite:///python2.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    metadata = MetaData()
    mapper_registry = registry()
    users = Table('users', mapper_registry.metadata,
                  Column('id', Integer, primary_key=True),


                  Column('email', String(50)),
                  Column('login', String(50), nullable=False))


    class User:
        def __int__(self, name, email, login):
            self.name = name
            self.email = email
            self.login = login

        def __repr__(self):
            return f"{self.name}, {self.email}, {self.login}"


    mapper_registry.map_imperatively(User, users)
    metadata.create_all(bind=engine)

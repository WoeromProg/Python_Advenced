if __name__ == '__main__':
    # from sqlalchemy import create_engine, text
    # from sqlalchemy import sql
    # engine = create_engine("sqlite:///python.db")
    # with engine.connect() as connection:
    #     create_user_table_q = text("CREATE TABLE IF not EXISTS users ("
    #                                "id integer PRIMARY KEY,"
    #                                "name text NOT NULL)")
    #     connection.execute(create_user_table_q)
    #
    #     insert_q = text("INSERT INTO users(name) values('Nikita')")
    #     connection.execute(insert_q)
    #
    #     filter_query = text("SELECT * FROM users WHERE id=:user_id")
    #     cursor = connection.execute(filter_query, {'user_id': 1})
    #
    #     result = cursor.fetchone()
    #     print(result)
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///python.db")

    Session = sessionmaker(bind=engine)
    Session = Session()
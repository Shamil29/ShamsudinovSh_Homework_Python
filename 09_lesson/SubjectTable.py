from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select": text("select * from subject"),
        "insert new": text("insert into subject(subject_id, subject_title) values (:new_id, :new_title)"),
        "delete by id": text("delete from subject where subject_id = :id_to_delete"),
        "edit by id": text("update subject set subject_title = :new_title where subject_id = :new_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string).connect()

    def get_subject(self):
        result = self.__db.execute(self.__scripts["select"]).fetchall()
        return result

    def create(self, new_id, new_title):
        self.__db.execute(self.__scripts["insert new"], {"new_id": new_id, "new_title": new_title})
        self.__db.commit()

    def delete(self, new_id):
        self.__db.execute(self.__scripts["delete by id"],
                          {"id_to_delete": new_id})
        self.__db.commit()

    def edit(self, subject_id, new_title):
        self.__db.execute(self.__scripts["edit by id"],
                          {"new_id": subject_id, "new_title": new_title})
        self.__db.commit()

    def get_subject_by_id(self, subject_id):
        result = self.__db.execute(self.__scripts["select by id"],
                                   {"new_id": subject_id}).fetchall()
        return result

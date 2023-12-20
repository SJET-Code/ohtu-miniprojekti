"""Functions to save and get citations from the database"""
from sqlalchemy import text
from entities.reference import Reference
from services.validation_service import ValidationType

class CitationRepository:
    def __init__(self, db, validation_service):
        self.db = db
        self.__validation_service = validation_service

    def create_citation(self, ref_type, key, author, title, year, user_id = 1):
        self.__validation_service.validate(key, ValidationType.REFERENCE_KEY)
        self.__validation_service.validate(author, ValidationType.AUTHOR)
        self.__validation_service.validate(title, ValidationType.TITLE)
        self.__validation_service.validate(year, ValidationType.YEAR)

        sql = text("""INSERT INTO citations
                    (user_id, type, key, author, title, year)
                    VALUES (:user_id, :type, :key, :author, :title, :year)""")
        self.db.session.execute(sql, {"user_id": user_id, "type": ref_type, "key": key,
                                "author": author, "title": title, "year": year})
        self.db.session.commit()

    def get_citations(self, user_id = 1):
        sql = text("SELECT * FROM citations WHERE user_id=:user_id")
        result = self.db.session.execute(sql, {"user_id": user_id})
        citations = result.fetchall()
        return self._convert_to_citation_objects(citations)

    def delete_citation(self, key, user_id = 1):
        sql = text("DELETE FROM citations WHERE key=:key and user_id=:user_id")
        self.db.session.execute(sql, {"key": key, "user_id": user_id})
        self.db.session.commit()

    def delete_all_citations(self, user_id = 1):
        sql = text("DELETE FROM citations WHERE user_id=:user_id")
        self.db.session.execute(sql, {"user_id": user_id})
        self.db.session.commit()

    def _convert_to_citation_objects(self, fetched_data:list):
        return_list = []
        for db_tuple in fetched_data:
            # db_tuple format: ({id}, {user_id}, {type}, {key}, {author}, {title}, {year})
            citation_object = Reference(db_tuple[2], db_tuple[3], db_tuple[4],
                                         db_tuple[5], db_tuple[6])
            return_list.append(citation_object)
        return return_list

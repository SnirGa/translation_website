import psycopg2


class Searcher:
    def __init__(self,user, password, db, host):
        self.user = user
        self.password = password
        self.db = db
        self.host = host

    def get_melingo_id(self, word):
        try:
            conn = self.__get_conn()
            cursor = conn.cursor()
            sql_query = """
                SELECT "MelingoId" FROM "Entriesnodu"
                WHERE "Entry" = %s;
            """
            cursor.execute(sql_query, (word,))
            melingo_id = cursor.fetchone()
            cursor.close()
            conn.close()
            return melingo_id
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")

    def get_translation(self, word):
        try:
            conn = self.__get_conn()
            cursor = conn.cursor()
            melingo_id = self.get_melingo_id(word)
            sql_query = """
                SELECT "TranslationFull" FROM "Entriesnodu"
                WHERE "MelingoId" = %s;
            """
            cursor.execute(sql_query, (melingo_id,))
            translation = cursor.fetchone()
            cursor.close()
            conn.close()
            return translation
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")

    def get_examples(self, word):
        try:
            conn = self.__get_conn()
            cursor = conn.cursor()
            melingo_id = self.get_melingo_id(word)
            sql_query = """
                SELECT "Text" FROM "Examples"
                WHERE "MelingoID" = %s;
            """
            cursor.execute(sql_query, (melingo_id,))
            examples = cursor.fetchall()
            cursor.close()
            conn.close()
            return examples
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")

    def __get_conn(self):
        conn = psycopg2.connect(
            host=self.host,
            database=self.db,
            user=self.user,
            password=self.password
        )
        return conn



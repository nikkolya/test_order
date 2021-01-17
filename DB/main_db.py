import sqlite3


class DB:
    def __init__(self):
        self.connect = sqlite3.connect("./DB/for_test.db3")
        self.check_test_table()  # Если запуск первый, то будет создана таблица с индексом

    def get_text(self, text):
        cursor = self.connect.cursor()
        exec = """
SELECT *
FROM test_table
WHERE text LIKE ('%{}%')
ORDER BY created_date
LIMIT 20
        """.format(text)
        fetch = cursor.execute(exec).fetchall()
        cursor.close()
        return fetch

    def put_text(self, rubrics, text, created_date):
        cursor = self.connect.cursor()
        str_rubr = ','.join(rubrics)
        exec = """
INSERT INTO test_table
(rubrics,text,created_date)
VALUES
(?,?,?)
        """
        cursor.execute(exec, (str_rubr, text, created_date,))
        self.connect.commit()
        cursor.close()
        return cursor.lastrowid

    def del_text(self, row_ID):
        cursor = self.connect.cursor()
        exec = """
DELETE FROM test_table
WHERE ID = ?
        """
        cursor.execute(exec, (row_ID,))
        self.connect.commit()
        return cursor.rowcount

    def check_test_table(self):
        cursor = self.connect.cursor()
        try:
            cursor.execute("SELECT * FROM test_table")
        except:
            exec = """
    CREATE TABLE test_table (
        id           INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                             UNIQUE ON CONFLICT ROLLBACK
                             NOT NULL,
        rubrics      VARCHAR NOT NULL,
        text         VARCHAR NOT NULL,
        created_date DATE    NOT NULL
    );   
            """
            cursor.execute(exec)
            self.connect.commit()
            exec = """
    CREATE UNIQUE INDEX test_index ON test_table (
        id ASC,
        text ASC
    );
            """
            cursor.execute(exec)
            self.connect.commit()
            cursor.close()

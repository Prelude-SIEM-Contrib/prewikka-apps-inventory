from prewikka.database import SQLScript


class SQLUpdate(SQLScript):
    type = "install"
    version = "0"

    def run(self):
        self.query("""
DROP TABLE IF EXISTS Prewikka_Inventory;

CREATE TABLE Prewikka_Inventory (
    hostname TEXT NOT NULL,
    address TEXT NULL,
    os TEXT NULL
);
""")

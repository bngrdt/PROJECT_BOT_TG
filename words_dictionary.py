from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('words.db')


class Word(Model):
    word = CharField()
    translate = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Word])

if __name__ == '__main__':
    db.close()

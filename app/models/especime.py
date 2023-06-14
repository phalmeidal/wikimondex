import datetime
import db

class Especime(db.Model):
    __table_name__ = 'especime'

    id = db.Column(db.Integer,primary_key=True)
    apelido = db.Column(db.String, nullable=False)
    altura = db.Column(db.Float, nullable = False)
    peso = db.Column(db.Float, nullable = False)
    _data_cadastro = db.Column('data_cadastro', db.Date, nullable=False)

    @property
    def data_cadastro(self):
        return self._data_nascimento

    @data_cadastro.setter
    def data_nascimento(self, value):
        self._data_nascimento = datetime.strptime(value, '%Y-%m-%d').date()
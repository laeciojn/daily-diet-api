from database import db
from datetime import datetime, timezone


class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.String(80), nullable=False)
    data_refeicao = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    dentroDaDieta = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_refeicao": self.data_refeicao.isoformat(),
            "dentroDaDieta": self.dentroDaDieta
        }
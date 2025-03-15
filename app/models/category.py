from app.extensions import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)
    
    def __repr__(self):
        return f"<Category {self.id} - {self.name}>"



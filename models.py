from dynamic import db

class ElementType(db.Model):
    __tablename__ = "element_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    elements = db.relationship(
        'Element',
        backref='element_type',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<ElementType %r>" % self.name

class Element(db.Model):
    __tablename__ = "element"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    symbol = db.Column(db.String(2))
    element_type_id = db.Column(
        db.Integer,
        db.ForeignKey("element_type.id")
    )

    def __init__(self, name, symbol, element_type):
        self.name = name
        self.symbol = symbol
        self.element_type_id = element_type.id

    def __repr__(self):
        return "<Element %r (%r)>" % (self.name, self.symbol)

class Alloy(db.Model):
    __tablename__ = "alloy"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    element_1_id = db.Column(
        db.Integer,
        db.ForeignKey("element.id")
    )
    element_2_id = db.Column(
        db.Integer,
        db.ForeignKey("element.id")
    )
    element_3_id = db.Column(
        db.Integer,
        db.ForeignKey("element.id"),
        nullable=True
    )
    has_segregation = db.Column(db.Boolean, default=False)

    def __init__(self, element_1, element_2, element_3=None,
                    has_segregation=False):
        self.element_1_id = element_1.id
        self.element_2_id = element_2.id
        if element_3:
            self.element_3_id = element_3.id
            self.name = "%s_{x} %s_{1-x} %s" % (
                element_1.symbol,
                element_2.symbol,
                element_3.symbol
            )
        else:
            self.element_3_id = None
            self.name = element_1.symbol + element_2.symbol
        self.has_segregation = has_segregation

    def __repr__(self):
        return "<Alloy %r>" % self.name

class Device(db.Model):
    __tablename__ = "device"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    monolayers = db.relationship('Monolayer', backref='device', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Device %r>" % self.name

class Monolayer(db.Model):
    __tablename__ = "monolayer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    alloy_id = db.Column(db.Integer, db.ForeignKey('alloy.id'))
    temperature = db.Column(db.Float, default=0.0)
    segregation_coef = db.Column(db.Float, default=0.0)
    x_fraction = db.Column(db.Float, default=0.0)
    
    def __init__(self, device, alloy, temperature=0.0, segregation_coef=0.0,
                    x_fraction=0.0):
        self.device_id = device.id
        self.alloy_id = alloy.id
        self.name = "(%s, T=%.2f, R=%.2f, x=%.2f)" % (
            alloy.name, temperature, segregation_coef, x_fraction
        )
        self.temperature = temperature
        self.segregation_coef = segregation_coef
        self.x_fraction = x_fraction
        
    def __repr__(self):
        return "<Monolayer %r>" % self.name
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class CountryStats(Model):
    id = Column(Integer, primary_key=True)
    stat_date = Column(Date, nullable=True)
    population = Column(Float)
    unemployed_perc = Column(Float)
    poor_perc = Column(Float)
    college = Column(Float)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    country = relationship("Country")

    def college_perc(self):
        if self.population != 0:
            return (self.college*100)/self.population
        else:
            return 0.0

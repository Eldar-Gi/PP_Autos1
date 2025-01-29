from pydantic import BaseModel
import datetime


class CarsSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    pagaminimo_metai: int
    kaina: float

    class Config:
        from_atributes = True

from fireo.fields import IDField, TextField, NumberField
from fireo.models import Model


class Translation(Model):
    id = IDField()
    ayah_id = TextField()
    ayah_number = NumberField()
    edition_id = TextField()
    text = TextField()
import datetime
from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    count_friends = None

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | VaccineError:
        current_date = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"

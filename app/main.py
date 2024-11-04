from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_friends += 1

    if count_friends > 0:
        return f"Friends should buy {count_friends} masks"

    return f"Friends can go to {cafe.name}"

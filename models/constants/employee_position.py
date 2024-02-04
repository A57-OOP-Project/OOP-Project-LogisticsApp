class EmployeePosition:
    REGULAR = 'regular'
    SUPERVISOR = 'supervisor'
    MANAGER = 'manager'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.REGULAR, cls.SUPERVISOR, cls.MANAGER]:
            raise ValueError(
                f'None of the possible employee positions  matches the value {value}.')

        return value
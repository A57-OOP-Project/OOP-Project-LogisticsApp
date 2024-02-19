class EmployeePosition:
    REGULAR = 'regular'
    SUPERVISOR = 'supervisor'
    MANAGER = 'manager'

    @classmethod
    def validate_position(cls, value):
        if value not in [cls.REGULAR, cls.SUPERVISOR, cls.MANAGER]:
            raise ValueError(
                f'None of the possible employee positions  matches the value {value}.')

        #return value

# Not used
# For further development
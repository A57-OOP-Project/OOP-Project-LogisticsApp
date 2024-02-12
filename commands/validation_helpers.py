from errors.invalid_params import InvalidParams


def validate_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) != count:
        raise InvalidParams(cmd_name, count)



def try_parse_int(int_string: str, msg: str):
    try:
        return int(int_string)
    except:
        raise ValueError(msg)



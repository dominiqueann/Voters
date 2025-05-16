def is_eligible_to_vote(age, is_citizen):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 18 and is_citizen:
        return True
    return False


def is_not_eligible_to_vote(age):
    if age < 18:
        return True
    return False

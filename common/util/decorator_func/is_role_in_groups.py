"""

"""


def is_role_in_group(roles, groups):
    for role in roles:
        for group in groups:
            if role.value == group.name:
                return True

    return False

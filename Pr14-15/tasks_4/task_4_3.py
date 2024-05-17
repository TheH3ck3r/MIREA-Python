def if_then_else(condition):
    return lambda then_branch: lambda else_branch: condition(then_branch)(else_branch)


print(if_then_else(lambda x: lambda y: x)("Истина")("Ложь"))
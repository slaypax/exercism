def sum_of_multiples(limit, multiples):
    values_to_sum = []
    if 0 in multiples:
        multiples.remove(0)
    for value in range(1, limit):
        for multiple in multiples:
            if value % multiple == 0 and value not in values_to_sum:
                values_to_sum.append(value)
    return sum((values_to_sum))
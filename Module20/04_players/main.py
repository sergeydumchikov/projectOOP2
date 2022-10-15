def players_tuple(peoples):
    result = []
    for i_name, i_points in peoples.items():
        name_tuple = i_name[0], i_name[1], i_points[0], i_points[1], i_points[2]
        result.append(name_tuple)

    return result



players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

printer = players_tuple(players)

print(printer)
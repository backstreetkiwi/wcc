import itertools

def cube_definition():
    return [
        [  1,  8, 15, 22, 29, 99 ],
        [  2,  9, 16, 23, 30,  1 ],
        [  3, 10, 17, 24, 31,  1 ],
        [  4, 11, 18, 25,  1,  2 ],
        [  5, 12, 19, 26,  2, 99 ],
        [  6, 13, 20, 27,  3, 99 ],
        [  7, 14, 21, 28,  4, 31 ]
    ]

def weeks_to_test():
    normal_weeks = [ [ i for i in range(i, i+7)] for i in range(1, 22) ]
    last_days = [d for d in range(28, 32)] # 28 .. 31
    break_weeks = [ [ prev_day for prev_day in range(last_day-6+x, last_day) ] + [last_day] + [ following_day for following_day in range(1, 1+x) ] 
        for x in range(0,7) for last_day in last_days ]
    return normal_weeks + break_weeks

def print_week(week):
    print(' '.join([f"{day :02}" for day in week]))

def day_to_cube_index(cube_definition):
    return { day: [ cube_index for cube_index in range(1, 8) if day in cube_definition[cube_index-1]] for day in range (1, 32)}

def test_week(week, day_to_cube_index):
    possible_cubes = [ day_to_cube_index[day] for day in week]
    matching = [list(selected_cubes) for selected_cubes in itertools.product(*possible_cubes) if len(set(selected_cubes))==7 ]
    if len(matching)>0:
        pretty_week = ' '.join([f"{day :02}" for day in week])
        print(f"{pretty_week} -> {matching[0]}")
    return len(matching) > 0 

if __name__ == "__main__":

    weeks_to_test = weeks_to_test()
    cube_definition = cube_definition()
    day_to_cube_index = day_to_cube_index(cube_definition)

    for week in weeks_to_test:
        if(not test_week(week, day_to_cube_index)):
            pretty_week = ' '.join([f"{day :02}" for day in week])
            print(pretty_week + " :-(")

    print()
    flattened_cube_config = [x for sublist in cube_definition for x in sublist]
    print([x for x in set(flattened_cube_config) if flattened_cube_config.count(x)==1])

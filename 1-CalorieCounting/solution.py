if __name__ == "__main__":

    calorie_dict = {}
    elf_idx = 0

    with open('calories_test.txt') as f:
        lines = f.readlines()

    lines_clean = map(
        lambda x: x.strip('\n'),
        lines
    )

    lines_int = map(
        lambda x: int(x) if x != '' else x,
        lines_clean
    )
    
    for calorie in lines_int:
        if calorie == '':
            elf_idx += 1
        else:
            if elf_idx not in calorie_dict:
                calorie_dict[elf_idx] = calorie
            else:
                calorie_dict[elf_idx] += calorie

    sorted_calorie_dict = dict(sorted(calorie_dict.items(), reverse=True, key=lambda cal: cal[1]))
    
    total_cals = 0
    for i in range(3):
        total_cals += sorted_calorie_dict[list(sorted_calorie_dict.keys())[i]]

    print(total_cals)
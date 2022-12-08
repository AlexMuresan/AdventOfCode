def countTotalOverlap(pairing):
    sections = pairing.split(',')

    full_sections = []
    for section in sections:
        min_section, max_section = section.split('-')
        min_section = int(min_section)
        max_section = int(max_section)+1

        full_sections.append(set(range(min_section, max_section)))

    if full_sections[1].issubset(full_sections[0]) or full_sections[0].issubset(full_sections[1]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    with open('train.txt', 'r') as f:
        lines = f.readlines()

    clean_lines = list(map(lambda x: x.strip('\n'), lines))
    
    print(sum(list(map(countTotalOverlap, clean_lines))))

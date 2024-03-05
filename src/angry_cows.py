# Second lab 3 level 3 option

def min_distance_between_cows(free_sections, num_cows):
    free_sections.sort()
    left = 0
    right = free_sections[-1] - free_sections[0]
    while left <= right:
        middle = (left + right) // 2
        if can_place_cows(free_sections, num_cows, middle):
            left = middle + 1
        else:
            right = middle - 1
    print(right)
    return right


def can_place_cows(sections, num_cows, distance):
    count_cows = 1
    left_cow = 0
    for i in range(1, len(sections)):
        if sections[i] - sections[left_cow] >= distance:
            count_cows += 1
            left_cow = i
    if count_cows >= num_cows:
        return True
    else:
        return False


arr = [1, 2, 8, 4, 9]
min_distance_between_cows(arr, 3)

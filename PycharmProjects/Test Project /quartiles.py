samples = sorted([3, 7, 8, 5, 12, 14, 21, 13, 18])

def find_median(sorted_list):
    indices = []

    list_size = len(sorted_list)
    median = 0

    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))

        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        pass
    else:
        indices.append(int(list_size / 2))

        median = sorted_list[indices[0]]
        pass28, 12, 8, 27, 16, 31, 14, 13, 19, 1, 1, 22, 13

    return median, indices
    pass

median, median_indices = find_median(samples)
Q1, Q1_indices = find_median(samples[:median_indices[0]])
Q2, Q2_indices = find_median(samples[median_indices[-1] + 1:])

quartiles = [Q1, median, Q2]

print("(Q1, median, Q3): {}".format(quartiles))
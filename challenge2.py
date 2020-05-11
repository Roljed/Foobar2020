import itertools

LEN_MAJOR = 1
LEN_MINOR = 2


def _inner_sort(y):
    """
    Sorts dict of versions into dict of minors with a list of revisions inside a dict of majors.
    :param y: Dict of versions, arranged by major key.
    :return: New sorted dict.
    """
    out_dict = {}
    for major in y:
        out_dict[major] = {}
        for version in y[major]:
            minor = -1
            revision = -1
            version_list = version.split('.')
            if len(version_list) > LEN_MAJOR:
                minor = int(version_list[1])
                if len(version_list) > LEN_MINOR:
                    revision = int(version_list[2])

            if minor not in out_dict[major]:
                out_dict[major][minor] = []
            out_dict[major][minor].append(revision)
    return out_dict


def solution2_1(x):
    """
    Sort and print revisions by order.
    :param x: list of values to sort by revisions.
    :return: None.
    """
    majors = []
    versions = {}
    for num in x:
        num_split = num.split('.')
        major = int(num_split[0])
        if major not in majors:
            majors.append(major)
            major_indexes = [i for i, version in enumerate(x) if int(version.split('.')[0]) == major]
            versions[major] = [x[i] for i in major_indexes]

    _print_solution(_inner_sort(versions))


def _print_solution(z):
    """
    Print dict of revisions by order.
    :param z: Dict of revisions.
    :return: None.
    """
    output = ''
    major_sorted = sorted(z.keys())
    for major in major_sorted:
        minor_sorted = sorted(z[major].keys())
        for minor in minor_sorted:
            if minor != -1:
                revision_sorted = sorted(z[major][minor])
                for revision in revision_sorted:
                    output = output + str(major) + '.' + str(minor)
                    if revision != -1:
                        output = output + '.' + str(revision)
                    output = output + ','
            else:
                output = output + str(major) + ','

    print(output[:-1])


def sub_challenge1():
    print("----- Sub Challenge 1 -----")
    test2_1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    result2_1 = '0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0'
    solution2_1(test2_1)
    print(result2_1)


def solution2_2(l):
    mega_permutations_list = []
    i = 1
    while i <= len(l):
        permutations = list(itertools.permutations(l, i))
        mega_permutations_list.append(permutations)
        i = i + 1

    divisible_3 = []
    for permutations in mega_permutations_list:
        for numbers in permutations:
            number = int(''.join(map(str, numbers)))
            if number >= 3 and number % 3 == 0:
                divisible_3.append(number)

    if len(divisible_3) != 0:
        return max(divisible_3)
    else:
        return 0


def sub_challenge2():
    print("----- Sub Challenge 2 -----")
    test2_2 = [3, 1, 4, 1]
    result2_2 = 4311
    print(solution2_2(test2_2))
    print(result2_2)

    test2_3 = [3, 1, 4, 1, 5, 9]
    result2_3 = 94311
    print(solution2_2(test2_3))
    print(result2_3)
    pass


if __name__ == '__main__':
    sub_challenge1()
    sub_challenge2()

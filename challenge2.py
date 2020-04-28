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


if __name__ == '__main__':
    test2_1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    result2_1 = '0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0'
    solution2_1(test2_1)
    print(result2_1)

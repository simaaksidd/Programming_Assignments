# There are 3 merges, a left merge, a right merge, and a both merge.
# right merge: smaller or equal idx 0 and larger idx 1
# left merge: smaller or equal idx 1 and larger idx 0
# Both merge: idx 0 is larger and idx 1 is smaller
def merge_tuples(tuples_list):
    # First we want to get rid of all duplicates
    cleaned = set(tuples_list)
    cleaned = list(cleaned)
    cleaned.sort()
    print(cleaned)
    # Since this is a sorted list with no duplicates, 
    #         we know that we do not need left merge and
    #         we know that we need to add the first value to new_list
    new_list = [cleaned[0]]

    # Now we want to compare the smaller and larger 
    #         values of the tuples (besides the first 1!)
    for tuples in cleaned[1:]:
        # In the new list, we have 1 value at the start,
        #         we want to compare to it once, but then 
        #         after we want the more recent value because 
        #         we will have known that the previous value
        #         is completely separate from the others 
        #         to do this, set "boundaries" for the smaller and
        #         larger values of the most recent addition to new_list
        smaller_boundary = new_list[-1][0]
        larger_boundary = new_list[-1][1]
        # right merge 
        if tuples[0] <= larger_boundary and larger_boundary < tuples[1]:
            new_list[-1] = smaller_boundary, tuples[1]

        # new distinct value
        elif larger_boundary < tuples[0]:
            new_list.append((tuples[0], tuples[1]))

    return new_list

tuples = [(-25, -14), (-24, -15), (-21, -16), (-20, -15), (-10, -7), (-8, -5), (-6, -3), (2, 3), (2, 4), (3, 6), (12, 15), (13, 18), (14, 17), (22, 27), (25, 30), (26, 29)]
print(merge_tuples(tuples))
import collections
def leastInterval( tasks, n):
    """
    1. Find the most occurred task(s). The number of the most occurred
        tasks could be less than or more than the given n.

        For example:

        #1 scenario - the number of kinds of the most occurred tasks < n
        A, A, A, A, B, B, B, B, C, C, D where n = 5
        count(A) = 4
        count(B) = 4
        count(C) = 2
        count(D) = 1

        2 < 5

        #2 scenario - the number of kinds of the most occurred tasks > n
        A, A, A, B, B, B, C, C, C, E, E, F, G, H, I where n = 2
        count(A) = 3
        count(B) = 3
        count(C) = 3
        count(E) = 2
        count(F) = 1
        count(G) = 1
        count(H) = 1
        count(I) = 1

        3 > 2

    2. Generate the buckets, which are prefixed with the most occurred
        task(s).

        For example:

        #1 scenario
        A B _ _ _ _ | A B _ _ _ _ | A B _ _ _ _ | A B ...
        bucket#1    | bucket#2    | bucket#3    | ...

        #2 scenario
        A B C | A B C | A B C ...
        #1    | #2    | ...

    3. Fill in the remaining tasks (as evenly as possible) into the each
        bucket.

        For example:

        #1 scenario
        A B _ _ _ _ | A B _ _ _ _ | A B _ _ _ _ | A B ...
        A B C _ _ _ | A B _ _ _ _ | A B _ _ _ _ | A B ...
        A B C _ _ _ | A B C _ _ _ | A B _ _ _ _ | A B ...
        A B C _ _ _ | A B C _ _ _ | A B D _ _ _ | A B ...

        Result: 20 intervals

        #2 scenario
        A B C | A B C | A B C ...
        A B C E | A B C | A B C ...
        A B C E | A B C E | A B C ...
        A B C E F | A B C E | A B C ...
        A B C E F | A B C E G | A B C ...
        A B C E F H | A B C E G | A B C ...
        A B C E F H | A B C E G I | A B C ...

        Result: 15 intervals

    4. Explanations

        1) At the beginning we count the occurrence for each task and
            find out the most occurred task(s).
        2) We always take the most occurred tasks as one group and put it
            into a bucket. As in #1 scenario, "A B" is a group; while in
            #2 scenario, "A B C" is a group.
        2) The difference is that in #1 scenario, after we group them we
            have empty slots left, however in #2 scenario, we used up all
            the empty slots.
        3) Fill in the empty slots by rolling the buckets. For example, if
            we have bucket#1, #2, #3 and there are "C, C, D, E" left, we
            put the first "C" into bucket#1, the second "C" into bucket#2,
            "D" into bucket#3, "E" into bucket#1. Note that even we run out
            of the empty slot, we can still add tasks into the bucket.
            By doing this, we are guaranteed that every remaining task we
            put into the bucket won't have conflicts (because they are
            separated by the most occurred tasks, and even they won't have
            any conflicts.)

    5. Equation

        The minimum intervals that the CPU can schedule without having
        conflicts for the most occurred task(s):

        (k - 1) * (n + 1) + p

        k is the count for the most occurred task. In #1 scenario k = 4 (
        AAAA or BBBB), while in #2 scenario k = 3 (AAA or BBB or CCC).

        p is the number of how many tasks are the most occurred task. In
        #1 scenario p = 2 (AAAA, BBBB), while in #2 scenario p = 3
        (AAA, BBB, CCC).

        Note that the equation gives the correct answer directly for #1
        scenario, but not for #2 scenario. This is because in #2 scenario
        the empty slots have been used up, and all the remaining tasks are
        put into the buckets. The result for #2 scenario may greater than
        the result of the equation.

        So the final equation that works for both scenarios is:

        max(len(tasks), (k - 1) * (n + 1) + p)

    6. Code

        Following code not only give the correct answer, but with the task
        scheduling sequence.
    """
    task_counts = collections.Counter(tasks).most_common()
    k, p = task_counts[0][1], 0
    for task_count in task_counts:
        if task_count[1] == k:
            p += 1
    # With the actual task scheduling sequence.
    # 1. Group all the most occurred tasks and put all remaining tasks
    # together.
    most_occurred_tasks, remaining_tasks = '', ''
    for task_count in task_counts:
        if task_count[1] == k:
            most_occurred_tasks += task_count[0]
        else:
            remaining_tasks += task_count[0] * task_count[1]
    print('\n')
    print('task_counts: %s' % task_counts)
    print('most_occurred_tasks: %s' % most_occurred_tasks)
    print('remaining_tasks: %s' % remaining_tasks)
    # 2. Create the buckets for filling the remaining tasks. Each bucket
    # should have the minimum size of n + 1.
    buckets = []  # (# of the empty slots left, values)
    for _ in range(k - 1):
        empty_slots_count = max(0, n + 1 - len(most_occurred_tasks))
        buckets.append((empty_slots_count, most_occurred_tasks))
    print('buckets: %s' % buckets)
    # 3. Rolling the buckets and put the remaining tasks into the buckets.
    # For every task we put into the bucket, we reduce the bucket's
    # empty_slots_count by 1 until it reaches 0.
    index = 0
    while index < len(remaining_tasks):
        bucket_index = index % len(buckets)
        count, bucket_tasks = buckets[bucket_index]
        buckets[bucket_index] = (max(0, count - 1),
                                    bucket_tasks + remaining_tasks[index])
        index += 1
    # 4. Next convert the empty slot to `#` since there is no task
    # can be scheduled at that interval.
    for (i, (count, bucket_tasks)) in enumerate(buckets):
        buckets[i] = (0, bucket_tasks + '#' * count)
    # 5. Don't forget to add one more most_occurred_tasks since we use
    # k - 1 to create the buckets.
    buckets.append((0, most_occurred_tasks))
    print('final buckets: %s' % buckets)
    # 6. Finally print out the readable results.
    results = []
    for _, bucket_tasks in buckets:
        results.extend(list(bucket_tasks))
    results = [x.replace('#', 'idle') for x in results]
    print('final results: %s' % ' -> '.join(results))
    return max(len(tasks), (k - 1) * (n + 1) + p)

# print(leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))
# print((leastInterval(["A","A","A","B","B","B"],2)))
# print(leastInterval(["A","A","C","B","D"],2))
# print(leastInterval(["A","C","A","B","D","B"],1))

# print((leastInterval(["A","A","A","B","B","B"],3)))
# print((leastInterval(["A","A","A","B","B","B"],50)))
# print(leastInterval(["A","A","A","B","B","B","C","C","C", "D", "D", "E"],2))
# print((leastInterval(["A","A","A","B","B","B"],2)))
# print(leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"],7))
# print((leastInterval(["A","A","A","B","B","B"],2)))
# print(leastInterval(["A","A","C","B","D"],2))
# print(leastInterval(["A","C","A","B","D","B"],1))
# print(leastInterval(["A","A","A","B","B","B","C","C","C", "D", "D", "E"],2))
# print(leastInterval(["A","A","A"],1))    
# print(leastInterval(["A","A","A","B","B","B","C","C","C", "D", "D", "E"],2))
# print((leastInterval(["A","A","A","B","B","B"],2)))
# print(leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"],7))
# print(leastInterval(["A","A","C","B","D"],2))
# print(leastInterval(["A","C","A","B","D","B"],1))
# print((leastInterval(["A","A","A","B","B","B"],3)))
# print((leastInterval(["A","A","A","B","B","B"],50)))
# print(leastInterval(["G","C","A","H","A","G","G","F","G","J",],1))
# print(leastInterval(["C","E","E","G","G","H"],2))
# print(leastInterval(["A","B","C","D","E","A","B","C","D","E"],4))
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],1))

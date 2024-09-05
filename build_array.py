def buildArray(n, m, k):
    def search(elements, max_so_far, cost):
        counter = 0
        if elements == n:
            if cost == k:
                return 1
            else:
                return 0
        for x in range(1, m + 1):
            org_cost = cost
            if x > max_so_far:
                cost += 1
            counter += search(elements + 1, max(x, max_so_far), cost)
            cost = org_cost
        return counter

    return search(0, 0, 0)


print(buildArray(5, 2, 3))

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2

        # make lists of flights [(ratio, cost, person, city), ...]
        flights = []
        for i in range(len(costs)):
            flights.append( (costs[i][0] - costs[i][1], costs[i][0], i, 0) )
            flights.append( (costs[i][1] - costs[i][0], costs[i][1], i, 1) )

        # track people that have been seen
        seen = {}

        # track number of people in each city
        # city A and city B
        num = [0, 0]

        # sort city costs in decending order
        flights = list(reversed(sorted(flights)))
        print("flights:", flights)

        # the min cost
        total = 0

        # for each flight
        while len(flights) > 0:
            ratio, cost, person, city = flights.pop()
            print("cost, person, city:", cost, person, city)
            if person not in seen and num[city] < N:
                print("person:", person, "to city:", city)
                seen[person] = True
                num[city] += 1
                total += cost

        print("num:", num)
        return total

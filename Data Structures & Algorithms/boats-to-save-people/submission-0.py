class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        result = 0
        while i <= j:
            if people[j] + people[i] <= limit:
                result += 1
                i += 1
                j -= 1
            else:
                result += 1
                j -= 1
        return result
        
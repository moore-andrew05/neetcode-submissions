class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 1
        maxk = math.ceil((max(piles) / h)) * len(piles)
        
        l = mink
        r = maxk
        possibilities = []
        iter_limit = 100
        iter = 0

        while (r >= l) and (iter < iter_limit):
            iter += 1
            mid = l + ((r - l) // 2)
            sim_h = self.simulatePiles(piles, mid)

            if sim_h <= h:
                r = mid - 1
                possibilities.append(mid)
                continue

            l = mid + 1

        return min(possibilities)
    

    def simulatePiles(self, piles: List[int], k: int) -> int:
        h = 0
        piles = piles[:]
        for pile in piles:
            h += math.ceil(pile / k)
        
        return h
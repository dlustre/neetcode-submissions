class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] == 0:
                continue

            groups_to_start = count[card]

            for x in range(card, card + groupSize):
                if count[x] < groups_to_start:
                    return False

                count[x] -= groups_to_start

        return True
class Solution:
    # Time complexity: `O(n)` since we run through the input array once.
    # Space Complexity: `O(n)` since our solution can be the size of the input should nothing collide.
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroidsLeft = []
        for asteroid in asteroids:
            # if the stack is empty, append the current asteroid since there's nothing to crash into
            if not asteroidsLeft:
                asteroidsLeft.append(asteroid)
            else:
                # if they're in the same direction, add it to the array since they can't crash
                if asteroidsLeft[-1] > 0 and asteroid > 0:
                    asteroidsLeft.append(asteroid)
                else:
                    # collide the asteroids!
                    isDestroyed = False
                    while asteroidsLeft and (asteroidsLeft[-1] > 0 and asteroid < 0) and not isDestroyed:
                        if abs(asteroidsLeft[-1]) < abs(asteroid):
                            # asteroid in the stack breaks
                            asteroidsLeft.pop()
                        elif abs(asteroidsLeft[-1]) == abs(asteroid):
                            # both the asteroid in the stack and the current asteroid breaks
                            asteroidsLeft.pop()
                            isDestroyed = True
                        else:
                            # only the current asteroid breaks
                            isDestroyed = True
                    # if the current asteroid survives, add it to the array
                    if not isDestroyed:
                        asteroidsLeft.append(asteroid)
                
        return asteroidsLeft
                            
class LRUCache:

    class Node:
        def __init__(self, prev, next, kv: [int,int]):
            self.prev = prev
            self.next = next
            self.kv = kv

    def __init__(self, capacity: int):
        # two nodes
        # 2 -> 1
        # forward insert for put
        # trivial to just go through and look for the key wanted but this is O(n) time

        # I can just use a hash table to do O(1) lookup

        # key to Node(next, prev, value)

        # how does this handle key removal?
        self.lookup = {}
        self.currCap = 0
        self.capacity = capacity
        # temp fix this somehow will be the list
        self.head = None
        self.oldest = None

    def get(self, key: int) -> int:
        # if ur using a hash table this is really easy
        # you WOULD have to deal with removing the correct key though, or leaving it in, and setting it to -1 to show its no longer in the cache

        # what to do on cache hit for updation of LRU policy?
        # we can just use indices? 

        # DNE or removed
        if key not in self.lookup:
            return -1

        # do updation policy, return value

        # if its the oldest we need to update oldest since its going to the front

        # if its not the oldest it STILL goes to the front and we set the n.prev.next to n.next

        n = self.lookup[key]

        if n == self.head:
            return n.kv[1]
        
        # not the head, but the oldest
        if n == self.oldest:

            # update the oldest
            self.oldest = self.oldest.prev
            self.oldest.next = None

            # move the node to the front
            n.next = self.head
            n.prev = None
            self.head.prev = n
            self.head = n

            return n.kv[1]
        
        # not the oldest but still needs to bubble up (middle node)

        # pluck by setting the next and previous nodes to each other
        n.prev.next = n.next
        n.next.prev = n.prev

        # move the node to the front
        n.next = self.head
        n.prev = None
        self.head.prev = n
        self.head = n
        
        return n.kv[1]

    def put(self, key: int, value: int) -> None:
        # step 1: check lookup for key
        
        if key in self.lookup:
            n = self.lookup[key]
            n.kv[1] = value

            if n == self.head:
                return
            
            if n == self.oldest:
                self.oldest = self.oldest.prev
                self.oldest.next = None

                # bubble it up
                n.next = self.head
                n.prev = None
                self.head.prev = n
                self.head = n
                return

            # middle node case

            # pluck | rewire
            n.prev.next = n.next
            n.next.prev = n.prev

            # move the node to the front
            n.next = self.head
            n.prev = None
            self.head.prev = n
            self.head = n
            
            # else it is front of list already... at which point all we need to do is update the value already done

        else:
            n = self.Node(None, self.head, [key, value])
            self.lookup[key] = n
            
            # initial put
            if not self.oldest:
                self.oldest = n
                self.head = n
                self.currCap += 1
                return
            
            if self.currCap >= self.capacity:
                del self.lookup[self.oldest.kv[0]]

                # edge case at cap 1, cap will be full with head and oldest being the same
                if self.head == self.oldest:
                    self.head = n
                    self.oldest = n
                else:
                    # oldest node eviction
                    self.oldest = self.oldest.prev
                    self.oldest.next = None

                    # attach n to the front
                    self.head.prev = n
                    self.head = n
            else:
                self.head.prev = n
                self.head = n
                self.currCap += 1
                
        # not in cache?
            # place at front
                # insert in lookup
                # if there is a head, set head.prev to this new node
            # removal of LRU if past capacity
                # 'remove' the oldest from the lookup by setting to -1 | or just use remove but might be O(n) worst case 
                # new oldest is the oldest.prev
                # set new oldest.next to None

        # in cache?
            # find place in cache O(1) time -> check your lookup for the node
            # update the node
            # LRU updation

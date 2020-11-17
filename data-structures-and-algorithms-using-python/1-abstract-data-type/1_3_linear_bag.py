class Bag:
    """Implements the Bag ADT container using a Python list."""

    def __init__(self):
        """Constructs an empty bag."""
        self._items = list()

    def __len__(self):
        """Returns the number of items in the bag."""
        return len(self._items)

    def __contains__(self, item):
        """Determines if an item is contained in the bag."""
        return item in self._items

    def add(self, item):
        """Adds a new item to the bag."""
        self._items.append(item)

    def remove(self, item):
        """Removes and returns an instance of the item from the bag."""
        assert item in self._items, "The item must be in the bag."
        ndx = self._items.index(item)
        return self._items.pop(ndx)

    def __iter__(self):
        """Returns an iterator for traversing the list of items."""
        return BagIterator(self._items)


class BagIterator:
    """An iterator for the Bag ADT implemented as a Python list."""

    def __init__(self, items):
        self._bag_items = items
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item < len(self._bag_items):
            curr_item = self._bag_items[self._cur_item]
            self._cur_item += 1
            return curr_item
        else:
            raise StopIteration


if __name__ == "__main__":
    bag = Bag()
    bag.add(19)
    bag.add(74)
    bag.add(23)
    bag.add(19)
    bag.add(12)

    for item in bag:
        print(item)

    # Create a BagIterator object for myBag.
    iterator = bag.__iter__()
    # Repeat the while loop until break is called.
    while True:
        try:
            # Get the next item from the bag. If there are no
            # more items, the StopIteration exception is raised.
            cur_item = iterator.__next__()
            # Perform the body of the for loop.
            print(cur_item)
        except StopIteration:
            # Catch the exception and break from the loop when we are done.
            print("No item found...")
            break

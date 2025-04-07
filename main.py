WORDS = ["jumps", "laziest", "brown", "a",
         "quick", "fox", "the", "dog", "over"]

# Implement a custom version of max, called my_max
# Like the actual max, consider raising a ValueError if the collection is empty
# but feel free to assume you will always be given a non-empty collection.
# Otherwise, this function should behave the same as max when a key parameter is
# supplied. It should return the value from the collection which has the biggest
# comparison value as determined by calling the function passed in the key
# parameter on it. This will be very similar to the min_function_custom
# developed in the Learn reading.


def my_max(collection, key):
    if not collection:
        raise ValueError("cannot find max in empty list")

    # This approach works for list-like collections (collections that
    # support [] indexing and that we can ask the length of). This
    # would NOT work if we tried iterating over the keys in a
    # dictionary since we cannot use [] indexing on the keys,
    # values, or items iterators.

    # assume the first value in the list will be the max
    max_item = collection[0]
    max_value = key(max_item)

    # iterate through the remaining values
    for i in range(1, len(collection)):
        item = collection[i]
        current_value = key(item)

        # if the current value beats the best one, replace the best
        if current_value > max_value:
            max_value = current_value
            max_item = item

    return max_item

# An alternative approach (not called in the functions below, so
# rename this to my_max if you'd like to confirm that it works),
# that makes fewer assumptions about the collection of data being
# passed in (avoids [] indexing and asking for the length).


def my_max_iterable(iterable, key):
    if not iterable:
        raise ValueError("cannot find max in empty list")

    # this variation works for any iterable type, including lists,
    # tuples, any of the dict iterators, or sets, since the only thing
    # this code tries to do to the passed in data is iterate over it.

    # initialize the max to a value indicating we haven't picked it yet
    max_item = None
    max_value = None

    # iterate over the inputs
    for item in iterable:
        current_value = key(item)

        # if we haven't yet picked a max, or the current value beats
        # the best so far, replace the max
        if max_item is None or current_value > max_value:
            max_value = current_value
            max_item = item

    return max_item

# Implement a custom version of filter, called my_filter
# my_filter takes a function (should_keep) which it will call on every item in
# the supplied collection. If should_keep returns a truthy value for an item,
# then the item should be included in a new list containing only those filtered
# items, which should be returned
# WARNING: notice the parameters order is reversed compared to my_max


def my_filter(should_keep, collection):
    # if you've encountered list comprehensions, this would be a
    # great place to use one
    result = []
    for item in collection:
        if should_keep(item):
            result.append(item)

    # list comprehension approach
    # result = [item for item in collection if should_keep(item)]

    return result

# Implement a custom version of map, called my_map
# my_map takes a function (transform) which it will call on every item in the
# supplied collection. The result of calling transform on each item will be
# added to a new list in the same order as the original items. The new list
# should be returned.
# WARNING: notice the parameters order is reversed compared to my_max


def my_map(transform, collection):
    result = []
    for item in collection:
        transformed_item = transform(item)
        result.append(transformed_item)
    return result

# Implement a custom version of map, called my_map
# my_map takes a function (transform) which it will call on every item in the
# supplied collection. The result of calling transform on each item will be
# added to a new list in the same order as the original items. The new list
# should be returned.
# WARNING: notice the parameters order is reversed compared to my_max


def my_map(transform, collection):
    # if you've encountered list comprehensions, this would be a
    # great place to use one
    result = []
    for item in collection:
        transformed_item = transform(item)
        result.append(transformed_item)
    return result


#################################################
# NO CODE BELOW THIS POINT NEEDS TO BE MODIFIED #
# IMPLEMENT ONLY THE 3 FUNCTIONS ABOVE          #
#################################################

# These are the same functions as the live code session, but updated
# to call my_max rather than the built-in max.

# find the word that is alphabetically "highest" (comes last alphabetically)
def get_last_word_alphabetically(words):
    # Notice that we still need to provide a key function to get
    # the default behavior that max usuauly has. To mimic the behavior
    # of the max function more closely, try researching python
    # default arguments
    last_word = my_max(words, key=lambda word: word)
    return last_word

# find the longest word


def get_longest_word(words):
    # For any of these keyword arguments, we could leave off the name
    # since we did NOT define our versions to force certain parameters
    # to be passed positionally, and others by name.
    longest_word = my_max(words, key=len)
    return longest_word

# find the shortest word (still using max)
# this is a little sneaky!


def get_shortest_word(words):
    # here, we left off the name to show it works positionally as well
    # we'll just use positional params for the remaining helpers
    shortest_word = my_max(words, lambda word: -len(word))
    return shortest_word

# a helper method used to test out the behavior of my_filter


def get_short_words(words):
    # get the words whose length is 3 or less
    short_words = my_filter(lambda word: len(word) <= 3, words)

    # but in python, we are more likely to do something like
    # this, using list comprehension syntax
    # short_words = [word for word in words if len(word) <= 3]

    return short_words

# a helper method used to test out the behavior of my_map


def get_word_lengths(words):
    # transform each word into its length
    lengths = my_map(lambda word: len(word), words)

    # but in python, we are more likely to do something like
    # this, using list comprehension syntax
    # lengths = [len(word) for word in words]

    return lengths


# print("Actual word lengths:", get_word_lengths(WORDS))
# print("Expected word lengths:", [5, 7, 5, 1, 5, 3, 3, 3, 4])


def main():
    # test behavior of my_max (through using the helpers)
    assert get_last_word_alphabetically(WORDS) == "the"
    print("get_last_word_alphabetically PASSED!")
    assert get_longest_word(WORDS) == "laziest"
    print("get_longest_word PASSED!")
    assert get_shortest_word(WORDS) == "a"
    print("get_shortest_word PASSED!")

    # test behavior of my_filter (through using a helper)
    assert get_short_words(WORDS) == ["a", "fox", "the", "dog"]
    print("get_short_words PASSED!")

    # test behavior of my_map (through using a helper)
    assert get_word_lengths(WORDS) == [5, 7, 5, 1, 5, 3, 3, 3, 4]
    print("get_word_lengths PASSED!")

    print("All tests PASSED!")


if __name__ == "__main__":
    main()

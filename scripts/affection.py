# Gakuen Necro Early Development

# class Affection:
    # """A collection of scripts for dealing with boys and their affection for
    # you. <3"""
def calculate(attributes):
    """Calculate attribute change, save, and return change value.

    Specifically this recieves a comma-separated list of attributes,
    with any applicable modifiers, iterates through that list and
    builds a dictionary containing attribute:value pairs.
    That dictionary is then evaluated to return the affection value
    changes to the user and add + store the new affection values in
    a persistent variable.

    """
    # Create the attr list.
    attr = []

    # Iterate through all items that have been passed to the fucntion.
    for a in attributes:
        # If the attribute includes a :--that is, it has a modifier--then we
        # need to do some special stuff with it.
        if ':' in a:
            # Split at colon, then convert to tuple.
            a = tuple(a.split(':'))
            # Convert the second item from a string to an integer.
            # If we don't things will get ugly.
            a = a[0],int(a[1])
            # At this point, 'a' should be a tuple in the form of
            # ('attribute',n).
        else:
            # If the attribute doesn't have a modifier, then a a "modifier"
            # of 1.
            a = a,1
            # At this point, 'a' should be a tuple in the form of
            # ('attribute',n).
        # Append the 'a' tuple to the list 'attr'.
        attr.append(a)
    return attr

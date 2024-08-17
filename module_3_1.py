calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string=''):
    t = {len(string), string.upper(), string.lower()}
    count_calls()
    return (t)


def is_contains(string='', list_to_search=[]):
    res = False
    for i in range(len(list_to_search)):
        if list_to_search[i] in string.lower():
            res = True
            break

    count_calls()
    return (res)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

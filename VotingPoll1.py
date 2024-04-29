def vote_menu():
    john_votes = 0
    print('-' * 35)
    print('VOTE MENU')
    print('-' * 35)
    print('v: Vote')
    print('x: Exit')
    option = input('Option: ').strip().lower()
    while option != 'v' and option != 'x':
        option = input('Invalid(v/x): ').strip().lower()

    return option


def candidate_menu():
    print('-' * 35)
    print('CANDIDATE MENU')
    print('-' * 35)
    print('1: John')
    print('2: Jane')
    candidate = int(input('Candidate: '))
    while True:
        if candidate == 1 or candidate == 2:
            break
        candidate = int(input('Invalid(1/2): '))
    if candidate == 1:
        print('Voted John')
    elif candidate == 2:
        print('Voted Jane')
    return candidate


def main():
    john_votes = 0
    jane_votes = 0

    while True:
        ans = vote_menu()
        if ans == 'x':
            break
        else:
            candidate = candidate_menu()
            if candidate == 1:
                john_votes += 1
            elif candidate == 2:
                jane_votes += 1

    print('-' * 35)
    print(f'John - {john_votes}, Jane - {jane_votes}, Total - {john_votes + jane_votes}')
    print('-' * 35)


main()

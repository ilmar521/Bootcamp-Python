import datetime


def get_age(year, month, day):
    dt_now = datetime.datetime.now()
    date_birth = datetime.datetime(year, month, day)
    delta = dt_now - date_birth
    return delta.days // 365


def can_retire(gender, date_of_birth):
    answer = {
        'error': False,
        'can_retire': False
    }
    try:
        year, month, day = map(int, date_of_birth.split('/'))
    except:
        answer['error'] = True
        return answer
    age = get_age(year, month, day)
    if gender == 'm':
        answer['can_retire'] = age >= 67
    else:
        answer['can_retire'] = age >= 62

    return answer


def main():
    date_of_birth = input('Enter a date of birth in yyyy/mm/dd format: ')
    gender = input('Input your gender in m/f format: ')
    answer = can_retire(gender, date_of_birth)
    if not answer['error']:
        if answer['can_retire']:
            print('You are retired person')
        else:
            print('You are not retired person yet')
    else:
        print('You enter invalid date of birth!')


main()

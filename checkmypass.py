import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},Check thi api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(passwords):
    sha1password = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(passwords):
    # for passwords in args:
        count = pwned_api_check(passwords)
        if count:
            return (f'Be Careful! "{passwords}" was goten haked before {count} times!!!\n You should change it now.')
        else:
            return (f'😃Congragulations "{passwords}" was not found before.\n you can keep your password.')
        return


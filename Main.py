from utils.io import read_data, write_data


def main():
    info, data = read_data('hash_code/exampledata')
    print(data)
    write_data(data, 'hash_code/out')


if __name__ == '__main__':
    main()


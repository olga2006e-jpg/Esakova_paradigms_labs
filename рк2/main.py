import requests

def main():
    print("Задача A1:")
    for item in requests.get_A1():
        print(item)
    print("\nЗадача A2:")
    for item in requests.get_A2():
        print(item)
    print("\nЗадача A3:")
    for key, value in requests.get_A3().items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
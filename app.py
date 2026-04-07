from utils import *

def main():
    data = input("Enter data: ")
    hash_value = generate_hash(data)

    if is_duplicate(hash_value):
        print("❌ Duplicate data detected.")
    else:
        store_data(hash_value, data)
        print("✅ Stored in AWS!")

if __name__ == "__main__":
    main()
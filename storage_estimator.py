# My Python file for Lab 7
# Storage Estimator
# Estimates how much storage a number of files will need.

def main():
    print("=== Storage Estimator ===")

    num_files = int(input("How many files? "))
    size_mb = float(input("Average size of each file in MB? "))

    total_mb = num_files * size_mb
    total_kb = total_mb * 1024
    total_gb = total_mb / 1024

    print("Total storage needed:")
    print(f"  {total_kb:.2f} KB")
    print(f"  {total_mb:.2f} MB")
    print(f"  {total_gb:.4f} GB")


if __name__ == "__main__":
    main()

import sys

print("=== Comand Quest ===")
print(f"Program name: {sys.argv[0]}")
print(f"Arguments recived: {len(sys.argv) - 1}")
for idx in range(len(sys.argv) - 1):
    print(f"Argument {idx + 1}: {sys.argv[idx + 1]}")
print(f"Total arguments: {len(sys.argv)}\n")

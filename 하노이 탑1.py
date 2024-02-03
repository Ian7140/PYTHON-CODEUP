def hanoi_tower(n, source, auxiliary, target):
    if n == 1:
        print(f"Disk 1 : {source} to {target}")
        return
    hanoi_tower(n - 1, source, target, auxiliary)
    print(f"Disk {n} : {source} to {target}")
    hanoi_tower(n - 1, auxiliary, source, target)

def main():
    n = int(input())
    hanoi_tower(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()

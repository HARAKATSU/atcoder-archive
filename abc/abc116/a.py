def main():
    ab, bc, ca = list(map(int, input().split(' ')))
    
    print(int((ab * bc) / 2))

if __name__ == '__main__':
    main()
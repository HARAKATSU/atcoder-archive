def main():
    s = input().strip()
    t = input().strip()
    cnt = 0
    
    for i in range(3):
        if s[i] == t[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
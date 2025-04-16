def quick_merge(count):
    final_list = []
    for i in range(count):
        i = input().split()
        mid_list = []
        for j in i:
            mid_list.append(int(j))
        final_list.extend(mid_list)
        final_list.sort()
        list_str = [str(k) for k in final_list]
    return " ".join(list_str)


n = int(input())
print(quick_merge(n))

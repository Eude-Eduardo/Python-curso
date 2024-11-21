def soma(* num):
    for p ,i in enumerate(num):
        print(f"{i} ", end="+ " if p < len(num)-1 else "= ")
    print(sum(num))

soma(1, 2, 3)
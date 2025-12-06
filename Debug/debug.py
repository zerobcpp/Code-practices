def debug(*args, **kwargs):
    print("args:", args, end = '\t')
    
    for i, v in kwargs.items():
        print(f"{i}: {v}", end = '\t')
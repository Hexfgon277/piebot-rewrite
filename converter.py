def time_converter(x: int):
    base = []
    if x >= 3600:
        base.append(f"{round(x // 3600)}시간")
    if x >= 60 and x % 3600 != 0:
        base.append(f"{round(x % 3600 // 60)}분")
    if x % 60 != 0:
        base.append(f"{x % 60}초")
    text = ' '.join(base)
    return text

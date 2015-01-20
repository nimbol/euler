def len_recurring(n):
    mod = 1
#    results = []
    mods = []
    while True:
        div, mod = divmod(mod, n)
#        results.append(str(div))
        if mod != 0 and mod not in mods:
            mods.append(mod)
            mod *= 10
        else:
            break
    if mod == 0:
        return 0
    return len(mods) - mods.index(mod)
#    r = len(mods) - mods.index(mod)
#    return results[0] +'.'+ results[1:mods.index(mod)] +'('+ results[mods.index(mod):] +')'

print max((len_recurring(n), n) for n in range(1, 1001))[1]
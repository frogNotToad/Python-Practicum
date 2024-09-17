(lambda x, y, z: print("YES") if x < y + z and y < x + z and z < x + y else print("NO"))(int(input()),
                                                                                         int(input()), int(input()))

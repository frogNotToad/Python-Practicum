print(['Петя', 'Вася', 'Толя'][(lambda x, y, z: [x, y, z].index(max(x,
                                                                    y, z)))(int(input()), int(input()), int(input()))])

[print(f'{x[0]}. {x[1]}') for x in zip([1, 2, 3], sorted(['Петя', 'Вася', 'Толя'], key=lambda _: -int(input())))]

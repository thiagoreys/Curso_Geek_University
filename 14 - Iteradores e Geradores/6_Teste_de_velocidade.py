from time import time

# Generator Expression
inicio_gen = time()
print(sum(num for num in range(100000000)))  # 100 milhões
tempo_gen = time() - inicio_gen

# List Comprehension
inicio_list = time()
print(sum([num for num in range(100000000)]))  # 100 milhões
tempo_list = time() - inicio_list

print(f'Generator Expression demorou {tempo_gen} segundos.')
print(f'List Comprehension demorou {tempo_list} segundos.')
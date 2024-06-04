import numpy as np

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None
 
    while low <= high:
        iterations += 1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_bound = arr[mid]
            break
 
    # # якщо елемент не знайдений
    # return -1

    if upper_bound is None:
        upper_bound = arr[-1]

    return iterations, upper_bound


random_arr = np.random.uniform(low=0, high=10, size=(10))
arr = sorted(random_arr)
x = 9.9
iterations, upper_bound = binary_search(arr, x)
print(arr)
print(f"Кількість ітерацій: {iterations}, Верхня межа: {upper_bound}")

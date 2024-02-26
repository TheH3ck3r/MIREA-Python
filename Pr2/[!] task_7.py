import matplotlib.pyplot as plt

def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()

    # Построение гистограммы с подписями.
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    # для тех, кто работает в средах, отличных от jupyter-подобных - раскомментировать строку ниже
    # plt.show()
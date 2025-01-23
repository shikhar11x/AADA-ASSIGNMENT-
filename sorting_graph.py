import matplotlib.pyplot as plt 

input_sizes = [10, 20, 30, 40, 50]

# Data for Insertion Sort
insertion_sort_sorted = [155, 610, 1365, 2420, 3775]
insertion_sort_rev_sorted = [290, 1180, 2670, 4760, 7450]
insertion_sort_random = [176, 895, 2028, 3617, 5713]
# Data for Selection Sort
selection_sort_sorted = [198, 703, 1508, 2613, 4018]
selection_sort_rev_sorted = [213, 733, 1553, 2673, 4093]
selection_sort_random = [231, 780, 1644, 2776, 4246]
# Data for Bubble Sort
bubble_sort_sorted = [30, 60, 90, 120, 150]
bubble_sort_rev_sorted = [351, 1406, 3161, 5616, 8771]
bubble_sort_random = [253, 870, 2250, 3816, 5258]
plt.figure(figsize=(18, 12))

# Graph 1: Insertion Sort
plt.subplot(3, 1, 1)
plt.plot(input_sizes, insertion_sort_sorted, label="Sorted Case(Best)", marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(input_sizes, insertion_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
plt.plot(input_sizes, insertion_sort_rev_sorted, label="Reverse Sorted Case(Worst)", marker='^', linestyle='-.', color='red', linewidth=2)
plt.title("Graph 1: Insertion Sort (Ascending)", fontsize=14)
plt.xlabel("Input Size", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.text(input_sizes[-2], insertion_sort_sorted[-2] + 0.22 * insertion_sort_sorted[-2], 'O(n)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[-2], insertion_sort_random[-2] + 0.22 * insertion_sort_random[-2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[-2], insertion_sort_rev_sorted[-2] + 0.22 * insertion_sort_rev_sorted[-2], 'O(n^2)', fontsize=10, color='red', ha='left')
plt.legend()
plt.grid(True)

# Graph 2: Selection Sort
plt.subplot(3, 1, 2)
plt.plot(input_sizes, selection_sort_sorted, label="Sorted Case(Best)", marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(input_sizes, selection_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
plt.plot(input_sizes, selection_sort_rev_sorted, label="Reverse Sorted Case(Worst)", marker='^', linestyle='-.', color='red', linewidth=2)
plt.title("Graph 2: Selection Sort (Ascending)", fontsize=14)
plt.xlabel("Input Size", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.text(input_sizes[-2], selection_sort_sorted[-2] + 0.24 * selection_sort_sorted[-2], 'O(n^2)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[-2], selection_sort_random[-2] + 0.24 * selection_sort_random[-2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[-2], selection_sort_rev_sorted[-2] + 0.24 * selection_sort_rev_sorted[-2], 'O(n^2)', fontsize=10, color='red', ha='left')
plt.legend()
plt.grid(True)

# Graph 3: Bubble Sort
plt.subplot(3, 1, 3)
ax1 = plt.gca()
ax1.plot(input_sizes, bubble_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
ax1.plot(input_sizes, bubble_sort_rev_sorted, label="Reverse Sorted Case(Worst)", marker='^', linestyle='-.', color='red', linewidth=2)
ax1.set_xlabel("Input Size", fontsize=12)
ax1.set_ylabel("Steps (Average/Worst)", fontsize=12)
ax1.set_yscale('log')
ax1.legend(loc='upper left')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(input_sizes, bubble_sort_sorted, label="Sorted Case(Best)", marker='o', linestyle='-', color='blue', linewidth=2)
ax2.set_ylabel("Steps (Best)", fontsize=12)
ax2.set_ylim(0, 300)
ax2.legend(loc='upper right')

plt.title("Graph 3: Bubble Sort (Ascending)", fontsize=14)
plt.text(input_sizes[-2], bubble_sort_sorted[-2] + 0.12 * bubble_sort_sorted[-2], 'O(n)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[2], bubble_sort_random[2] - 0.94 * bubble_sort_random[2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[2], bubble_sort_rev_sorted[2] - 0.93 * bubble_sort_rev_sorted[2], 'O(n^2)', fontsize=10, color='red', ha='left')

plt.subplots_adjust(hspace=0.5)
plt.show(block=False)


# Descending Order Data
# Selection Sort
selection_sort_sorted = [213, 733, 1553, 2673, 4093]
selection_sort_rev_sorted = [198, 703, 1508, 2613, 4018]
selection_sort_random = [213, 751, 1589, 2715, 4153]

# Bubble Sort
bubble_sort_sorted = [351, 1406, 3161, 5616, 8771]
bubble_sort_rev_sorted = [30, 60, 90, 120, 150]
bubble_sort_random = [241, 923, 1885, 4042, 6225]

# Insertion Sort
insertion_sort_sorted = [290, 1180, 2670, 4760, 7450]
insertion_sort_rev_sorted = [155, 610, 1365, 2420, 3775]
insertion_sort_random = [224, 913, 2112, 3599, 5581]

# Create the second figure for Descending Order
plt.figure(figsize=(18, 12))

# Descending Graphs
# Graph 1: Insertion Sort
plt.subplot(3, 1, 1)
plt.plot(input_sizes, insertion_sort_sorted, label="Sorted Case(Worst)", marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(input_sizes, insertion_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
plt.plot(input_sizes, insertion_sort_rev_sorted, label="Reverse Sorted Case(Best)", marker='^', linestyle='-.', color='red', linewidth=2)
plt.title("Graph 1: Insertion Sort (Descending)", fontsize=14)
plt.xlabel("Input Size", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.text(input_sizes[-2], insertion_sort_sorted[-2] + 0.22 * insertion_sort_sorted[-2], 'O(n^2)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[-2], insertion_sort_random[-2] + 0.22 * insertion_sort_random[-2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[-2], insertion_sort_rev_sorted[-2] + 0.22 * insertion_sort_rev_sorted[-2], 'O(n)', fontsize=10, color='red', ha='left')
plt.legend()
plt.grid(True)

# Graph 2: Selection Sort
plt.subplot(3, 1, 2)
plt.plot(input_sizes, selection_sort_sorted, label="Sorted Case(Worst)", marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(input_sizes, selection_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
plt.plot(input_sizes, selection_sort_rev_sorted, label="Reverse Sorted Case(Best)", marker='^', linestyle='-.', color='red', linewidth=2)
plt.title("Graph 2: Selection Sort (Descending)", fontsize=14)
plt.xlabel("Input Size", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.text(input_sizes[-2], selection_sort_sorted[-2] + 0.24 * selection_sort_sorted[-2], 'O(n^2)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[-2], selection_sort_random[-2] + 0.24 * selection_sort_random[-2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[-2], selection_sort_rev_sorted[-2] + 0.24 * selection_sort_rev_sorted[-2], 'O(n^2)', fontsize=10, color='red', ha='left')
plt.legend()
plt.grid(True)

# Graph 3: Bubble Sort
plt.subplot(3, 1, 3)
ax1 = plt.gca()
ax1.plot(input_sizes, bubble_sort_random, label="Random Case(Average)", marker='s', linestyle='--', color='green', linewidth=2)
ax1.plot(input_sizes, bubble_sort_sorted, label="Sorted Case(Worst)", marker='o', linestyle='-', color='blue', linewidth=2)
ax1.set_xlabel("Input Size", fontsize=12)
ax1.set_ylabel("Steps (Average/Worst)", fontsize=12)
ax1.set_yscale('log')
ax1.legend(loc='upper left')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(input_sizes, bubble_sort_rev_sorted, label="Reverse Sorted Case(Best)", marker='^', linestyle='-.', color='red', linewidth=2)
ax2.set_ylabel("Steps (Best)", fontsize=12)
ax2.set_ylim(0, 300)
ax2.legend(loc='upper right')

plt.title("Graph 3: Bubble Sort (Descending)", fontsize=14)
plt.text(input_sizes[2], bubble_sort_sorted[2] - 0.93 * bubble_sort_sorted[2], 'O(n^2)', fontsize=10, color='blue', ha='left')
plt.text(input_sizes[2], bubble_sort_random[2] - 0.93 * bubble_sort_random[2], 'O(n^2)', fontsize=10, color='green', ha='left')
plt.text(input_sizes[-2], bubble_sort_rev_sorted[-2] + 0.12 * bubble_sort_rev_sorted[2], 'O(n)', fontsize=10, color='red', ha='left')

plt.subplots_adjust(hspace=0.5)
plt.show()


def amdahls_law(parallelizable_fraction, num_processors):
    """
    Calculate the speedup of a program based on Amdahl's Law.
    
    :param parallelizable_fraction: The fraction of the program that can be parallelized (between 0 and 1).
    :param num_processors: The number of processors available.
    :return: The speedup factor.
    """
    # The fraction of the program that is sequential (cannot be parallelized)
    sequential_fraction = 1 - parallelizable_fraction
    
    # Amdahl's Law formula
    speedup = 1 / (sequential_fraction + (parallelizable_fraction / num_processors))
    
    return speedup

# Example parameters
parallelizable_fraction = 0.60  # 60% of the program can be parallelized
processor_counts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]  # Various numbers of processors

# Calculate speedup for different numbers of processors
print(f"Parallelizable Fraction: {parallelizable_fraction * 100}%\n")
print(f"{'Processors':<15}{'Speedup':<10}{'Execution Time (100s Program)':<30}")
print("="*50)
for processors in processor_counts:
    speedup = amdahls_law(parallelizable_fraction, processors)
    execution_time = 100 / speedup  # Assuming the original execution time is 100 seconds
    print(f"{processors:<15}{speedup:<10.4f}{execution_time:<30.4f} seconds")

# Theoretical maximum speedup with infinite processors
theoretical_max_speedup = amdahls_law(parallelizable_fraction, float('inf'))
print(f"\nTheoretical Maximum Speedup: {theoretical_max_speedup:.4f}")

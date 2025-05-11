
def calculate_power_four_sum(nums, expected_count):
    """Calculate sum of power of four of integers, excluding positives."""
    if len(nums) != expected_count:
        return -1
    
    # Define recursive helper function
    def sum_power_four_negatives(numbers, index=0):
        if index >= len(numbers):
            return 0
        
        num = numbers[index]
        
        power_four = num**4 if num < 0 else 0
        
        return power_four + sum_power_four_negatives(numbers, index + 1)
    
    return sum_power_four_negatives(nums)

def process_test_cases(n):
    """Process n test cases."""
    if n <= 0:
        return []
    
    x = int(input())
    
    nums = list(map(int, input().split()))
    
    result = calculate_power_four_sum(nums, x)
    
    # Process remaining test cases recursively
    return [result] + process_test_cases(n - 1)

def main():
    n = int(input())
    
    results = process_test_cases(n)
    
    print_results(results)

def print_results(results, index=0):
    """Print results recursively."""
    if index >= len(results):
        return
    
    print(results[index])
    print_results(results, index + 1)

if __name__ == "__main__":
    main() 
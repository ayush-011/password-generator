numbers = []  # Empty list to store numbers

# Infinite loop to take user input
while True:
    value = input("Enter a number (or type 'stop' to finish): ")

    if value.lower() == "stop":  # If user types "stop", break the loop
        break

    try:
        numbers.append(int(value))  # Convert to integer and store
    except ValueError:
        print("❌ Please enter a valid number!")

# Check if the list is empty before processing
if numbers:
    largest = numbers[0]  # Assume first number is the largest
    smallest = numbers[0]  # Assume first number is the smallest

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    total = sum(numbers)  # Sum of all numbers
    average = total / len(numbers)  # Average calculation

    # Find even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Remove duplicates and sort
    unique_sorted_numbers = sorted(set(numbers))

    # Check if we have at least two unique numbers for second largest & second smallest
    if len(unique_sorted_numbers) > 1:
        second_smallest = unique_sorted_numbers[1]  # Second smallest number
        second_largest = unique_sorted_numbers[-2]  # Second largest number
    else:
        second_smallest = "N/A (Not enough unique numbers)"
        second_largest = "N/A (Not enough unique numbers)"

    # Results
    print("\n📊 Results:")
    print(f"✅ Largest number: {largest}")
    print(f"✅ Second Largest number: {second_largest}")
    print(f"✅ Smallest number: {smallest}")
    print(f"✅ Second Smallest number: {second_smallest}")
    print(f"🧮 Sum of numbers: {total}")
    print(f"📊 Average of numbers: {average:.2f}")  # Rounding average to 2 decimal places

    print("\n🔢 Even numbers:", even_numbers, f"(Count: {len(even_numbers)})")
    print("🔴 Odd numbers:", odd_numbers, f"(Count: {len(odd_numbers)})")

else:
    print("⚠ No numbers were entered.")

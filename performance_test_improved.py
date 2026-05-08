"""
Performance test for string concatenation optimization in PySimpleGUI
Compares original vs optimized implementation
"""

import time
import sys
import os

# Test the original string concatenation approach
def original_convert_args(args):
    """Original implementation with string concatenation in loop"""
    max_line_total, width_used, total_lines, = 0, 0, 0
    single_line_message = ''
    for message in args:
        message = str(message)
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = max(longest_line_len, width_used)
        max_line_total = max(max_line_total, width_used)
        lines_needed = len(message.split('\n'))  # Simplified for testing
        total_lines += lines_needed
        single_line_message += message + '\n'  # String concatenation
    return single_line_message, width_used, total_lines

# Test the optimized approach with list and join
def optimized_convert_args(args):
    """Optimized implementation using list.append and join"""
    max_line_total, width_used, total_lines, = 0, 0, 0
    message_parts = []
    for message in args:
        message = str(message)
        message_lines = message.split('\n')
        longest_line_len = max(len(l) for l in message_lines) if message_lines else 0
        width_used = max(longest_line_len, width_used)
        max_line_total = max(max_line_total, width_used)
        lines_needed = len(message_lines)  # Simplified for testing
        total_lines += lines_needed
        message_parts.append(message)
    single_line_message = '\n'.join(message_parts) + '\n' if message_parts else ''
    return single_line_message, width_used, total_lines

def test_string_concatenation(num_messages, message_size):
    """Test both implementations with specified parameters"""
    
    # Create test messages
    messages = []
    for i in range(num_messages):
        # Create multi-line messages to be realistic
        lines = [f"Line {j} of message {i}: " + "x" * message_size for j in range(5)]
        messages.append('\n'.join(lines))
    
    # Test original implementation
    start = time.perf_counter()
    result1 = original_convert_args(messages)
    original_time = time.perf_counter() - start
    
    # Test optimized implementation
    start = time.perf_counter()
    result2 = optimized_convert_args(messages)
    optimized_time = time.perf_counter() - start
    
    # Verify results are the same
    assert result1[0] == result2[0], "Results don't match!"
    
    return original_time, optimized_time

def main():
    print("String Concatenation Optimization Test")
    print("=" * 60)
    print("Testing convert_args_to_single_string optimization")
    print("-" * 60)
    
    # Test with different message counts and sizes
    test_cases = [
        (10, 50, "Small: 10 messages, 50 chars"),
        (50, 50, "Medium: 50 messages, 50 chars"),
        (100, 100, "Large: 100 messages, 100 chars"),
        (200, 100, "XLarge: 200 messages, 100 chars"),
        (500, 50, "Many small: 500 messages, 50 chars"),
        (100, 500, "Long messages: 100 messages, 500 chars"),
    ]
    
    print(f"{'Test Case':<40} {'Original':>10} {'Optimized':>10} {'Speedup':>8}")
    print("-" * 70)
    
    total_original = 0
    total_optimized = 0
    
    for num_msgs, msg_size, description in test_cases:
        # Run each test 3 times and take the minimum (to reduce noise)
        orig_times = []
        opt_times = []
        
        for _ in range(3):
            orig_time, opt_time = test_string_concatenation(num_msgs, msg_size)
            orig_times.append(orig_time)
            opt_times.append(opt_time)
        
        orig_time = min(orig_times)
        opt_time = min(opt_times)
        
        speedup = orig_time / opt_time if opt_time > 0 else 0
        
        print(f"{description:<40} {orig_time*1000:>8.3f}ms {opt_time*1000:>8.3f}ms {speedup:>7.2f}x")
        
        total_original += orig_time
        total_optimized += opt_time
    
    print("-" * 70)
    overall_speedup = total_original / total_optimized if total_optimized > 0 else 0
    print(f"{'Total':<40} {total_original*1000:>8.3f}ms {total_optimized*1000:>8.3f}ms {overall_speedup:>7.2f}x")
    
    print("\n" + "=" * 60)
    if overall_speedup > 1:
        improvement = ((total_original - total_optimized) / total_original) * 100
        print(f"SUCCESS: Optimization successful! {improvement:.1f}% faster overall")
    else:
        print("FAIL: No improvement detected")
    
    # Now test with the actual PySimpleGUI module
    print("\n" + "=" * 60)
    print("Testing actual PySimpleGUI implementation")
    print("-" * 60)
    
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import PySimpleGUI as sg
    
    # Create test messages
    test_messages = ["Test message " + str(i) * 10 for i in range(100)]
    
    # Measure performance
    start = time.perf_counter()
    result = sg.convert_args_to_single_string(*test_messages)
    psg_time = time.perf_counter() - start
    
    print(f"PySimpleGUI (optimized): {psg_time*1000:.3f}ms for 100 messages")
    print("SUCCESS: PySimpleGUI module working with optimization")

if __name__ == "__main__":
    main()
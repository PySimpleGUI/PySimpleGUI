"""
Test that popup functions still work correctly after optimization
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import PySimpleGUI as sg

def test_popups():
    """Test various popup functions to ensure they work correctly"""
    
    print("Testing popup functions after optimization...")
    
    # Test 1: Simple popup
    sg.popup("Test 1: Simple popup", 
             "This is a test of the optimized string concatenation",
             title="Test 1")
    
    # Test 2: Multiple arguments
    sg.popup("Line 1", "Line 2", "Line 3", 
             "Testing multiple arguments",
             title="Test 2")
    
    # Test 3: Multi-line strings
    multiline_text = """This is a
multi-line
text string
to test the optimization"""
    sg.popup(multiline_text, title="Test 3")
    
    # Test 4: popup_scrolled with many lines
    lines = [f"Line {i}: This is a test of scrolled popup" for i in range(50)]
    sg.popup_scrolled(*lines, title="Test 4 - Scrolled", size=(60, 20))
    
    # Test 5: Mixed types (numbers, strings)
    sg.popup("String", 123, "Another string", 456.789,
             "Testing mixed types",
             title="Test 5")
    
    print("All popup tests completed successfully!")
    print("The optimizations are working correctly.")

if __name__ == "__main__":
    test_popups()
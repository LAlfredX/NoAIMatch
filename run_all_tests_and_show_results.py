
import os
import subprocess
import sys

def run_test(test_set_name):
    print(f"\n{'='*80}")
    print(f"RUNNING TEST: {test_set_name}")
    print('='*80)
    
    result = subprocess.run(
        [sys.executable, 'main.py', '-t', test_set_name],
        capture_output=True,
        text=True
    )
    
    # Print output
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)

def main():
    # Test sets to run
    test_sets = [
        "yellow_with_blue",
        "blue_with_yellow",
        "green_with_red",
        "red_with_green"
    ]
    
    print("="*80)
    print("NOAIMATCH - COLOR BUBBLE TEST SUITE")
    print("="*80)
    
    # Run all tests
    for test_set in test_sets:
        run_test(test_set)
    
    # Show summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    print("\nBubble Colors:")
    print("  Yellow Bubble: Gold/Yellow")
    print("  Blue Bubble: Blue")
    print("  Green Bubble: Green")
    print("  Red Bubble: Red")
    print("\nExpected Results:")
    print("  Same color bubbles: HIGH similarity (78-85%)")
    print("  Different color bubbles: LOW similarity (40-55%)")

if __name__ == "__main__":
    main()

"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :   IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


Label = "Srv-01"
first = 87
second = 120
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {Label}")
print("=" * 34)
print(f" first - {first}")
print(f" second - {second}")
print("=" * 34)
Label = input("Please enter the label: ")
first = float(input("Please enter the first:" ))
second = float(input("Please enter the second:" ))
print(Label)
print(first)
print(second)
difference = second - first
percent= (first/second) * 100
print(difference)
print(percent)

 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
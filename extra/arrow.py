print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Original arrow lines
row1  = "    *"
row2  = "   * *"
row3  = "  *   *"
row4  = " *     *"
row5  = "***   ***"
row6  = "  *   *"
row7  = "  *   *"
row8  = "  *****"

# 1. Minimize prints with \n
print(row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" +
      row5 + "\n" + row6 + "\n" + row7 + "\n" + row8)

# 2. Double size arrow
print("        *\n       * *\n      *   *\n     *     *\n    *       *\n   *         *\n******     ******\n      *   *\n      *   *\n      *   *\n      *   *\n      *********")

# 3. Two arrows side by side (correctly spaced with gap)
lines = [row1, row2, row3, row4, row5, row6, row7, row8]
for line in lines:
    print(line + "   " + line)

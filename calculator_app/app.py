from classes.calc_class import Calculator

def main():
  power_on = True
  print("This is a Calculator")

  while power_on == True:
    num1 = int(input("First number: "))
    op = input("Operation [+-*/]: ")
    num2 = int(input("Second number: "))

    c = Calculator(num1, op, num2)
    result = c.calculation()
  
    print(f"Equals: {result}")

    again = input("Calculate again? [y/n]: ")
    again.lower()

    if again == "n":
      power_on = False
      print("Ok, bye.")
    else:
      pass
      
if __name__ == "__main__":
    main()
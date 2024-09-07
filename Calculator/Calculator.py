class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def division(self,a,b):
        if b == 0:
            return f'{a} can not be divided by zero'
        return a//b

def main():
    obj = Calculator()       
    operator_mapping = {
        '+': obj.add,
        '-': obj.sub,
        '*':obj.multiply,
        '/':obj.division
    }
    expression = input("Please Enter the two numbers with seprated operators\n")
    
   

    try:
        a,operator,b = expression.split(" ")
        a = int(a)
        b = int(b)
        if(operator in operator_mapping.keys()):
            ans = operator_mapping[operator](a,b)
            print(f'Result: {ans}')
        else:
            print("Invliad Operator")
    except Exception as E:
        print(f"An error : {E}")



if __name__ == "__main__":
    main()


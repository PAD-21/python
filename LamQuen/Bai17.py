def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def evaluate_expression(a, b, c, x):
    return a*x**2 + b*x + c

# Nhập hệ số A, B, C và giá trị N từ bàn phím
A = int(input("Nhập giá trị hệ số A: "))
B = int(input("Nhập giá trị hệ số B: "))
C = int(input("Nhập giá trị hệ số C: "))
N = int(input("Nhập giá trị N: "))

# Duyệt từ x=1 đến x=N-1
for x in range(1, N):
    # Tính giá trị biểu thức Ax^2 + Bx + C với x hiện tại
    expression_value = evaluate_expression(A, B, C, x)
    # Kiểm tra giá trị tính được có phải là số nguyên tố hay không
    if is_prime(expression_value):
        # Nếu là số nguyên tố thì in ra giá trị x và kết thúc việc duyệt
        print("Giá trị x tìm được là:", x)
        break
#Chú ý rằng trong trường hợp không tìm thấy giá trị x thỏa mãn y




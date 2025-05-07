from datetime import date

# 1. 💰 Calculadora de propina  
def calculate_tip(amount, percentage):
    return amount * percentage/100
# print(calculate_tip(100, 15))
 
# 2. 📏 Conversor de unidades  
def meters_to_kilometers(meters):
    return meters / 1000
# print(meters_to_kilometers(1500))

# 3. ✉️ Generador de email empresarial 
def create_email(name, last_name, domain):
    return f"{name.lower()}.{last_name.lower()}@{domain.lower()}"     
# print(create_email("Lucia", "Gomez", "empresa.com"))

# 4. 🧾 Precio con impuestos  
def final_price(base_price, iva):
    return base_price + (iva * 100)
# print(final_price(100, 0.21))

# 5. 🔐 Simulador de login  
def validate_login(user, password):
    if user == "admin" and password == "1234":
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas")
        return False
# validate_login("admin", "1234")

# 6. 🧑‍💻 Generador de nombre de usuario  
def generate_username(name, birth):
    generate = name.lower() + str(birth)[2:]
    return generate

generate = generate_username("Lucas", 1997)
# print(generate)

# 7. ✨ Formateador de nombres  
def format_name(complete_name):
    return complete_name.title()
# print(format_name("juan perez"))

# 8. 🎂 Calculadora de edad  
def calculate_age(birth_age):
    return 2025 - birth_age  
# print(calculate_age(2000))

# 9. 📞 Validación de número telefónico  
def validate_phone(number):
    if number == 1234567890:
        print("is True")
        return True
    else:
        print("is False")
        return False 
# print(validate_phone(1234567890))

# 10. 🧠 Notas de estudiantes  
def student_average(name, *notes):
    joi = name.join(notes)
    average = sum(notes) 

print(student_average("Ana", 23, 44,))

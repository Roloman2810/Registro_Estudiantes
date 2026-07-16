 
def estandariza_texto(texto: str, formato: str) -> str:
#Limpia y estandariza los espacios en blanco y el formato del texto.
  
    texto_limpio = texto.strip()
    
    if formato == "titulo":
        return texto_limpio.title() # Ej: "juan pérez" -> "Juan Pérez"
    elif formato == "minuscula":
        return texto_limpio.lower() # Ej: "JUAN@GMAIL.COM" -> "juan@gmail.com"
    elif formato == "mayuscula":
        return texto_limpio.upper() # Ej: "micitt" -> "MICITT"
    
    return texto_limpio


  
def _solicitar_edad() -> int:
# Solicita la edad por consola asegurando obligatoriamente que sea 
# un número entero mediante manejo de excepciones.   
    edad_valida = False
    edad_final = 0
    
    while not edad_valida:
        entrada = input("Ingrese su edad: ").strip()
        try:
            edad_final = int(entrada)
            edad_valida = True
        except ValueError:
            print("-> Error: La edad introducida no es un número. Por favor, intente de nuevo.")
        finally:
            if not edad_valida:
                print("-> [Sistema]: Reiniciando el proceso de captura de edad...\n")
            else:
                print("-> [Sistema]: Validación de edad completada con éxito.\n")
                
    return edad_final

def validar_correo(correo):

    if " " in correo:
        return False
 
    if correo.count("@") != 1:
        return False
 
    usuario, dominio = correo.split("@")
 
    if usuario == "" or dominio == "":
        return False
 
    if "." not in dominio:
        return False
 
    return True




def capturar_participante() -> dict:
# Función principal que ejecuta la solicitud de datos, utiliza las
# funciones auxiliares para limpieza y validación, y retorna el 
# diccionario estructurado.
    
    print("=== Formulario de Captura de Datos ===")
    
    # 1. Captura de Nombre
    nombre_estudiante = input("Ingrese su nombre completo: ")
    nombre = estandariza_texto(nombre_estudiante, "titulo")
    
    # 2. Captura de Edad
    edad = _solicitar_edad()
    
    # 3. Captura de Correo
      
    correo_valido = False
    while not correo_valido:
        entrada_correo = input("Ingrese su correo electrónico: ")
        correo = estandariza_texto(entrada_correo, "minuscula")
           
        try:
            if validar_correo (correo):
                print ("-> El correo ingresado es inválido.")
                correo_valido = True                
            else:
                print ("-> La información proporcionada no es un correo.")
        except ValueError:
            print ("->[Sistema] Verifique el correo proporcionado e intente de nuevo.")
            print("-> [Sistema]: Reiniciando el proceso de captura de correo...\n")
                
    # 4. Captura de Empresa    
    entrada_empresa = input("Ingrese el nombre de su empresa: ")
    empresa = estandariza_texto(entrada_empresa, "mayuscula")
    
    # 5. Retorno del diccionario estructurado
    participante = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
        "empresa": empresa
    }
    
    return participante



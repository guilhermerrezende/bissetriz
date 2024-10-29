def calcular_razao_bissetriz_externa(lado_ab, lado_ac, lado_bc):
    
    if lado_ab <= 0 or lado_ac <= 0 or lado_bc <= 0:
        return "Erro: Todos os lados devem ser maiores que zero."
    if lado_ab + lado_ac <= lado_bc or lado_ab + lado_bc <= lado_ac or lado_ac + lado_bc <= lado_ab:
        return "Erro: Os lados fornecidos não formam um triângulo válido."
    
   
    try:
        bd_dc = -lado_ab / lado_ac  
        bd = abs(bd_dc * lado_bc / (1 + bd_dc))
        dc = lado_bc + bd  
        
        
        if dc == 0:
            return "Erro: Divisão por zero ao calcular a razão BD/DC."

        return bd, dc, bd / dc


    except ZeroDivisionError:
        return "Erro: Divisão por zero ao calcular a razão da bissetriz externa."


try:
    lado_ab = float(input("Digite o comprimento do lado AB: "))
    lado_ac = float(input("Digite o comprimento do lado AC: "))
    lado_bc = float(input("Digite o comprimento do lado BC: "))

    resultado = calcular_razao_bissetriz_externa(lado_ab, lado_ac, lado_bc)
    if isinstance(resultado, str):
        print(resultado)  
    else:
        bd, dc, razao = resultado
        print(f"Segmentos BD e DC (no prolongamento de BC) são, respectivamente: {bd:.2f} e {dc:.2f}")
        print(f"A razão BD/DC é: {razao:.2f}, conforme o teorema da bissetriz externa.")
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para os lados do triângulo.")

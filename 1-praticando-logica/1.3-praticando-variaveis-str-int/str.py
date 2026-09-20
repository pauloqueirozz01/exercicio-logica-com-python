# str significa string: texto entre aspas, mesmo quando contém algarismos.
idade_texto = "18"
nome = "Ana"

print("=== Textos (str) ===")
print("Idade escrita como texto:", idade_texto)
print("Tipo da idade:", type(idade_texto))

# O sinal + junta dois textos. Ele não faz uma soma nesse caso.
print("Juntando dois textos:", idade_texto + "2")  # Mostra 182.
print("Apresentação:", nome + " tem " + idade_texto + " anos.")

# Preveja: o que mudaria se idade_texto fosse 18, sem aspas?
# Para fazer contas com "18", será preciso convertê-lo para int.

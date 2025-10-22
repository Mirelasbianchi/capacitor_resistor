import matplotlib.pyplot as plt
import pandas as pd
import io

# Dados fornecidos em formato de string
dados_str = """
Tempo (ms),Tensao_C (V),Tensao_R (V)
0,4.9,0.1
500,4.8,0.2
1000,4.6,0.4
1500,4.4,0.6
2000,4.2,0.8
2500,4.0,1.0
3000,3.8,1.2
3500,3.6,1.4
4000,3.4,1.6
"""

# Usando pandas para carregar os dados de forma fácil a partir da string
# O 'io.StringIO(dados_str)' permite que a string seja lida como um arquivo
df = pd.read_csv(io.StringIO(dados_str))

# --- Preparação dos Dados ---
tempo_ms = df['Tempo (ms)']
tensao_c = df['Tensao_C (V)']
tensao_r = df['Tensao_R (V)']

# ----------------------------------------------------------------------
# 1) Gráfico da Tensão no Capacitor (C) - Descarga
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(tempo_ms, tensao_c, label='Tensão no C (V)', color='blue')
plt.title('Carga no Capacitor (C) - Na verdade, é a Descarga') # Título conforme sua imagem
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)

# ----------------------------------------------------------------------
# 2) Gráfico da Tensão no Resistor (R)
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(tempo_ms, tensao_r, label='Tensão no R (V)', color='red')
plt.title('Descarga no Resistor (R)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)

# ----------------------------------------------------------------------
# 3) Gráfico Comparativo
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(tempo_ms, tensao_c, label='Tensão no C (V)', color='blue')
plt.plot(tempo_ms, tensao_r, label='Tensão no R (V)', color='red')
plt.title('Comparação: Carga no C e Descarga no R')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)

# Opcional: plota tensão total
tensao_total = tensao_c + tensao_r
plt.figure(figsize=(8, 5))
plt.plot(tempo_ms, tensao_total, label='Tensão Total (C + R)', color='purple')
plt.title('Verificação da Tensão Total (V_C + V_R)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)

# Mostra todas as figuras de uma vez
plt.show()
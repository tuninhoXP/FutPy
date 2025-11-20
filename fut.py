import os
import pandas as pd
pasta_atual = os.getcwd()
arquivos_csv = [f for f in os.listdir(pasta_atual) if f.endswith('.csv')]
for arquivo in arquivos_csv:
    print(f"\n=== Lendo: {arquivo} ===")
    df = pd.read_csv(arquivo)
    print(df)

# Cadastro de Pessoas

Este projeto é um aprimoramento de um exercício do **Curso em Vídeo**, onde trabalhamos com cadastro de pessoas, armazenando informações como nome, peso e IMC.

## 📌 Funcionalidades
- Cadastro de múltiplas pessoas.
- Identificação da pessoa com o maior e menor peso.
- Consulta do IMC de uma pessoa cadastrada.

## 🛠 Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Importe as funções do módulo `utils`:  
   ```python
   from utils import cadastrar_pessoa, pessoas
   ```
3. Execute o script principal para cadastrar pessoas e visualizar informações:
   ```python
   mai, men = cadastrar_pessoa()
   ```
4. O programa exibirá:
   - A quantidade de pessoas cadastradas.
   - O maior e o menor peso e seus respectivos nomes.
   - Um menu interativo para consultar o IMC de uma pessoa específica.

## 📚 Exemplo de Uso
```
Foram cadastradas 3 pessoas
O maior peso foi de 90KG. O peso foi de: João
O menor peso foi de 50KG. O peso foi de: Ana

Quer ver o IMC de qual pessoa? [0 para sair]: 1
João tem IMC de 27.78
```

## 📝 Notas
- O programa pode lidar com múltiplos cadastros.
- Para evitar erros, há uma verificação para que o usuário insira números válidos ao consultar o IMC.

---
Projeto baseado no curso de **Python do Curso em Vídeo** e aprimorado com novas funcionalidades. 🎯


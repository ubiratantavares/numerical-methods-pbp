# Método de Tabelamento (Varredura / Busca Incremental)

Este documento detalha o **Método de Tabelamento** (também conhecido como Varredura ou Busca Incremental), baseado na análise das fontes bibliográficas do projeto. A estruturação segue a metodologia **5W2H**.

## 1. What (O que é?)

O Método de Tabelamento é uma técnica numérica elementar utilizada para **localizar e isolar raízes** de uma função $f(x)$. Consiste em calcular os valores da função em uma série de pontos igualmente espaçados dentro de um intervalo de interesse e verificar onde ocorre uma **mudança de sinal** nos valores de $f(x)$.

Segundo o Teorema de Bolzano, se uma função contínua $f(x)$ muda de sinal entre dois pontos $x_i$ e $x_{i+1}$ (ou seja, $f(x_i) \cdot f(x_{i+1}) < 0$), então existe pelo menos uma raiz real nesse subintervalo.

## 2. Why (Por que usar?)

* **Simplicidade:** É extremamente fácil de entender e implementar.
* **Isolamento Inicial:** É fundamental para fornecer "chutes iniciais" (estimativas) para métodos abertos mais sofisticados e rápidos (como Newton-Raphson ou Secante), que exigem uma boa aproximação inicial para convergir.
* **Visualização:** Ajuda a compreender o comportamento global da função antes de refinar a busca.
* **Robustez (em certo grau):** Não sofre de problemas de divisão por zero (como Newton) em sua forma básica.

## 3. Where (Onde se aplica?)

* **Fase de Isolamento:** É aplicado na primeira etapa da resolução de equações, antes da aplicação de métodos de refinamento.
* **Análise Exploratória:** Utilizado quando não se tem informações prévias sobre a localização das raízes.
* **Engenharia e Ciências:** Em problemas onde se deseja ter uma ideia geral das soluções possíveis dentro de um domínio físico válido.

## 4. When (Quando usar?)

* Quando se desconhece a localização aproximada das raízes.
* Quando se suspeita da existência de múltiplas raízes em um intervalo e se deseja separá-las.
* Como passo prévio obrigatório para métodos que exigem um intervalo que contenha a raiz (como Bisseção e Falsa Posição).

## 5. Who (Quem usa / Quem desenvolveu?)

* **Histórico:** Historicamente, era realizado manualmente através da construção de tábuas (tabelas) de funções.
* **Usuários:** Estudantes, engenheiros e cientistas utilizam-no como ferramenta de "força bruta" inicial.
* **Referências:** Citado amplamente em bibliografias clássicas como Chapra ("Busca Incremental"), Ruggiero & Lopes, e materiais didáticos de cálculo numérico (UFF, UFSC, UTFP).

## 6. How (Como funciona?)

O algoritmo funciona da seguinte maneira:

1. **Definição:** Escolhe-se um intervalo inicial $[a, b]$ e um número de subintervalos $n$ (ou um passo $h$).
2. **Discretização:** Divide-se o intervalo em pontos $x_0, x_1, \dots, x_n$, onde $x_i = a + i \cdot h$.
3. **Avaliação:** Calcula-se $f(x_i)$ para cada ponto.
4. **Verificação (Teste de Bolzano):** Percorre-se a tabela verificando o produto $f(x_i) \cdot f(x_{i+1})$:
    * Se $f(x_i) \cdot f(x_{i+1}) < 0$, há uma raiz no intervalo $[x_i, x_{i+1}]$.
    * Se $f(x_i) \cdot f(x_{i+1}) = 0$, um dos pontos é a raiz exata.
5. **Refinamento (Opcional):** O subintervalo encontrado pode ser usado como entrada para um método mais preciso.

### Algoritmo Simplificado (Pseudocódigo)

```python
def tabela(f, a, b, passos):
    h = (b - a) / passos
    x = a
    f_anterior = f(x)
    
    intervalos_com_raiz = []
    
    for i in range(passos):
        x_prox = x + h
        f_prox = f(x_prox)
        
        if f_anterior * f_prox < 0:
            intervalos_com_raiz.append((x, x_prox))
            
        x = x_prox
        f_anterior = f_prox
        
    return intervalos_com_raiz
```

## 7. How Much (Quanto custa / Qual o custo?)

* **Custo Computacional:** O custo é **proporcional ao número de passos** (ou inversamente proporcional ao tamanho do passo $h$).
  * Muitos passos ($h$ pequeno) = Alto custo computacional (muitas avaliações de função), mas menor risco de perder raízes.
  * Poucos passos ($h$ grande) = Baixo custo, mas alto risco de pular raízes (especialmente raízes múltiplas ou muito próximas).
* **Limitação:** É um método ineficiente para obter alta precisão (exigiria um $h$ minúsculo). Seu "custo" principal é a ineficiência se usado como método único de solução.

**Fontes Consultadas:**

* *2008 - Métodos Numéricos para Engenharia.pdf* (Chapra)
* *calculo_numerico_capitulo2.pdf* (Material Didático)
* *Aula-Zeros.pdf*

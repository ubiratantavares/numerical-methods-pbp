# Método das Tentativas (Força Bruta / Trial and Error)

Este documento detalha o **Método das Tentativas** (também conhecido como Força Bruta ou Tentativa e Erro), baseado na análise das fontes bibliográficas do projeto. A estruturação segue a metodologia **5W2H**.

## 1. What (O que é?)

O Método das Tentativas é uma abordagem heurística e iterativa para encontrar raízes de uma função $f(x)$. Diferente de métodos sistemáticos como a Bisseção ou Newton, este método envolve "chutar" valores para $x$ e avaliar $f(x)$ repetidamente até que o valor da função esteja suficientemente próximo de zero (dentro de uma tolerância $\epsilon$).

## 2. Why (Por que usar?)

* **Intuição:** É o método mais intuitivo para humanos (ex: "está muito alto, diminui um pouco").
* **Simplicidade Extrema:** Não requer cálculo de derivadas nem intervalos iniciais estritos (embora ajudem).
* **Flexibilidade:** Pode ser adaptado para usar heurísticas aleatórias (Monte Carlo) ou guiadas pelo usuário.

## 3. Where (Onde se aplica?)

* **Problemas Mal Comportados:** Funções onde métodos de gradiente falham ou onde não há garantia de continuidade.
* **Estimativas Rápidas:** Para obter uma ideia grosseira da raiz antes de aplicar um método refinado.
* **Educação:** Para demonstrar a dificuldade de encontrar raízes sem um algoritmo estruturado.

## 4. When (Quando usar?)

* Quando outros métodos falham.
* Quando o custo de avaliação da função é muito baixo.
* Quando se deseja explorar o comportamento da função de forma aleatória ou semi-aleatória.

## 5. Who (Quem usa / Quem desenvolveu?)

* **Origem:** Pré-computacional, utilizado intuitivamente desde a antiguidade.
* **Usuários:** Estudantes iniciantes em programação e métodos numéricos.

## 6. How (Como funciona?)

O algoritmo básico (versão aleatória/guiada):

1. **Chute Inicial:** Escolhe-se um valor $x$.
2. **Avaliação:** Calcula-se $erro = |f(x)|$.
3. **Teste:** Se $erro < \epsilon$, $x$ é a raiz aproximada.
4. **Ajuste:** Se não, escolhe-se um novo $x$ (pode ser aleatório, ou baseado no sinal do erro anterior).
5. **Repetição:** Repete-se até satisfazer a tolerância ou atingir o número máximo de tentativas.

### Pseudocódigo (Versão Aleatória em Intervalo)

```python
import random

def tentativas(f, a, b, tolerancia, max_tentativas):
    melhor_x = None
    menor_erro = float('inf')
    
    for _ in range(max_tentativas):
        x = random.uniform(a, b)
        erro = abs(f(x))
        
        if erro < menor_erro:
            menor_erro = erro
            melhor_x = x
            
        if menor_erro < tolerancia:
            return melhor_x
            
    return melhor_x # Retorna o melhor encontrado mesmo se não atingiu tolerância
```

## 7. How Much (Quanto custa / Qual o custo?)

* **Custo Computacional:** Altamente imprevisível. Pode encontrar a raiz na primeira tentativa ou nunca encontrar.
* **Ineficiência:** Geralmente muito ineficiente comparado a métodos determinísticos. O "custo" é a falta de garantia de convergência.

**Fontes Consultadas:**

* *Numerical Methods.pdf*
* *Análise de heurísticas gerais de resolução de problemas.*

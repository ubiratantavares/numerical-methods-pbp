# Método de Isolamento de Raízes (Teorema de Bolzano)

Este documento detalha o **Método de Isolamento de Raízes** fundamentado no **Teorema de Bolzano**, baseado na análise das fontes bibliográficas do projeto. A estruturação segue a metodologia **5W2H**.

## 1. What (O que é?)

O Isolamento de Raízes é a fase inicial da resolução numérica de equações, onde se busca determinar intervalos $[a, b]$ que contenham pelo menos uma raiz real da equação $f(x) = 0$. O **Teorema de Bolzano** (ou Teorema do Valor Intermediário) é a base teórica: se $f(x)$ é contínua em $[a, b]$ e $f(a) \cdot f(b) < 0$, então existe pelo menos uma raiz real em $(a, b)$.

## 2. Why (Por que usar?)

* **Garantia de Existência:** Fornece uma garantia matemática da existência da raiz.
* **Pré-requisito:** A maioria dos métodos de refinamento (Bisseção, Falsa Posição, Newton) exige um intervalo inicial ou uma boa aproximação que só é obtida após o isolamento.
* **Separação de Raízes:** Permite distinguir raízes distintas em funções que oscilam.

## 3. Where (Onde se aplica?)

* **Análise de Funções:** Em qualquer problema matemático ou de engenharia que envolva encontrar zeros de funções contínuas.
* **Algoritmos de Busca:** É o "motor" de decisão dentro de métodos de varredura e bisseção.

## 4. When (Quando usar?)

* Sempre, como **primeiro passo** antes de tentar calcular o valor numérico preciso da raiz.
* Para verificar se um intervalo candidato obtido por outros meios (ex: gráfico) é válido.

## 5. Who (Quem usa / Quem desenvolveu?)

* **Bernhard Bolzano:** Matemático que provou o teorema.
* **Engenheiros e Matemáticos:** Utilizam o teorema para validar a existência de soluções em modelos físicos.
* **Referências:** Citado em todas as bibliografias básicas de Cálculo Numérico (Chapra, Ruggiero, Franco, etc.).

## 6. How (Como funciona?)

O processo de isolamento envolve:

1. **Análise Gráfica (Opcional):** Esboçar o gráfico para identificar regiões promissoras.
2. **Análise Analítica (Derivadas):** Usar a primeira derivada $f'(x)$ para determinar intervalos de crescimento/decrescimento. Se $f(x)$ é monótona em $[a, b]$ e troca de sinal, a raiz é **única**.
3. **Verificação Numérica:** Escolher pontos $a$ e $b$ e testar o sinal de $f(a) \cdot f(b)$.

### Algoritmo de Verificação

```python
def verifica_bolzano(f, a, b):
    try:
        fa = f(a)
        fb = f(b)
        if fa * fb < 0:
            return True # Raiz garantida (pelo menos uma)
        else:
            return False # Inconclusivo (pode haver 0 ou par de raízes)
    except:
        return False # Erro na avaliação (descontinuidade, etc)
```

## 7. How Much (Quanto custa / Qual o custo?)

* **Custo Computacional:** Baixíssimo (apenas duas avaliações de função).
* **Custo Intelectual:** Requer análise prévia do comportamento da função (continuidade) para ser aplicado corretamente. O teorema não garante unicidade sem análise de derivadas.

---

**Fontes Consultadas:**

* *2008 - Métodos Numéricos para Engenharia.pdf* (Chapra)
* *Caderno_Didatico_Calculo_Numerico.pdf*
* *2009 - Cálculo Numérico - Fundamentos e Aplicações.pdf*

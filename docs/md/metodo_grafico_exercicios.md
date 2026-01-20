# Exercícios e Problemas: Método Gráfico

Este documento lista exercícios e problemas práticos encontrados nas referências bibliográficas que utilizam o **Método Gráfico** para localização de raízes.

## 1. Métodos Numéricos para Engenharia (Chapra & Canale, 2008)

Esta fonte é a mais abrangente, dedicando o início do Capítulo 5 inteiramente aos Métodos Gráficos.

* **Problemas Propostos (Resolução Gráfica):**

  * **5.1:** $f(x) = -0.5x^2 + 2.5x + 4.5$

  * **5.2:** $f(x) = 5x^3 - 5x^2 + 6x - 2$

  * **5.3:** Determinar a raiz de um polinômio de grau 5.

  * **5.4:** $f(x) = -12 - 21x + 18x^2 - 2.75x^3$

  * **5.5:** $\text{sen}(x) = x^3$ (Primeira raiz não-trivial)

  * **5.6:** $\ln(x^4) = 0.7$ (Raiz real positiva)

  * **5.7:** $f(x) = (0.8 - 0.3x)/x$

* **Exemplos 5.1 e 5.2:** Estudos de caso com gráficos computacionais (ex: $f(x) = \text{sen}(10x) + \cos(3x)$).

* **Exemplo 6.2:** Método das Duas Curvas para $e^{-x} - x = 0$ (separando em $y_1 = x$ e $y_2 = e^{-x}$).

## 2. Métodos Numéricos (Sérgio Roberto de Freitas, 2000)

* **Exercício 3.7 (Questão 1):** Localize graficamente todos os zeros das funções:

  * (a) $f(x) = e^x - 3|x|$

  * (b) $f(x) = \text{sen}(x) - x/2$

  * (c) $f(x) = 2^x - \cos(x) - 1$

* **Exemplo 3.1.1:** Delimitação de zeros de $f(x) = e^x + x^2 - 2$ via intersecção de $g(x) = e^x$ e $h(x) = 2 - x^2$.

## 3. Cálculo Numérico - Um Livro Colaborativo (Octave, 2018)

* **Exercício E 3.2.2:** Trace o gráfico e isole as três primeiras raízes positivas de $f(x) = 5\text{sen}(x^2) - \exp(x/10)$.

* **Exercício E 3.4.3:** Trace o gráfico de $e^{-x^2} = x$ para verificar existência de raiz positiva.

* **Exercício E 3.4.4:** Isolar e encontrar raízes via gráfico e Newton.

## 4. Cálculo Numérico (José Eduardo Castilho, 2001)

* **Exemplo 2.1.1:** Isolamento da raiz de $f(x) = e^{-x} - x$ transformando em intersecção de $g(x) = e^{-x}$ e $h(x) = x$.

## 5. Cálculo Numérico Computacional - UFSC (Peters & Szeremeta, 2018)

* **Exemplo 3.1:** Isolar raiz de $e^x \text{sen}(x) - 1 = 0$ via esboço gráfico.

* **Exemplo 4.1:** Método gráfico para **sistema não-linear**: intersecção entre circunferência ($x_1^2 + x_2^2 - 9 = 0$) e hipérbole ($x_1 x_2 - 1 = 0$).

## 6. Noções de Cálculo Numérico (Humes et al., 1984)

* **Exemplo 2.1:** Raízes reais de $f(x) = x \ln(x) - 3.2$, decompondo em $y = 5 \log(x)$ e $y = 2 - 0.4x$.

## 7. Aula-Zeros (Material Didático)

* **Referências Citadas:**

  * Gilat & Subramaniam (2008)
  * I. Q. Barros (1972)
  * Neide B. Franco (2007)

* **Problemas Práticos:**

  * $f(x) = x - \cos(x) = 0$: Delimitação visual do zero.
  * $f(x) = x \cdot \tan(x) - 1 = 0$: Encontrar zeros via intersecção de $g(x) = \tan(x)$ e $h(x) = 1/x$.

## 8. Livro Cálculo Numérico com Python Google Colab (Fábio e Cinthia)

Esta fonte ensina explicitamente a técnica de separação de funções ($g(x) - h(x) = 0$).

* **Exercícios Propostos (Separação e Gráfico):**

  * **(01)** $f(x) = 0.2x^2 + \text{sen}(x)$

  * **(02)** $f(x) = x^2 - 4x$

  * **(03)** $f(x) = x^2 - \cos(x)$

  * **(04)** $f(x) = x^3 + \text{sen}(x)$

## 9. Métodos Numéricos básicos (Torelli)

* **Problema 1 (Crescimento Populacional):** Gráfico da função $g(t)$ versus biovolume para isolar o intervalo da raiz.

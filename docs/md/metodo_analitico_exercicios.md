# Exercícios e Problemas: Método Analítico

Este documento lista exercícios e problemas práticos encontrados nas referências bibliográficas que utilizam o **Método Analítico** (Teoremas de Bolzano, Rolle, análise de derivadas e sinais) para delimitar, justificar a existência ou isolar raízes.

## 1. Noções de Cálculo Numérico (Humes et al., 1984)

Esta fonte contém uma fundamentação teórica robusta sobre o método analítico e exercícios diretos de aplicação.

* **Exercício 1 (Capítulo 2):** Solicita: "pesquisar a existência de raízes das funções acima e isolá-las em intervalos".

  * $f(x) = \text{cosec}(x) - \tan(x)$

  * $f(x) = e^{-x} - \ln(x)$

  * *Nota:* Este tipo de pesquisa exige o uso do Teorema de Bolzano e análise de continuidade.

* **Análise de Derivadas (Exemplo):** O texto apresenta a teoria de usar a primeira derivada $f'$ e a segunda $f''$ para distinguir raízes simples de múltiplas e separar raízes muito próximas.

## 2. Cálculo Numérico com Aplicações (1987)

Apresenta exemplos resolvidos detalhados que utilizam teoremas do cálculo para isolar raízes.

* **Exemplo 3.29:** Calcular a raiz negativa de um polinômio cúbico.

  * A resolução inicia com: "Aplicando o teorema de Lagrange...", calculando $f'(x)$ e $f''(x)$ para determinar intervalos de crescimento e concavidade.

  * Garante a unicidade da raiz no intervalo $[-2.44, -0.38]$.

* **Análise de Limites de Raízes (Página 142):** Problemas resolvidos (Plano A e Plano B) para determinar o número de raízes reais e seus limites (cotas) baseados nos coeficientes do polinômio (Regra de Sinais de Descartes e Teoremas de Cotas).

## 3. Cálculo Numérico (Neide Maria Bertoldi Franco)

Exercícios focados na justificativa teórica da existência de raízes.

* **Exercício 3.1:** "Dadas as funções... pesquisar a existência de raízes reais e isolá-las em intervalos."

* **Exercício 3.2:** "Justifique que a função... possui uma raiz no intervalo $(-1, 0)$ e outra no intervalo $(0, 1)$."

  * A palavra "Justifique" implica o uso do Teorema de Bolzano (troca de sinal) e análise da função.

## 4. Métodos Numéricos para Engenharia (Chapra & Canale, 2008)

Apresenta problemas que exigem solução analítica para comparação ou isolamento.

* **Problema 5.7:** Determinar a raiz real de $f(x) = (0.8 - 0.3x)/x$.

  * Item (a): "Analiticamente".

* **Problema 4.2:** Encontrar raízes simbólicas (analíticas) de um polinômio usado por Wallis, utilizando ferramentas algébricas.

## 5. Métodos Numéricos (Sérgio Roberto de Freitas, 2000)

* **Seção 3.1.2:** Seção específica sobre "Método Analítico" para delimitação dos zeros.

* **Exercícios 3.7:** Localização de zeros. A discussão sugere o uso de derivadas para auxiliar quando o gráfico não é óbvio.

* **Seção 4.2 (Zeros de Polinômios):** Discussão sobre delimitação analítica (cotas) de zeros.

## 6. Cálculo Numérico (José Eduardo Castilho, 2001)

* **Exercício 2.5:** "Encontrar um intervalo que depende do valor de $a$ e que contenha a raiz" para a raiz p-ésima de um número.

  * Exige manipulação algébrica e analítica de desigualdades.

* **Exercício 2.7:** Provar um teorema relacionado à convergência (Teorema 2.5.1).

## 7. Soluções Exatas (Histórico e Aplicação)

Esta seção aborda a aplicação de métodos analíticos para encontrar a solução exata de equações polinomiais, quando possível.

* **Equações Lineares (Euclides):**
  * $ax + b = 0 \implies x = -b/a$
  * Exemplo: $2x - 4 = 0 \implies x = 2$

* **Equações Quadráticas (Bhaskara / Sridhara):**
  * $ax^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
  * Exemplo: $x^2 - 5x + 6 = 0 \implies x = 2, x = 3$

* **Equações Cúbicas (Cardano / Tartaglia):**
  * Solução analítica para $ax^3 + bx^2 + cx + d = 0$.
  * Exemplo: $x^3 - 6x^2 + 11x - 6 = 0 \implies x = 1, x = 2, x = 3$

* **Equações Quárticas (Ferrari):**
  * Redução para uma equação cúbica resolvente.
  * Exemplo: $x^4 - 1 = 0 \implies x = \pm 1, x = \pm i$

* **Limitações (Abel-Ruffini):**
  * Para polinômios de grau $n \ge 5$, não existe fórmula geral por radicais.
  * Exemplo: $x^5 - x - 1 = 0$ (Solução exata geral não garantida, requer métodos numéricos).

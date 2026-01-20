# Método Gráfico: Análise 5W2H

Este documento detalha o **Método Gráfico** para localização de raízes de equações, utilizando a metodologia 5W2H e baseando-se nas fontes bibliográficas do projeto.

## Referências Bibliográficas

1. *Métodos Numéricos* (2000)
2. *Cálculo Numérico* (2001)
3. *Métodos Numéricos para Engenharia* (Chapra, 2008)
4. *Numerical Methods in Scientific Computing* (2008)
5. *Fundamentos de Cálculo Numérico para Engenheiros* (2009)
6. *Cálculo Numérico - Um Livro Colaborativo (Octave)* (2018)
7. *Cálculo Numérico Computacional - UFSC* (2018)
8. *Livro Cálculo Numérico com Python Google Colab* (Fábio e Cinthia)
9. *Métodos Numéricos para Engenharia* (Referência Adicional)

## 5W2H do Método Gráfico

### 1. What (O que é?)

É uma técnica visual e exploratória para identificar a localização aproximada das raízes de uma equação $f(x) = 0$. Consiste em traçar o gráfico da função em um sistema de coordenadas cartesianas e observar os pontos onde a curva intercepta o eixo das abcissas (eixo $x$). Alternativamente, pode-se separar a equação em duas funções, $g(x) = h(x)$, e buscar os pontos de interseção entre elas.
**Insight Adicional:** Em contextos modernos (como Google Colab), utiliza-se bibliotecas como `matplotlib` e `numpy` para gerar visualizações dinâmicas e interativas, permitindo "zoom" em regiões de interesse.

### 2. Why (Por que usar?)

* **Intuição Visual:** Fornece uma compreensão imediata do comportamento da função (crescimento, concavidade, descontinuidades).

* **Estimativa Inicial:** É essencial para fornecer "chutes" iniciais ($x_0$) ou intervalos de isolamento $[a, b]$ para métodos numéricos mais refinados (como Newton-Raphson ou Bisseção), que dependem de boas aproximações para convergir.

* **Verificação:** Serve como uma ferramenta rápida para validar resultados obtidos por métodos algorítmicos.

* **Diagnóstico de Problemas:** Permite identificar visualmente problemas de **mal-condicionamento** ou raízes múltiplas (onde a função tangencia o eixo $x$ sem cruzá-lo), situações que podem causar falha ou convergência lenta em métodos iterativos.

### 3. Where (Onde é aplicado?)

* Na fase preliminar de qualquer problema de busca de raízes.

* Em softwares de matemática simbólica e numérica (Matlab, Python/Matplotlib, GeoGebra) para análise exploratória.

* No ensino de cálculo numérico para ilustrar conceitos de zeros de funções.

### 4. When (Quando usar?)

* Sempre que se inicia a análise de uma nova equação não linear cujas propriedades não são bem conhecidas.

* Quando se suspeita de múltiplas raízes ou raízes próximas, onde métodos cegos podem falhar.

* Para determinar a existência e unicidade de raízes em um intervalo antes de aplicar métodos iterativos.

### 5. Who (Quem utiliza?)

* Engenheiros e cientistas na modelagem de problemas físicos.

* Estudantes de cálculo numérico.

* Analistas de dados para inspeção visual de funções de custo ou erro.

### 6. How (Como funciona?)

O método pode ser aplicado de duas formas principais:

**Forma Direta ($f(x) = 0$):**

1. Define-se um intervalo de interesse para a variável $x$.

2. Calculam-se os valores de $f(x)$ para diversos pontos neste intervalo.

3. Plota-se o gráfico de $f(x)$ versus $x$.

4. Identificam-se visualmente os pontos onde a curva cruza o eixo $x$ ($y=0$).

**Forma de Separação ($g(x) = h(x)$):**

1. Reescreve-se $f(x) = 0$ como $g(x) = h(x)$ (ex: $e^{-x} - x = 0 \rightarrow e^{-x} = x$).

2. Plotam-se ambas as funções $y_1 = g(x)$ e $y_2 = h(x)$ no mesmo gráfico.

3. A abcissa do ponto de interseção das duas curvas corresponde à raiz da equação original.

**Implementação Moderna (Python/Colab):**

Utiliza-se `numpy` para criar vetores de pontos (`x = np.linspace(a, b, n)`) e `matplotlib.pyplot` para plotagem (`plt.plot(x, f(x))`), adicionando grade (`plt.grid()`) para facilitar a leitura das coordenadas.

### 7. How Much (Quanto custa / Qual o custo computacional?)

* **Custo Computacional:** Baixo para funções simples e visualização 2D. Depende da resolução (número de pontos) necessária para uma visualização suave.

* **Precisão:** Baixa. O método é qualitativo e não fornece raízes com alta precisão numérica (geralmente limitado à resolução visual ou do grid de plotagem). É um método de *localização*, não de *refinamento*.

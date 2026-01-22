# Método de Busca Incremental (Incremental Search)

Este documento detalha o **Método de Busca Incremental**, baseado na análise das fontes bibliográficas do projeto, especialmente Chapra & Canale. A estruturação segue a metodologia **5W2H**.

## 1. What (O que é?)

O Método de Busca Incremental é uma técnica numérica exploratória utilizada para **identificar intervalos que contêm raízes** de uma função $f(x)$. Ele percorre um domínio de interesse em passos fixos (incrementos), avaliando a função em cada ponto e verificando a ocorrência de **mudança de sinal** entre pontos consecutivos.

Se $f(x_i)$ e $f(x_{i+1})$ têm sinais opostos, assume-se que existe pelo menos uma raiz no intervalo $[x_i, x_{i+1}]$.

## 2. Why (Por que usar?)

* **Simplicidade:** É intuitivo e fácil de programar.
* **Segurança Inicial:** Serve como uma "rede de segurança" para encontrar boas estimativas iniciais para métodos mais rápidos (como Newton-Raphson), que podem divergir se iniciados longe da raiz.
* **Detecção de Múltiplas Raízes:** Ao varrer um grande intervalo, pode identificar múltiplas sub-regiões de interesse, ao contrário de métodos que convergem para uma única raiz.

## 3. Where (Onde se aplica?)

* **Fase Preliminar:** Aplicado no início da análise numérica de um problema.
* **Sistemas de Engenharia:** Em problemas físicos onde se conhece os limites operacionais (ex: temperatura entre 0 e 100°C) e se deseja varrer todo o espectro em busca de soluções de equilíbrio.
* **Gráficos Computacionais:** É a base lógica por trás da plotagem de gráficos para inspeção visual de raízes.

## 4. When (Quando usar?)

* Quando não se tem nenhuma ideia prévia de onde as raízes estão.
* Quando se suspeita que a função pode ter múltiplas raízes e se deseja encontrar todas elas dentro de um domínio.
* Antes de aplicar métodos de refinamento (Bisseção, Falsa Posição, Newton) para garantir que o intervalo inicial contém uma raiz (bracketing).

## 5. Who (Quem usa / Quem desenvolveu?)

* **Referências:** Amplamente citado por **Steven C. Chapra** e **Raymond P. Canale** em "Numerical Methods for Engineers" como uma técnica fundamental de isolamento. Também referenciado por **Jaan Kiusalaas** em contextos de programação Python.
* **Público:** Engenheiros e cientistas que precisam de robustez na inicialização de algoritmos de otimização ou busca de raízes.

## 6. How (Como funciona?)

O algoritmo opera da seguinte forma:

1. **Escolha do Intervalo:** Define-se um intervalo global $[x_{start}, x_{end}]$.
2. **Definição do Incremento:** Escolhe-se um passo $\Delta x$ (ou número de divisões).
3. **Iteração:**
    * Inicia-se em $x_{curr} = x_{start}$.
    * Calcula-se $f(x_{curr})$.
    * Avança-se para $x_{next} = x_{curr} + \Delta x$.
    * Calcula-se $f(x_{next})$.
4. **Teste de Sinal:** Verifica-se se $f(x_{curr}) \cdot f(x_{next}) < 0$.
    * Se **Sim**: Armazena-se o intervalo $[x_{curr}, x_{next}]$ como candidato.
    * Se **Não**: Continua-se a varredura.
5. **Repetição:** O processo se repete até atingir $x_{end}$.

### Pseudocódigo

```python
def busca_incremental(f, inicio, fim, passo):
    x = inicio
    f_x = f(x)
    raizes_intervalos = []
    
    while x < fim:
        x_prox = x + passo
        f_prox = f(x_prox)
        
        if f_x * f_prox < 0:
            raizes_intervalos.append((x, x_prox))
            
        x = x_prox
        f_x = f_prox
        
    return raizes_intervalos
```

## 7. How Much (Quanto custa / Qual o custo?)

* **Custo Computacional:** Linearmente dependente do tamanho do intervalo e inversamente proporcional ao tamanho do passo ($Custo \approx \frac{L}{\Delta x}$).
* **Trade-off Precisão vs. Custo:**
  * Passos muito pequenos ($\Delta x \to 0$): Alta precisão no isolamento, mas custo computacional elevado (muitas avaliações de função).
  * Passos muito grandes: Baixo custo, mas risco de **perder raízes** (ex: se a função desce e sobe cruzando o eixo x duas vezes dentro de um único passo, a mudança de sinal não é detectada).
  * *Nota:* Raízes tangenciais (multiplicidade par) não são detectadas por mudança de sinal simples.

---

**Fontes Consultadas:**

* *2008 - Métodos Numéricos para Engenharia.pdf* (Chapra & Canale)
* *2005 - Numerical Methods in Engineering with Python.pdf* (Kiusalaas)

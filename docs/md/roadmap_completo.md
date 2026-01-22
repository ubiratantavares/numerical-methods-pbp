# Roadmap Completo

A seguir está um **roadmap completo, técnico e progressivo** para estudar **Métodos Numéricos em Python**, aplicando **POO, SOLID, Clean Code e MVC**, com foco em **engenharia de software científico** (não apenas matemática).

A proposta forma você para:

> construir **bibliotecas numéricas reutilizáveis, testáveis, extensíveis e profissionais**.

## 📌 Pré-requisitos

Antes do Módulo 1:

* Python intermediário
* Álgebra linear básica
* Cálculo diferencial e integral
* Git + virtualenv
* PyTest básico

## 🏗 Arquitetura Base do Projeto

Estrutura padrão para TODOS os módulos:

```bash
numerical_methods/
│
├── domain/        # Modelos matemáticos (entidades)
├── algorithms/    # Implementações numéricas
├── services/      # Casos de uso
├── interfaces/    # Abstrações (SOLID)
├── controllers/   # MVC Controller
├── views/         # CLI / API / Notebook
├── tests/
└── main.py
```

## 🔹 MÓDULO 1 — Introdução aos Métodos Numéricos

### Matemática

* Erros: absoluto, relativo, truncamento, arredondamento
* Estabilidade numérica
* Condicionamento

### Programação

* Tipagem estática (typing)
* Dataclasses
* POO básica

### Arquitetura

* Interfaces com `ABC`
* Injeção de dependência

### Projeto

```python
class NumericalMethod(ABC):
    @abstractmethod
    def solve(self): ...
```

### Entregável

✔ Framework base para métodos numéricos
✔ Testes unitários de erro numérico

## MÓDULO 2 — Raízes de Equações

### Métodos

* Bisseção
* Falsa posição
* Newton-Raphson
* Secante
* Ponto fixo

### Design

* Strategy Pattern
* Open/Closed Principle

### Exemplo

```python
class RootFinder(NumericalMethod):
    def solve(self, f, interval): ...
```

### Projeto MVC

* Controller recebe função
* Model representa equação
* View exibe iterações

* Entregável

✔ Biblioteca extensível de métodos de raiz
✔ Comparador automático de convergência

## MÓDULO 3 — Sistemas Lineares e Não Lineares

### Métodos

* Gauss
* LU
* Jacobi
* Gauss-Seidel
* Newton para sistemas

### Engenharia

* Separação entre matriz e algoritmo
* Imutabilidade

### Projeto

```python
class LinearSystemSolver:
    def solve(self, matrix, vector): ...
```

* Entregável

✔ Motor de resolução matricial
✔ Detector automático de dominância diagonal

## MÓDULO 4 — Otimização

### Métodos

* Gradiente descendente
* Newton
* Quase-Newton
* Busca unidimensional

### Arquitetura

* Função objetivo como entidade
* Otimizador como serviço

### Projeto

```python
class Optimizer:
    def minimize(self, function): ...
```

### Entregável

✔ Biblioteca de otimização extensível
✔ Sistema de log de convergência

## MÓDULO 5 — Regressão, Interpolação e Ajuste

### Métodos

* Interpolação polinomial
* Lagrange
* Newton
* Splines
* Regressão linear e não linear

### Engenharia

* Separar dados de modelo
* Regressor genérico

### Projeto

```python
class RegressionModel:
    def fit(self, data): ...
```

### Entregável

✔ Engine de ajuste de curvas
✔ Avaliação automática de erro

## MÓDULO 6 — Integração Numérica

### Métodos

* Trapézio
* Simpson
* Romberg
* Gaussiana

### Arquitetura

* Strategy
* Factory

### Projeto

```python
class Integrator:
    def integrate(self, f, a, b): ...
```

### Entregável

✔ Sistema de integração adaptativa

## MÓDULO 7 — EDOs

### Métodos

* Euler
* Euler modificado
* Runge-Kutta
* Adams-Bashforth

### Engenharia

* Separar equação de método
* Controle de passo adaptativo

### Projeto

```python
class ODESolver:
    def solve(self, equation, initial_conditions): ...
```

### Entregável

✔ Solver genérico de EDOs
✔ Visualizador de solução

## MÓDULO 8 — EDPs

### Métodos

* Diferenças finitas
* Elementos finitos (intro)
* Crank-Nicolson

### Engenharia

* Grid como entidade
* Solver desacoplado

### Projeto

```python
class PDESolver:
    def solve(self, grid, equation): ...
```

### Entregável

✔ Simulador numérico 2D

# 🧠 SOLID aplicado

| Princípio | Aplicação                         |
| --------- | --------------------------------- |
| SRP       | Cada método em classe própria     |
| OCP       | Novos métodos sem alterar código  |
| LSP       | Todos os métodos substituíveis    |
| ISP       | Interfaces pequenas               |
| DIP       | Algoritmos dependem de abstrações |

# 🧼 Clean Code

* Nomes matematicamente semânticos
* Funções < 20 linhas
* Um conceito por método
* Testes antes da implementação

# 🧪 Testes

* PyTest
* TDD para cada método
* Validação com soluções analíticas

# 📈 Projeto Final

Criar uma **Numerical Computing Library em Python**, com:

* API pública
* Documentação
* CLI
* Jupyter notebooks
* 100% orientada a SOLID

# 📚 Bibliografia Recomendada

* Chapra — Numerical Methods for Engineers
* Burden & Faires
* NumPy Docs
* SciPy Source Code
* Clean Code — Robert Martin

# 🔚 Resultado

Você termina com:

> capacidade de escrever **software numérico profissional**, usado em engenharia, ciência de dados, simulações e pesquisa.

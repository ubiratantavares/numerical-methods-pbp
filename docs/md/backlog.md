# Backlog e Checklist de Implementação

Baseado no `roadmap_completo.md`, este documento serve como um guia de implementação passo a passo para o projeto de Métodos Numéricos.

## 📌 Pré-requisitos (Antes do Módulo 1)

- [x] Instalar Python (versão mais recente estável)
- [x] Configurar Git e repositório
- [x] Criar ambiente virtual (`virtualenv` ou `venv`)
- [x] Instalar dependências iniciais (`pytest`, `numpy` se necessário)
- [ ] Revisar conceitos de Álgebra Linear e Cálculo (Just-in-Time: sob demanda)

## 🏗 Arquitetura Base

- [ ] Criar estrutura de diretórios:
  - `numerical_methods/domain`
  - `numerical_methods/algorithms`
  - `numerical_methods/services`
  - `numerical_methods/interfaces`
  - `numerical_methods/controllers`
  - `numerical_methods/views`
  - `numerical_methods/tests`
  - `numerical_methods/main.py`

## 🔹 MÓDULO 1 — Introdução aos Métodos Numéricos

**Objetivo:** Estabelecer o framework base e lidar com erros numéricos.

### Checklist

- [x] **Matemática**: Estudar e implementar conceitos de erros (absoluto, relativo, truncamento, arredondamento).
- [x] **Programação**: Definir uso de Dataclasses e Tipagem Estática.
- [x] **Arquitetura**: Criar interfaces base com `ABC`.
- [x] **Projeto**: Implementar classe abstrata `NumericalMethod`.

    ```python
    class NumericalMethod(ABC):
        @abstractmethod
        def solve(self): ...
    ```

- [x] **Testes**: Criar testes unitários para verificação de erros numéricos.

**Entregável:**

- [x] Framework base para métodos numéricos
- [x] Testes unitários de erro numérico

## 🔹 MÓDULO 2 — Raízes de Equações

**Objetivo:** Implementar métodos para encontrar raízes de equações.

- Checklist

- [ ] **Métodos de Localização e Isolamento**:

  - [x] Método Gráfico
  - [x] Método Analítico (Bolzano e Derivadas)
  - [x] Método Analítico (Solução Exata quando possível)
  - [x] Método de Tabelamento (Varredura)
  - [x] Método de Busca Incremental
  - [x] Método das Tentativas (Força Bruta)
  - [x] Método de Isolamento de Raízes (Teorema de Bolzano)

- [ ] **Métodos Intervalares**:

  - [ ] Bisseção (Dicotomia)
  - [ ] Falsa Posição (Regula Falsi)
  - [ ] Falsa Posição Modificado
  - [ ] Busca Incremental

- [ ] **Métodos Abertos**:

  - [ ] Ponto Fixo (Iteração Linear)
  - [ ] Newton-Raphson
  - [ ] Secante
  - [ ] Secante Modificado
  - [ ] Steffensen
  - [ ] Halley
  - [ ] Wegstein
  - [ ] Schröder

- [ ] **Métodos Híbridos**:

  - [ ] Brent
  - [ ] Ridders
  - [ ] Misto (Bissecção + Newton/Falsa Posição)
  - [ ] Interpolação Quadrática Inversa

- [ ] **Métodos para Polinômios**:

  - [ ] Müller
  - [ ] Bairstow
  - [ ] Birge-Vieta (Newton para polinômios)
  - [ ] Jenkins-Traub
  - [ ] Laguerre
  - [ ] Lin
  - [ ] Graeffe
  - [ ] Algoritmo Quociente-Diferença (QD)
  - [ ] Deflação Polinomial

- [ ] **Design**: Aplicar Strategy Pattern para seleção do método.

- [ ] **Design**: Garantir Open/Closed Principle.

- [ ] **Projeto**: Implementar `RootFinder`.

    ```python
    class RootFinder(NumericalMethod):
        def solve(self, f, interval): ...
    ```

- [ ] **MVC**: Criar Controller que recebe função.

- [ ] **MVC**: Criar Model que representa a equação.

- [ ] **MVC**: Criar View que exibe iterações.

**Entregável:**

- [ ] Biblioteca extensível de métodos de raiz
- [ ] Comparador automático de convergência

## 🔹 MÓDULO 3 — Sistemas Lineares e Não Lineares

**Objetivo:** Resolver sistemas de equações lineares e não lineares.

- Checklist

- [ ] **Métodos**: Implementar Eliminação de Gauss.
- [ ] **Métodos**: Implementar Decomposição LU.
- [ ] **Métodos**: Implementar Gauss-Jacobi.
- [ ] **Métodos**: Implementar Gauss-Seidel.
- [ ] **Métodos**: Implementar Newton para sistemas não lineares.
- [ ] **Engenharia**: Separar estrutura de matriz do algoritmo.
- [ ] **Engenharia**: Garantir imutabilidade onde apropriado.
- [ ] **Projeto**: Implementar `LinearSystemSolver`.

    ```python
    class LinearSystemSolver:
        def solve(self, matrix, vector): ...
    ```

**Entregável:**

- [ ] Motor de resolução matricial
- [ ] Detector automático de dominância diagonal

## 🔹 MÓDULO 4 — Otimização

**Objetivo:** Encontrar mínimos e máximos de funções.

- Checklist

- [ ] **Métodos**: Implementar Gradiente Descendente.
- [ ] **Métodos**: Implementar Método de Newton (Otimização).
- [ ] **Métodos**: Implementar Quase-Newton.
- [ ] **Métodos**: Implementar Busca Unidimensional.
- [ ] **Arquitetura**: Modelar Função Objetivo como entidade.
- [ ] **Arquitetura**: Implementar Otimizador como serviço.
- [ ] **Projeto**: Implementar `Optimizer`.

    ```python
    class Optimizer:
        def minimize(self, function): ...
    ```

**Entregável:**

- [ ] Biblioteca de otimização extensível
- [ ] Sistema de log de convergência

## 🔹 MÓDULO 5 — Regressão, Interpolação e Ajuste

**Objetivo:** Ajustar curvas e interpolar dados.

- Checklist

- [ ] **Métodos**: Implementar Interpolação Polinomial.
- [ ] **Métodos**: Implementar Lagrange.
- [ ] **Métodos**: Implementar Newton (Interpolação).
- [ ] **Métodos**: Implementar Splines.
- [ ] **Métodos**: Implementar Regressão Linear e Não Linear.
- [ ] **Engenharia**: Separar dados do modelo.
- [ ] **Engenharia**: Criar Regressor genérico.
- [ ] **Projeto**: Implementar `RegressionModel`.

    ```python
    class RegressionModel:
        def fit(self, data): ...
    ```

**Entregável:**

- [ ] Engine de ajuste de curvas
- [ ] Avaliação automática de erro

## 🔹 MÓDULO 6 — Integração Numérica

**Objetivo:** Calcular integrais definidas numericamente.

- Checklist

- [ ] **Métodos**: Implementar Regra do Trapézio.
- [ ] **Métodos**: Implementar Regra de Simpson.
- [ ] **Métodos**: Implementar Integração de Romberg.
- [ ] **Métodos**: Implementar Quadratura Gaussiana.
- [ ] **Arquitetura**: Aplicar Strategy e Factory patterns.
- [ ] **Projeto**: Implementar `Integrator`.

    ```python
    class Integrator:
        def integrate(self, f, a, b): ...
    ```

**Entregável:**

- [ ] Sistema de integração adaptativa

## 🔹 MÓDULO 7 — Equações Diferenciais Ordinárias (EDOs)

**Objetivo:** Resolver EDOs.

- Checklist

- [ ] **Métodos**: Implementar Euler.
- [ ] **Métodos**: Implementar Euler Modificado.
- [ ] **Métodos**: Implementar Runge-Kutta.
- [ ] **Métodos**: Implementar Adams-Bashforth.
- [ ] **Engenharia**: Separar equação do método numérico.
- [ ] **Engenharia**: Implementar controle de passo adaptativo.
- [ ] **Projeto**: Implementar `ODESolver`.

    ```python
    class ODESolver:
        def solve(self, equation, initial_conditions): ...
    ```

**Entregável:**

- [ ] Solver genérico de EDOs
- [ ] Visualizador de solução

---

## 🔹 MÓDULO 8 — Equações Diferenciais Parciais (EDPs)

**Objetivo:** Resolver EDPs.

- Checklist

- [ ] **Métodos**: Implementar Diferenças Finitas.
- [ ] **Métodos**: Introdução a Elementos Finitos.
- [ ] **Métodos**: Implementar Crank-Nicolson.
- [ ] **Engenharia**: Modelar Grid como entidade.
- [ ] **Engenharia**: Desacoplar Solver.
- [ ] **Projeto**: Implementar `PDESolver`.

    ```python
    class PDESolver:
        def solve(self, grid, equation): ...
    ```

**Entregável:**

- [ ] Simulador numérico 2D

## 📈 Projeto Final

**Objetivo:** Consolidar tudo em uma biblioteca profissional.

- Checklist

- [ ] Definir API pública clara.
- [ ] Escrever documentação completa.
- [ ] Criar Interface de Linha de Comando (CLI).
- [ ] Criar Jupyter Notebooks de exemplo.
- [ ] Revisar conformidade com SOLID (SRP, OCP, LSP, ISP, DIP).
- [ ] Revisar Clean Code (Nomes semânticos, funções pequenas, testes).
- [ ] Garantir cobertura de testes (PyTest).

**Entregável Final:**

- [ ] Numerical Computing Library em Python

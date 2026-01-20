# Numerical Methods PBP

This project applies Problem-Based Learning (PBP) methodology to the problems presented in Steven C. Chapra's "Applied Numerical Methods with MATLAB for Engineers and Scientists" (3rd edition).

## Objective

To implement all problems from the 24 chapters of the book using:

- Object-Oriented Programming (OOP) in Python
- SOLID Principles
- Model-View-Controller (MVC) Architecture
- Clean Code practices

The goal is to treat this not just as solving exercises, but as a **scientific software engineering educational project**.

## Project Structure

The project follows a Domain-Driven Design (DDD) inspired structure within `src/`:

```text
numerical-methods-pbp/
│
├── src/
│   ├── algorithms/       # Numerical implementations (e.g., roots, linear_systems)
│   ├── domain/           # Core domain logic, errors, and entities
│   ├── interfaces/       # Abstract base classes (ABCs)
│   ├── services/         # Application services
│   ├── controllers/      # MVC Controllers
│   ├── views/            # Views
│   ├── tests/            # Unit tests
│   └── main.py           # Entry point
│
├── md/                   # Documentation and Backlogs
├── docs/                 # Reference PDFs
└── notebooks/            # Jupyter notebooks
```

## Prerequisites

- Python 3.12+
- Conda (recommended) or Virtualenv

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd numerical-methods-pbp
   ```

2. Create and activate the environment:

   ```bash
   conda create -n env_numerical_computation_lab python=3.12
   conda activate env_numerical_computation_lab
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt  # If available
   # Or manually:
   pip install pytest numpy matplotlib
   ```

## Running Tests

The project uses `pytest` for testing. **Crucially, tests must be run from the project root** to ensure correct package resolution.

### Run All Tests

```bash
python -m pytest src/tests
```

### Run Specific Test File

```bash
python -m pytest src/tests/test_graphical_method.py
```

### Run Tests with Output

```bash
python -m pytest -s src/tests
```

## Methodology

For each problem (example or exercise), we follow these steps:

1. **Context**: Understand the real-world phenomenon.
2. **Formulation**: Create the `Model`.
3. **Method Choice**: Select the `Solver`.
4. **Implementation**: Write Clean Code + Tests.
5. **Validation**: Compare with analytical solutions or MATLAB results.
6. **Reflection**: Document insights in `reflection.md`.

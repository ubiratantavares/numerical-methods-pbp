function f = derivada_funcao7(x)
    f = (100 .* exp(x) .* x .^4 + 20 .* exp(x) .* x .^2 + exp(x) + 200 .* x )./ ((10 .* x .^2 + 1) .^2);
end
function f = derivada_funcao4(x)
    f = 0.5 .* (10 .* exp(-x) .* sqrt(x) + 1) ./ sqrt(x);
end
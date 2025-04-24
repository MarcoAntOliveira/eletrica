# Conceitos de Engenharia Elétrica

## Elementos Passivos

### Lei de Ohm
- V = R.I
- Potência: P = V.I = I²R = V²/R

### Convenção Passiva
Sempre que a direção da corrente em um elemento passivo na direção da queda de tensão no elemento, use um sinal positivo em qualquer expressão que relacione a tensão com a corrente. Caso contrário, use um sinal negativo.

- Se a potência for positiva, significa que o circuito absorve energia
- Se for negativa, o circuito fornece energia

### Elementos
- Elemento ativo: dispositivo capaz de gerar energia elétrica
- Elemento passivo: dispositivos que não podem gerar energia elétrica

## Divisores

### Divisor de Corrente
```
I₁ = (R₂/(R₁ + R₂)) . I₃
I₂ = (R₁/(R₁ + R₂)) . I₃

Req = (R₁.R₂)/(R₁ + R₂)
```

### Divisor de Tensão
```
V₁ = (R₁/(R₁ + R₂)) . V₃
V₂ = (R₂/(R₁ + R₂)) . V₃
```

## Teorema de Thevenin
- Permite simplificar um circuito complexo em um circuito equivalente mais simples
- O circuito equivalente consiste em uma fonte de tensão em série com uma resistência

## Indutância e Capacitância

### Indutor
```
V = L.dI/dt
W = ½.L.I²
```

### Capacitor
```
I = C.dV/dt
V(t) = (1/C)∫I.dt + V(t₀)
W = ½.C.V²
```

### Associações
Em série:
```
Leq = L₁ + L₂ + ... + Ln
1/Ceq = 1/C₁ + 1/C₂ + ... + 1/Cn
```

Em paralelo:
```
1/Leq = 1/L₁ + 1/L₂ + ... + 1/Ln
Ceq = C₁ + C₂ + ... + Cn
```

## Resposta de Circuitos RC e RL

### Circuito RC
```
V(t) = I₀.R + (V₀ - I₀.R)e^(-t/RC)
```

### Máxima Transferência de Potência
- Ocorre quando Rth = RL
- P(RL) = (RL.Vth²)/(Rth + RL)²
- Condição para máxima potência: dP(RL)/dRL = 0

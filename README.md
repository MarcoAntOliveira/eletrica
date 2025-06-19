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

## Circuitos RL e RC – Resposta Natural

### Circuito RL
- Corrente:
  ```
  i(t) = i(0) * e^{-t/(L/R)}
  ```
- Constante de tempo:
  ```
  \tau = \frac{L}{R}
  ```
- Energia no resistor:
  ```
  W_R(t) = \frac{1}{2} L [i(0)]^2 e^{-t/(L/R)}
  ```
- Potência no resistor:
  ```
  P_R(t) = R [i(0)]^2 e^{-2t/(L/R)}
  ```
- Energia no indutor:
  ```
  W_L(t) = \frac{1}{2} L [i(0)]^2
  ```

### Circuito RC
- Corrente:
  ```
  i_R(t) = \frac{V(0)}{R} e^{-t/(RC)}
  i_C(t) = -\frac{V(0)}{R} e^{-t/(RC)}
  ```
- Tensão:
  ```
  V(t) = V(0) e^{-t/(RC)}
  ```
- Potência no capacitor:
  ```
  P_C(t) = V(t) \cdot i(t) = -\frac{[V(0)]^2}{R} e^{-2t/(RC)}
  ```

---

## Resposta de Circuito RLC

- Equação diferencial:
  ```
  C \frac{d^2v(t)}{dt^2} + \frac{1}{R} \frac{dv(t)}{dt} + \frac{1}{L} v(t) = 0
  ```
- Solução geral:
  ```
  v(t) = A e^{s_1 t} + B e^{s_2 t}
  ```
  Onde:
  ```
  s_1, s_2 = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}
  \alpha = \frac{1}{2RC}
  \omega_0^2 = \frac{1}{LC}
  ```
- Condição de subamortecimento:
  ```
  \omega_d = \sqrt{\omega_0^2 - \alpha^2}
  s_1 = -\alpha + j\omega_d
  s_2 = -\alpha - j\omega_d
  ```

---

## Exemplo de Análise de Circuito

- Aplicação de Leis de Kirchhoff para encontrar correntes e tensões em circuitos resistivos.
- Exemplo de resolução:
  ```
  Va - 50 + \frac{Va}{10} + \frac{Va}{40} = 3 + 10
  Va(\frac{1}{5} + \frac{1}{10} + \frac{1}{40}) = 13
  Va = \frac{13}{0,325} = 40V
  ```
- Cálculo de correntes:
  ```
  Ia = \frac{40 - 50}{5} = -2A
  Ib = \frac{40}{10} = 4A
  Ic = \frac{40}{40} = 1A
  ```
### Circuitos Trifásicos
Há apenas duas relações de fase possíveis entre a tensão de fase a e as tensões de fase b e c. Uma das possibilidades é a tensão de fase b estar 120° atrasada em relação à tensão de fase a, caso em que a tensão de fase c deve estar 120° adiantada em relação à tensão de fase a. Essa relação entre fases é conhecida como sequência de fase abc (ou positiva). Outra possibilidade é a tensão de fase b estar 120° adiantada em relação à tensão de fase a, caso em que a tensão de fase c deve estar 120° atrasada em relação à tensão de fase a. Essa relação é conhecida como sequência de fase acb (ou negativa). Em notação fasorial, os dois conjuntos possíveis de tensões de fase equilibradas são


$$
V_a  = V_m \angle {0 ^{\circ}}$$
$$V_b  = V_m \angle { -120 ^{\circ}}$$
$$V_c  = V_m \angle +120 ^{\circ}
$$

$$V_a  = V_m \angle {  0 ^{\circ}}
$$
$$V_b  = V_m \angle {+120 ^{\circ}}
$$

$$V_c  = V_m \angle -120 ^{\circ}
$$

ar em paralelo se tiverem a mesma sequência de fases. Outra característica importante de um conjunto de tensões trifásicas equilibradas é que a soma das três tensões é igual a zero. Assim, pelas equações 11.1 ou pelas equações 11.2, $V_a + V_b + V_c = 0.$
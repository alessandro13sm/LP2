# Atividade Avaliativa 02 - Parte 2
### Dupla: Alessandro da Silva Moreira e Yuri Miguel Pinto
### Turma: 2º Informática

---

# 1. O que é uma função de hash e por que não é possível transformar o hash de volta na senha?

Uma função de hash é um algoritmo matemático que recebe uma entrada de qualquer tamanho e devolve uma saída de tamanho fixo.
Não é possível "desfazer" o hash para recuperar a senha original porque a função é **unidirecional**.

---

# 2. O que é o salt e que problema ele resolve?^

O *salt* é um valor aleatório e único gerado a cada nova senha criada ou atualizada e combinado à senha antes de calcular o hash.
Ele resolve senhas iguais com hashes diferentes e ataques com tabelas pré-calculadas

---

# 3. Por que o salt pode ficar gravado no banco, ao lado do hash, sem ser segredo?

O *salt* não precisa ser secreto porque a segurança do sistema **não depende de esconder** o *salt*,
mas sim da imprevisibilidade da senha do usuário, da unidade do *salt* por registro e do custo computacional do algoritmo de hash.

---

![imagem legal!](https://i.postimg.cc/mDHq3bp2/imagem.jpg)

# -*- coding: utf-8 -*-

import hashlib
import hmac
import secrets
from conexao import conectar

ITERACOES_PBKDF2 = 100000
TAMANHO_SALT_BYTES = 16

def calcular_hash_pbkdf2(senha, salt_hex):
   senha_bytes = senha.encode('utf-8')
   salt_bytes = bytes.fromhex(salt_hex)
   hash_bytes = hashlib.pbkdf2_hmac(
      "sha256",
      senha_bytes,
      salt_bytes,
      ITERACOES_PBKDF2,
   )

   return hash_bytes.hex()

def preparar_senha(senha):
   """PROVISÓRIO: devolve (senha_hash, salt) para gravar no banco. """

   salt_hex = secrets.token_hex(TAMANHO_SALT_BYTES)
   senha_hash = calcular_hash_pbkdf2(senha, salt_hex)
   return senha_hash, salt_hex

def verificar_login(login, senha):
    if not login or not senha:
        return None

    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
           "SELECT nome, senha_hash, salt FROM usuario WHERE login = %s",
           (login,),
        )
        registro = cursor.fetchone()

    if not registro:
        return None
    
    nome, senha_hash_banco, salt_banco = registro
    if not senha_hash_banco or not salt_banco or len(salt_banco) != 32:
        return None

    try:
        hash_calculado = calcular_hash_pbkdf2(senha, salt_banco)
    except ValueError:
        return None

    if hmac.compare_digest(hash_calculado, senha_hash_banco):
        return nome
    return None


def listar():
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("SELECT id, nome, login FROM usuario ORDER BY nome")
       return cursor.fetchall()

def inserir(nome, login, senha):
   senha_hash, salt = preparar_senha(senha)
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("INSERT INTO usuario (nome, login, senha_hash, salt) VALUES (%s, %s, %s, %s)",
                      (nome, login, senha_hash, salt))
       conexao.commit()

def atualizar(id_usuario, nome, login, senha):
   senha_hash, salt = preparar_senha(senha)
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("UPDATE usuario SET nome = %s, login = %s, senha_hash = %s, salt = %s WHERE id = %s",
                      (nome, login, senha_hash, salt, id_usuario))
       conexao.commit()

def excluir(id_usuario):
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("DELETE FROM usuario WHERE id = %s", (id_usuario,))
       conexao.commit()

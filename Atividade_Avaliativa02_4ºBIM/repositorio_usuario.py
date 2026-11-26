# -*- coding: utf-8 -*-

import hashlib
import secrets
from conexao import conectar

def preparar_senha(senha):
   """PROVISÓRIO: devolve (senha_hash, salt) para gravar no banco. """

   salt_bytes = secrets.token_bytes(16)
   salt = salt_bytes.hex()

   senha_bytes = senha.encode('utf-8')
   salt_hash_bytes = salt.encode('utf-8')
   iteracoes = 100000

   hash_bytes = hashlib.pbkdf2_hmac(
      'sha256',
      senha_bytes,
      salt_hash_bytes,
      iteracoes
   )

   senha_hash = hash_bytes.hex()

   return senha_hash, salt

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

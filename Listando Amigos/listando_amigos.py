def melhores_amigos(amigos):
  quantidade = len(amigos)
  return quantidade 

def amizades(quantidade):
  if quantidade >= 10:
    print('Nossa, você tem muitos amigos')
  elif quantidade == 1:
    print('Você vai conseguir fazer mais')
  else:
    print('O que importa não é a quantidade e sim a qualidade')

amigos = ['Lucas', 'Vini', 'Yann', 'Gabriel', 'Caio', 'Dio', 'Carlos', 'Pedro', 'João']
quantidade = melhores_amigos(amigos)
amizades(quantidade)

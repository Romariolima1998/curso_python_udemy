# copy, sorted, produtos.sort
import copy

# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda

#produtos_corridos = []
#for indice,lista in enumerate(produtos):
 #   produtos_corridos.append(lista)
 #   produtos_corridos[indice]['preco'] = produtos[indice]['preco'] * 1.10

#jeitoo certo
produtos_corrigidos = [
    {**p,'preco':round(p['preco'] * 1.1,2)}
     for p in copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produto_ordenado_por_nome = sorted(copy.deepcopy(produtos_corrigidos),key=lambda b: b['nome'], reverse=True )
print (*produto_ordenado_por_nome, sep='\n')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produto_ordenado_por_preco = sorted(copy.deepcopy(produtos_corrigidos),key=lambda b: b['preco'] )

print (*produto_ordenado_por_preco, sep='\n')
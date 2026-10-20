
from src.pedidos import *

if __name__ == "__main__":
    print(processar_pedido([{'sku':'LIVRO','preco_centavos':4000,'quantidade':2}], {'LIVRO':5}))
    # {'subtotal_centavos':8000, 'desconto_centavos':0, 'frete_centavos':1500, 'total_centavos':9500}

    print(processar_pedido([{'sku':'FONE','preco_centavos':8000,'quantidade':2}], {'FONE':2}, 10))
    # {'subtotal_centavos':16000, 'desconto_centavos':1600, 'frete_centavos':1500, 'total_centavos':15900}

    # try: 
    #     processar_pedido(
    #         [{'sku':'CABO','preco_centavos':1000,'quantidade':2},
    #         {'sku':'CABO','preco_centavos':1000,'quantidade':2}],
    #         {'CABO':3}
    #     )
    # except Exception as E:
    #     print(f"Exception: {E}")
    # # ValueError (estoque insuficiente)


import horizon
horizon.PoolManager.add_pool("pool")
print("added pools")
for k,v in horizon.PoolManager.get_pools().items() :
	print(k,v)

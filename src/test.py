import settings

print(settings.mongo_client.pos.productos.find_one())

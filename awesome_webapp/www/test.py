import orm,asyncio
from model import User,Blog,Comment
async def test(loop):
    await orm.create_pool(loop=loop,user='root',password='123456',database='awesome')
    u=User(name='Test',email='test@sina.com',passwd='123456',image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop)) 
loop.close()
print('end')






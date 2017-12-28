import orm, asyncio
from model import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='root',password='123456',database='awesome')
    u=User(name='Test',email='test@sina.com',passwd='123456',image='about:blank')
    await u.save()

async  def test_find(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', database='awesome')
    user = await User.find('test@sina.com')
    print(user)

async def test_findAll(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', database='awesome')
    user = await User.findAll()
    for u in user:
        print(u.email)
    await orm.destroy_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_findAll(loop))
loop.close()






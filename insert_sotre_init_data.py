from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, StoreItem

engine = create_engine('sqlite:///store.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ##################################################


duckStore = Store(name="매일 덕")

session.add(duckStore)
session.commit()

duckSmoke = StoreItem(name="훈제오리",
                      description="유황먹은 오리요리",
                      price="33,000",
                      package_item="정식",
                      store=duckStore)

session.add(duckSmoke)
session.commit()

duckSoup = StoreItem(name="한방오리백숙",
                     description="한방재료와 진한국물 오리요리",
                     price="44,000",
                     package_item="정식",
                     store=duckStore)

session.add(duckSoup)
session.commit()

duckSalt = StoreItem(name="소금오리구이",
                     description="탄력있는 오리요리",
                     price="26,000",
                     package_item="정식",
                     store=duckStore)

session.add(duckSalt)
session.commit()

duckRoast = StoreItem(name="로스오리구이",
                      description="구운 오리요리",
                      price="22,000",
                      package_item="정식",
                      store=duckStore)

session.add(duckRoast)
session.commit()

iceCream = StoreItem(name="연꽃 아이스크림",
                      description="녹차맛과 유사",
                      price="3,000",
                      package_item="디저트",
                      store=duckStore)

session.add(iceCream)
session.commit()

# ##################################################


cookieStore = Store(name="세이 쿠키")

session.add(cookieStore)
session.commit()


cheeseCake = StoreItem(name="치즈 케이크",
                          description="치즈를 넣어 구운 케이크",
                          price="25,500",
                          package_item="디저트",
                          store=cookieStore)

session.add(cheeseCake)
session.commit()


pumpkinCookie = StoreItem(name="단호박 비건 쿠키",
                          description="단호박과 호밀",
                          price="2,500",
                          package_item="디저트",
                          store=cookieStore)

session.add(pumpkinCookie)
session.commit()


chocolateCookie = StoreItem(name="초코 쿠키",
                          description="달콤한 초코 쿠키",
                          price="2,000",
                          package_item="디저트",
                          store=cookieStore)

session.add(chocolateCookie)
session.commit()


greenTeaCookie = StoreItem(name="녹차 쿠키",
                          description="쌉사름한 녹차 쿠키",
                          price="3,000",
                          package_item="디저트",
                          store=cookieStore)

session.add(chocolateCookie)
session.commit()



americano = StoreItem(name="아메리카노",
                          description="기본 아메리카노",
                          price="3,000",
                          package_item="디저트",
                          store=cookieStore)

session.add(americano)
session.commit()


print('Done')

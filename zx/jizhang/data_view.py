# coding：utf-8
__author__ = 'Administrator'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from jizhang.models import *


class InitView(APIView):
	debug = True
	def post(self, request, format=None):
		'''
		初始化城市数据
		'''
		province = [ (10,'北京','1','1'),(11,'上海','1','1'),(12,'天津','1','1'),(13,'重庆','1','1'),(14,'河北','2','1'),(15,'山西','2','1'),(16,'内蒙古','3','1'),(17,'辽宁','2','1'),(18,'吉林','2','1'),(19,'黑龙江','2','1'),(20,'江苏','2','1'),(21,'浙江','2','1'),(22,'安徽','2','1'),(23,'福建','2','1'),(24,'江西','2','1'),(25,'山东','2','1'),(26,'河南','2','1'),(27,'湖北','2','1'),(28,'湖南','2','1'),(29,'广东','2','1'),(30,'广西','3','1'),(31,'海南','2','1'),(32,'四川','2','1'),(33,'贵州','2','1'),(34,'云南','2','1'),(35,'西藏','3','1'),(36,'陕西','2','1'),(37,'甘肃','2','1'),(38,'青海','2','1'),(39,'宁夏','3','1'),(40,'新疆','3','1'),(41,'香港','4','1'),(42,'澳门','4','1'),(43,'台湾','2','1')]
		city = [(1000,'北京',10,'1'),(1018,'上海',11,'1'),(1037,'天津',12,'1'),(1055,'重庆',13,'1'),(1095,'石家庄',14,'1'),(1096,'唐山',14,'1'),(1097,'秦皇岛',14,'1'),(1098,'邯郸',14,'1'),(1099,'邢台',14,'1'),(1100,'保定',14,'1'),(1101,'张家口',14,'1'),(1102,'承德',14,'1'),(1103,'沧州',14,'1'),(1104,'廊坊',14,'1'),(1105,'衡水',14,'1'),(1106,'太原',15,'1'),(1107,'大同',15,'1'),(1108,'阳泉',15,'1'),(1109,'长治',15,'1'),(1110,'晋城',15,'1'),(1111,'朔州',15,'1'),(1112,'晋中',15,'1'),(1113,'运城',15,'1'),(1114,'忻州',15,'1'),(1115,'临汾',15,'1'),(1116,'吕梁',15,'1'),(1117,'呼和浩特',16,'1'),(1118,'包头',16,'1'),(1119,'乌海',16,'1'),(1120,'赤峰',16,'1'),(1121,'通辽',16,'1'),(1122,'鄂尔多斯',16,'1'),(1123,'呼伦贝尔',16,'1'),(1124,'乌兰察布',16,'1'),(1125,'锡林郭勒盟',16,'1'),(1126,'巴彦淖尔',16,'1'),(1127,'阿拉善盟',16,'1'),(1128,'兴安盟',16,'1'),(1129,'沈阳',17,'1'),(1130,'大连',17,'1'),(1131,'鞍山',17,'1'),(1132,'抚顺',17,'1'),(1133,'本溪',17,'1'),(1134,'丹东',17,'1'),(1135,'锦州',17,'1'),(1136,'葫芦岛',17,'1'),(1137,'营口',17,'1'),(1138,'盘锦',17,'1'),(1139,'阜新',17,'1'),(1140,'辽阳',17,'1'),(1141,'铁岭',17,'1'),(1142,'朝阳',17,'1'),(1143,'长春',18,'1'),(1144,'吉林',18,'1'),(1145,'四平',18,'1'),(1146,'辽源',18,'1'),(1147,'通化',18,'1'),(1148,'白山',18,'1'),(1149,'松原',18,'1'),(1150,'白城',18,'1'),(1151,'延边朝鲜',18,'1'),(1152,'哈尔滨',19,'1'),(1153,'齐齐哈尔',19,'1'),(1154,'鹤岗',19,'1'),(1155,'双鸭山',19,'1'),(1156,'鸡西',19,'1'),(1157,'大庆',19,'1'),(1158,'伊春',19,'1'),(1159,'牡丹江',19,'1'),(1160,'佳木斯',19,'1'),(1161,'七台河',19,'1'),(1162,'黑河',19,'1'),(1163,'绥化',19,'1'),(1164,'大兴安岭',19,'1'),(1165,'南京',20,'1'),(1166,'无锡',20,'1'),(1167,'徐州',20,'1'),(1168,'常州',20,'1'),(1169,'苏州',20,'1'),(1170,'南通',20,'1'),(1171,'连云港',20,'1'),(1172,'淮安',20,'1'),(1173,'盐城',20,'1'),(1174,'扬州',20,'1'),(1175,'镇江',20,'1'),(1176,'泰州',20,'1'),(1177,'宿迁',20,'1'),(1178,'杭州',21,'1'),(1179,'宁波',21,'1'),(1180,'温州',21,'1'),(1181,'嘉兴',21,'1'),(1182,'湖州',21,'1'),(1183,'绍兴',21,'1'),(1184,'金华',21,'1'),(1185,'衢州',21,'1'),(1186,'舟山',21,'1'),(1187,'台州',21,'1'),(1188,'丽水',21,'1'),(1189,'合肥',22,'1'),(1190,'芜湖',22,'1'),(1191,'蚌埠',22,'1'),(1192,'淮南',22,'1'),(1193,'马鞍山',22,'1'),(1194,'淮北',22,'1'),(1195,'铜陵',22,'1'),(1196,'安庆',22,'1'),(1197,'黄山',22,'1'),(1198,'滁州',22,'1'),(1199,'阜阳',22,'1'),(1200,'宿州',22,'1'),(1201,'巢湖',22,'1'),(1202,'六安',22,'1'),(1203,'亳州',22,'1'),(1204,'池州',22,'1'),(1205,'宣城',22,'1'),(1206,'福州',23,'1'),(1207,'厦门',23,'1'),(1208,'莆田',23,'1'),(1209,'三明',23,'1'),(1210,'泉州',23,'1'),(1211,'漳州',23,'1'),(1212,'南平',23,'1'),(1213,'龙岩',23,'1'),(1214,'宁德',23,'1'),(1215,'南昌',24,'1'),(1216,'景德镇',24,'1'),(1217,'萍乡',24,'1'),(1218,'新余',24,'1'),(1219,'九江',24,'1'),(1220,'鹰潭',24,'1'),(1221,'赣州',24,'1'),(1222,'吉安',24,'1'),(1223,'宜春',24,'1'),(1224,'抚州',24,'1'),(1225,'上饶',24,'1'),(1226,'济南',25,'1'),(1227,'青岛',25,'1'),(1228,'淄博',25,'1'),(1229,'枣庄',25,'1'),(1230,'东营',25,'1'),(1231,'潍坊',25,'1'),(1232,'烟台',25,'1'),(1233,'威海',25,'1'),(1234,'济宁',25,'1'),(1235,'泰安',25,'1'),(1236,'日照',25,'1'),(1237,'莱芜',25,'1'),(1238,'德州',25,'1'),(1239,'临沂',25,'1'),(1240,'聊城',25,'1'),(1241,'滨州',25,'1'),(1242,'菏泽',25,'1'),(1243,'郑州',26,'1'),(1244,'开封',26,'1'),(1245,'洛阳',26,'1'),(1246,'平顶山',26,'1'),(1247,'焦作',26,'1'),(1248,'鹤壁',26,'1'),(1249,'新乡',26,'1'),(1250,'安阳',26,'1'),(1251,'濮阳',26,'1'),(1252,'许昌',26,'1'),(1253,'漯河',26,'1'),(1254,'三门峡',26,'1'),(1255,'南阳',26,'1'),(1256,'商丘',26,'1'),(1257,'信阳',26,'1'),(1258,'周口',26,'1'),(1259,'驻马店',26,'1'),(1260,'济源',26,'1'),(1261,'武汉',27,'1'),(1262,'黄石',27,'1'),(1263,'襄樊',27,'1'),(1264,'十堰',27,'1'),(1265,'荆州',27,'1'),(1266,'宜昌',27,'1'),(1267,'荆门',27,'1'),(1268,'鄂州',27,'1'),(1269,'孝感',27,'1'),(1270,'黄冈',27,'1'),(1271,'咸宁',27,'1'),(1272,'随州',27,'1'),(1273,'仙桃',27,'1'),(1274,'天门',27,'1'),(1275,'潜江',27,'1'),(1276,'神农架',27,'1'),(1277,'恩施土家',27,'1'),(1278,'长沙',28,'1'),(1279,'株洲',28,'1'),(1280,'湘潭',28,'1'),(1281,'衡阳',28,'1'),(1282,'邵阳',28,'1'),(1283,'岳阳',28,'1'),(1284,'常德',28,'1'),(1285,'张家界',28,'1'),(1286,'益阳',28,'1'),(1287,'郴州',28,'1'),(1288,'怀化',28,'1'),(1289,'娄底',28,'1'),(1290,'湘西土家',28,'1'),(1291,'永州',28,'1'),(1292,'广州',29,'1'),(1293,'深圳',29,'1'),(1294,'珠海',29,'1'),(1295,'汕头',29,'1'),(1296,'韶关',29,'1'),(1297,'佛山',29,'1'),(1298,'江门',29,'1'),(1299,'湛江',29,'1'),(1300,'茂名',29,'1'),(1301,'肇庆',29,'1'),(1302,'惠州',29,'1'),(1303,'梅州',29,'1'),(1304,'汕尾',29,'1'),(1305,'河源',29,'1'),(1306,'阳江',29,'1'),(1307,'清远',29,'1'),(1308,'东莞',29,'1'),(1309,'中山',29,'1'),(1310,'潮州',29,'1'),(1311,'揭阳',29,'1'),(1312,'云浮',29,'1'),(1313,'南宁',30,'1'),(1314,'柳州',30,'1'),(1315,'桂林',30,'1'),(1316,'梧州',30,'1'),(1317,'北海',30,'1'),(1318,'防城港',30,'1'),(1319,'钦州',30,'1'),(1320,'贵港',30,'1'),(1321,'玉林',30,'1'),(1322,'百色',30,'1'),(1323,'贺州',30,'1'),(1324,'河池',30,'1'),(1325,'来宾',30,'1'),(1326,'崇左',30,'1'),(1327,'海口',31,'1'),(1328,'三亚',31,'1'),(1329,'五指山',31,'1'),(1330,'琼海',31,'1'),(1331,'儋州',31,'1'),(1332,'文昌',31,'1'),(1333,'万宁',31,'1'),(1334,'东方',31,'1'),(1335,'澄迈',31,'1'),(1336,'定安',31,'1'),(1337,'屯昌',31,'1'),(1338,'临高',31,'1'),(1339,'白沙黎族',31,'1'),(1340,'江黎族自',31,'1'),(1341,'乐东黎族',31,'1'),(1342,'陵水黎族',31,'1'),(1343,'保亭黎族',31,'1'),(1344,'琼中黎族',31,'1'),(1345,'西沙群岛',31,'1'),(1346,'南沙群岛',31,'1'),(1347,'中沙群岛',31,'1'),(1348,'成都',32,'1'),(1349,'自贡',32,'1'),(1350,'攀枝花',32,'1'),(1351,'泸州',32,'1'),(1352,'德阳',32,'1'),(1353,'绵阳',32,'1'),(1354,'广元',32,'1'),(1355,'遂宁',32,'1'),(1356,'内江',32,'1'),(1357,'乐山',32,'1'),(1358,'南充',32,'1'),(1359,'宜宾',32,'1'),(1360,'广安',32,'1'),(1361,'达州',32,'1'),(1362,'眉山',32,'1'),(1363,'雅安',32,'1'),(1364,'巴中',32,'1'),(1365,'资阳',32,'1'),(1366,'阿坝藏族',32,'1'),(1367,'甘孜藏族',32,'1'),(1368,'凉山彝族',32,'1'),(1369,'贵阳',33,'1'),(1370,'六盘水',33,'1'),(1371,'遵义',33,'1'),(1372,'安顺',33,'1'),(1373,'铜仁',33,'1'),(1374,'毕节',33,'1'),(1375,'黔西南布',33,'1'),(1376,'黔东南苗',33,'1'),(1377,'黔南布依',33,'1'),(1378,'昆明',34,'1'),(1379,'曲靖',34,'1'),(1380,'玉溪',34,'1'),(1381,'保山',34,'1'),(1382,'昭通',34,'1'),(1383,'丽江',34,'1'),(1384,'思茅',34,'1'),(1385,'临沧',34,'1'),(1386,'文山壮族',34,'1'),(1387,'红河哈尼',34,'1'),(1388,'西双版纳',34,'1'),(1389,'楚雄彝族',34,'1'),(1390,'大理白族',34,'1'),(1391,'德宏傣族',34,'1'),(1392,'怒江傈傈',34,'1'),(1393,'迪庆藏族',34,'1'),(1394,'拉萨',35,'1'),(1395,'那曲',35,'1'),(1396,'昌都',35,'1'),(1397,'山南',35,'1'),(1398,'日喀则',35,'1'),(1399,'阿里',35,'1'),(1400,'林芝',35,'1'),(1401,'西安',36,'1'),(1402,'铜川',36,'1'),(1403,'宝鸡',36,'1'),(1404,'咸阳',36,'1'),(1405,'渭南',36,'1'),(1406,'延安',36,'1'),(1407,'汉中',36,'1'),(1408,'榆林',36,'1'),(1409,'安康',36,'1'),(1410,'商洛',36,'1'),(1411,'兰州',37,'1'),(1412,'金昌',37,'1'),(1413,'白银',37,'1'),(1414,'天水',37,'1'),(1415,'嘉峪关',37,'1'),(1416,'武威',37,'1'),(1417,'张掖',37,'1'),(1418,'平凉',37,'1'),(1419,'酒泉',37,'1'),(1420,'庆阳',37,'1'),(1421,'定西',37,'1'),(1422,'陇南',37,'1'),(1423,'临夏回族',37,'1'),(1424,'甘南藏族',37,'1'),(1425,'西宁',38,'1'),(1426,'海东',38,'1'),(1427,'海北藏族',38,'1'),(1428,'黄南藏族',38,'1'),(1429,'海南藏族',38,'1'),(1430,'果洛藏族',38,'1'),(1431,'玉树藏族',38,'1'),(1432,'海西蒙古',38,'1'),(1433,'银川',39,'1'),(1434,'石嘴山',39,'1'),(1435,'吴忠',39,'1'),(1436,'固原',39,'1'),(1437,'中卫',39,'1'),(1438,'乌鲁木齐',40,'1'),(1439,'克拉玛依',40,'1'),(1440,'石河子',40,'1'),(1441,'阿拉尔',40,'1'),(1442,'图木舒克',40,'1'),(1443,'五家渠',40,'1'),(1444,'吐鲁番',40,'1'),(1445,'哈密',40,'1'),(1446,'和田',40,'1'),(1447,'阿克苏',40,'1'),(1448,'喀什',40,'1'),(1449,'克孜勒苏',40,'1'),(1450,'巴音郭楞',40,'1'),(1451,'昌吉回族',40,'1'),(1452,'博尔塔拉',40,'1'),(1453,'伊犁哈萨',40,'1'),(1454,'塔城',40,'1'),(1455,'阿勒泰',40,'1'),(1456,'台北',43,'1'),(1457,'高雄',43,'1'),(1458,'基隆',43,'1'),(1459,'台中',43,'1'),(1460,'台南',43,'1'),(1461,'新竹',43,'1'),(1462,'嘉义',43,'1'),(1463,'台北县',43,'1'),(1464,'宜兰县',43,'1'),(1465,'新竹县',43,'1'),(1466,'桃园县',43,'1'),(1467,'苗栗县',43,'1'),(1468,'台中县',43,'1'),(1469,'彰化县',43,'1'),(1470,'南投县',43,'1'),(1471,'嘉义县',43,'1'),(1472,'云林县',43,'1'),(1473,'台南县',43,'1'),(1474,'高雄县',43,'1'),(1475,'屏东县',43,'1'),(1476,'台东县',43,'1'),(1477,'花莲县',43,'1'),(1478,'澎湖县',43,'1')]
		city.append((1000,'beijing',10,'1'))
		Province.objects.all().delete()
		for item in province:
			P = Province(area_code = item[0], name = item[1], state = True)
			P.save()

		City.objects.all().delete()
		for item in city:
			province = Province.objects.get(area_code=item[2])
			City.objects.create(province=province, name=item[1], state=True)

		DecorationCompany.objects.all().delete()
		city = City.objects.get(name='南京')
		DecorationCompany.objects.create(city=city, name='米兰装饰')

		user = User.objects.get(username='zx')
		userprofile = UserProfile.objects.create(user=user, city=city)

		if self.debug:
			Category.objects.all().delete()
			Category.objects.create(name='设计')
			Category.objects.create(name='主材')
			Category.objects.create(name='软装')
			Category.objects.create(name='家电')
			Category.objects.create(name='装修')

			Currency.objects.all().delete()
			Currency.objects.create(name='RMB')

			Brand.objects.all().delete()
			Brand.objects.create(name='西门子')
			Brand.objects.create(name='海尔')
			Brand.objects.create(name='美的')
			Brand.objects.create(name='九阳')
			Brand.objects.create(name='长虹')
			Brand.objects.create(name='格力')
			Brand.objects.create(name='三星')
			Brand.objects.create(name='博世')

			# city = City.objects.get(name='南京')
			Shop.objects.create(city=city, name='金盛国际家具')
			Shop.objects.create(city=city, name='卡子门')
			Shop.objects.create(city=city, name='红太阳装饰城')
			Shop.objects.create(city=city, name='苏宁易购')
			Shop.objects.create(city=city, name='国美')
			Shop.objects.create(city=city, name='苏果超市')
			Shop.objects.create(city=city, name='红星美凯龙卡子门店')
			Shop.objects.create(city=city, name='苏宁乐购仕')
			Shop.objects.create(city=city, name='大洋百货')
			Shop.objects.create(city=city, name='沃尔玛新街口店')
			Shop.objects.create(city=city, name='金鹰江宁店')
			Shop.objects.create(city=city, name='京东商城')


			Tag.objects.all().delete()
			category = Category.objects.get(name='家电')
			Tag.objects.create(category=category, name='洗衣机', cited_times=2414, average_price=2600,
							   min_price=1200, max_price=4500)
			Tag.objects.create(category=category, name='滚筒洗衣机', cited_times=1671, average_price=2700,
							   min_price=1260, max_price=5500)
			Tag.objects.create(category=category, name='西门子洗衣机', cited_times=100, average_price=3000, min_price=1999,
							   max_price=6500)
			Tag.objects.create(category=category, name='空调', cited_times=2178, average_price=3000,
							   min_price=1200, max_price=5500)
			Tag.objects.create(category=category, name='中央空调', cited_times=2840, average_price=25000,
							   min_price=11200, max_price=55500)
			Tag.objects.create(category=category, name='32寸液晶电视尺寸', cited_times=255, average_price=1500,
							   min_price=999, max_price=2500)
			Tag.objects.create(category=category, name='液晶电视', cited_times=1471, average_price=3050,
							   min_price=899, max_price=19500)
			Tag.objects.create(category=category, name='42寸液晶电视尺寸', cited_times=339, average_price=4000,
							   min_price=2500, max_price=9000)
			Tag.objects.create(category=category, name='对开门冰箱', cited_times=640, average_price=5500,
							   min_price=3300, max_price=8000)
			Tag.objects.create(category=category, name='豆浆机', cited_times=1430, average_price=400,
							   min_price=155, max_price=600)
			Tag.objects.create(category=category, name='电饭煲', cited_times=1507, average_price=200,
							   min_price=80, max_price=360)

			BrandDataWithCityTag.objects.all().delete()
			ShopDataWithCityTag.objects.all().delete()

			tag = Tag.objects.get(name='洗衣机')
			brand = Brand.objects.get(name='博世')
			cited_time = 2334
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='红太阳装饰城')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2322)

			tag = Tag.objects.get(name='洗衣机')
			brand = Brand.objects.get(name='西门子')
			cited_time = 2554
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁易购')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='洗衣机')
			brand = Brand.objects.get(name='三星')
			cited_time = 2500
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='金鹰江宁店')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1985)

			tag = Tag.objects.get(name='洗衣机')
			brand = Brand.objects.get(name='海尔')
			cited_time = 1233
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='大洋百货')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1985)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2333)
			shop = Shop.objects.get(name='国美')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1224)
			shop = Shop.objects.get(name='金鹰江宁店')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2121)
			shop = Shop.objects.get(name='金盛国际家具')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2222)
			shop = Shop.objects.get(name='京东商城')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1211)
			shop = Shop.objects.get(name='红星美凯龙卡子门店')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=32)


			tag = Tag.objects.get(name='液晶电视')
			brand = Brand.objects.get(name='海尔')
			cited_time = 1333
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2542)

			tag = Tag.objects.get(name='电饭煲')
			brand = Brand.objects.get(name='九阳')
			cited_time = 2551
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='滚筒洗衣机')
			brand = Brand.objects.get(name='西门子')
			cited_time = 3235
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='对开门冰箱')
			brand = Brand.objects.get(name='海尔')
			cited_time = 1998
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁易购')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='对开门冰箱')
			brand = Brand.objects.get(name='博世')
			cited_time = 1055
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='对开门冰箱')
			brand = Brand.objects.get(name='西门子')
			cited_time = 3636
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='苏宁乐购仕')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

			tag = Tag.objects.get(name='电饭煲')
			brand = Brand.objects.get(name='美的')
			cited_time = 1995
			BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
			shop = Shop.objects.get(name='沃尔玛新街口店')
			ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		return Response({'result': 'init data ok'}, status=status.HTTP_201_CREATED)

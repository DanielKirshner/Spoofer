from typing import List

VENDORS: List[str] = [ 
    'Total Random', 
    'Samsung', 
    'Apple', 
    'Intel', 
    'Microsoft', 
    'Huawei', 
    'Google', 
    'Cisco']

SAMSUNG_VENDORS: List[str] = [
    '00:21:19', '00:02:78', '00:07:ab', '00:09:18', '00:0d:ae', '00:0d:e5', '00:12:47', '00:12:fb',
    '00:13:77', '00:15:99', 'e8:50:8b', 'e8:6d:cb', 'e8:7f:6b', 'e8:93:09', 'e8:b4:c8', 'e8:e5:d6',
    'ec:10:7b', 'ec:1f:72', 'ec:7c:b6', 'ec:9b:f3', 'ec:aa:25', 'ec:e0:9b', 'f0:08:f1', 'f0:25:b7',
    'f0:39:65', 'f0:5a:09', 'f0:5b:7b', 'f0:65:ae', 'f0:6b:ca', 'f0:70:4f', 'f0:72:8c', 'dc:89:83',
    'dc:cc:e6', 'dc:cf:96', 'dc:dc:e2', 'dc:f7:56', 'e0:03:6b', 'e0:99:71', 'e0:9d:13', 'e0:aa:96',
    '78:00:9e', '78:1f:db', '78:23:27', '78:25:ad', '78:37:16', '78:40:e4', '78:46:d4', '78:47:1d'
]

APPLE_VENDORS: List[str] = [
    'f8:10:93', 'f8:1e:df', 'f8:27:93', 'f8:2d:7c', 'f8:38:80', 'f8:4d:89', 'f8:4e:73', 'f8:62:14',
    'f8:66:5a', 'f8:6f:c1', 'e4:b2:fb', 'e4:c6:3d', 'e4:ce:8f', 'e4:e0:a6', 'e4:e4:ab', 'e8:04:0b',
    'e8:06:88', 'e8:1c:d8', 'e8:36:17', 'e8:5f:02', 'e8:78:65', 'e8:7f:95', 'e8:80:2e', 'e8:81:52',
    'd8:cf:9c', 'd8:d1:cb', 'd8:dc:40', 'd8:de:3a', 'dc:08:0f', 'dc:0c:5c', 'dc:2b:2a', 'dc:2b:61',
    'dc:37:14', 'dc:41:5f', 'dc:52:85', 'dc:53:92', 'dc:56:e7', 'dc:80:84', 'dc:86:d8', 'dc:9b:9c',
    '5c:97:f3', '5c:ad:cf', '5c:e9:1e', '5c:f5:da', '5c:f7:e6', '5c:f9:38', '60:03:08', '60:06:e3'
]

INTEL_VENDORS: List[str] = [
    '00:d7:6d', '00:db:df', '00:e1:8c', '04:33:c2', '04:56:e5', '04:6c:59', '04:cf:4b', '04:d3:b0',
    '04:e8:b9', '04:ea:56', '04:ec:d8', '04:ed:33', '08:11:96', '08:5b:d6', '08:6a:c5', '08:71:90',
    '08:8e:90', '08:9d:f4', '08:d2:3e', '08:d4:0c', '0c:54:15', '0c:7a:15', '0c:8b:fd', '0c:91:92',
    '0c:9a:3c', '0c:d2:92', '0c:dd:24', '48:45:20', '48:51:b7', '48:51:c5', '48:68:4a', '48:89:e7',
    '48:a4:72', '48:ad:9a', '48:f1:7f', '4c:03:4f', '4c:1d:96', '4c:34:88', '4c:44:5b', '4c:77:cb',
    '4c:79:6e', 'cc:d9:ac', 'cc:f9:e4', 'd0:3c:1f', 'd0:57:7b', 'd0:7e:35', 'd0:ab:d5', 'd0:c6:37'
]

MICROSOFT_VENDORS: List[str] = [
    '00:03:ff', '00:22:48', '04:27:28', '00:25:ae', '00:12:5a', '00:15:5d', '00:17:fa', '00:1d:d8',
    '0c:41:3e', '0c:e7:25', '10:2f:6b', '14:9a:10', '14:cb:65', '1c:1a:df', '20:62:74', '20:a9:9b',
    '3c:83:75', '44:16:22', '48:50:73', '48:86:e8', '4c:3b:df', '5c:ba:37', '6c:5d:3a', '70:bc:10',
    '84:57:33', '84:63:d6', '90:6a:eb', '94:9a:a9', '98:5f:d3', '98:7a:14', '9c:6c:15', '9c:aa:1b',
    'a8:8c:3e', 'b8:31:b5', 'b8:4f:d5', 'bc:83:85', 'c4:9d:ed', 'c8:3f:26', 'c8:96:65', 'ca:12:5c',
    'd4:8f:33', 'd8:e2:df', 'dc:98:40', 'e4:2a:ac', 'e8:a7:2f', 'ec:59:e7', 'ec:83:50', 'f0:1d:bc',
]

HUAWEI_VENDOR: List[str] = [
    '00:18:82', '00:34:fe', '00:66:4b', '00:e0:fc', '04:25:c5', '04:75:03', '04:b0:e7', '04:e7:95',
    '08:19:a6', '08:63:61', '08:c0:21', '0c:31:dc', '0c:70:4a', '0c:c6:cc', '10:32:1d', '10:a4:da',
    '14:09:dc', '14:46:58', '14:89:cb', '14:ab:02', '18:02:2d', '18:cf:24', '1c:1d:67', '1c:59:9b',
    '1c:a6:81', '20:08:ed', '20:53:83', '20:a6:80', '20:f3:a3', '24:26:d6', '24:4c:07', '24:9e:ab',
    '24:df:6a', '28:17:09', '28:53:4e', '28:a6:db', '28:fb:ae', '2c:55:d3', '2c:ab:00', '30:74:96',
    '30:e9:8e', '34:0a:98', '34:58:40', '34:b3:54', '38:4c:4f', '38:f8:89', '3c:54:47', '3c:9d:56',
]

GOOGLE_VENDORS: List[str] = [
    '00:1a:11', '00:f6:20', '08:9e:08', '14:22:3b', '08:b4:b1', '1c:f2:9a', '20:1f:3b', '20:df:b9',
    '24:05:88', '24:29:34', '28:bd:89', '30:fd:38', '38:86:f7', '38:8b:59', '3c:28:6d', '3c:5a:b4',
    '3c:8d:20', '44:07:0b', '44:bb:3b', '48:d6:d5', '54:60:09', '58:24:29', '58:cb:52', '60:b7:6e',
    '70:3a:cb', '74:74:46', '7c:2e:bd', '7c:d9:5c', '88:3d:24', '88:54:1f', '90:0c:c8', '90:ca:fa',
    '94:eb:2c', '98:d2:93', '9c:4f:5f', 'a4:77:33', 'ac:67:84', 'b0:2a:43', 'b0:6a:41', 'b0:e4:d5',
    'd8:eb:46', 'da:a1:19', 'dc:e5:5b', 'e4:5e:1b', 'e4:f0:42', 'f0:5c:77', 'f0:72:ea', 'f0:ef:86',
]

CISCO_VENDORS: List[str] = [
    '08:ec:f5', '08:f3:fb', '0c:11:67', '0c:27:24', '0c:68:03', '0c:75:bd', '0c:85:25', '0c:d0:f8',
    '10:06:ed', '10:8c:cf', '10:b3:c6', '10:b3:d5', '10:b3:d6', '10:bd:18', '10:f3:11', '10:f9:20',
    '14:16:9d', '14:a2:a0', '18:33:9d', '18:59:f5', '18:80:90', '18:8b:45', '18:8b:9d', '18:9c:5d',
    '18:e7:28', '18:ef:63', '1c:17:d3', '1c:1d:86', '1c:6a:7a', '1c:aa:07', '1c:d1:e0', '1c:de:a7',
    '1c:e8:5d', '20:37:06', '20:3a:07', '20:4c:9e', '20:bb:c0', '20:cf:ae', '24:01:c7', '24:16:9d',
    '24:7e:12', '24:81:3b', '24:b6:57', '24:e9:b3', '24:36:da', '28:34:a2', '28:52:61', '28:6f:7f',
]
class FlaskConfig:
    # APScheduler
    SCHEDULER_API_ENABLED = True

class BaseConfig:
    proxies = {
        "http": "socks5://127.0.0.1:10808",
        "https": "socks5://127.0.0.1:10808"
    }


class BinanceConfig:
    api_key = ""
    api_secret = ""
    markets = ["BNB", "BTC", "ETH", "TRX", "XRP", "USDT", "PAX", "TUSD", "USDC", "BUSD", "USDS"]
    whitelist_BNB = ["XRPBNB", "EOSBNB", "TRXBNB", "KAVABNB", "LTCBNB", "VETBNB", "BTTBNB", "ALGOBNB", "NEOBNB","XLMBNB","XMRBNB","ADABNB", "WINBNB", "ARPABNB", "WANBNB", "FTMBNB", "ATOMBNB", "BATBNB","ONEBNB", "IOTABNB","MATICBNB","ERDBNB", "RLCBNB", "MCOBNB", "STXBNB", "ZILBNB", "CHZBNB","XTZBNB", "NASBNB", "ETCBNB", "HOTBNB","RVNBNB","ENJBNB", "FETBNB", "TOMOBNB", "ONTBNB","ICXBNB", "PERLBNB", "ZRXBNB", "DOGEBNB", "THETABNB","RENBNB","DASHBNB", "BLZBNB", "CELRBNB","TFUELBNB", "AIONBNB", "QTUMBNB", "ZENBNB", "ZECBNB", "DUSKBNB","XEMBNB","AGIBNB", "MFTBNB", "SKYBNB", "IOSTBNB", "NXSBNB", "WABIBNB", "BRDBNB", "NKNBNB", "MITHBNB","NANOBNB","STORMBNB", "BEAMBNB", "SCBNB", "COCOSBNB", "YOYOBNB", "HBARBNB", "WABIBNB", "BRDBNB", "NKNBNB","MITHBNB","NANOBNB", "STORMBNB", "BEAMBNB", "SCBNB", "COCOSBNB", "YOYOBNB", "HBARBNB", "WAVESBNB","PHBBNB","BANDBNB","DCRBNB", "DLTBNB", "ANKRBNB", "LSKBNB", "POLYBNB", "OMGBNB", "GTOBNB", "COSBNB", "CNDBNB","AEBNB","RDNBNB","GOBNB", "NULSBNB", "QSPBNB", "XZCBNB", "OSTBNB", "POABNB", "APPCBNB", "PIVXBNB", "WTCBNB","VIABNB","NEBLBNB", "POWRBNB", "STEEMBNB", "AMBBNB", "RCNBNB", "LOOMBNB", "ONGBNB", "BCPTBNB", "CMTBNB","QLCBNB","GNTBNB", "SYSBNB", "ARDRBNB", "ADXBNB"]
    whitelist_USDT = ["BTCUSDT", "ETHUSDT", "EOSUSDT", "BNBUSDT", "BCHABCUSDT", "XRPUSDT", "LTCUSDT", "VETUSDT","BTCUSDC","TRXUSDT", "LINKUSDT", "BTCNGN", "MCOUSDT", "NEOUSDT", "USDCUSDT", "ADAUSDT", "XLMUSDT", "BTCPAX", "BTCTUSD", "BTTUSDT", "IOSTUSDT", "ETCUSDT", "ONTUSDT", "BUSDNGN", "ATOMUSDT", "KAVAUSDT", "MATICUSDT", "TUSDUSDT", "FETUSDT", "BNBNGN", "QTUMUSDT", "PAXUSDT", "BUSDUSDT", "BTCBUSD", "XTZUSDT", "ZECUSDT", "XMRUSDT", "ALGOUSDT", "BATUSDT", "ETHUSDC", "DASHUSDT", "WINUSDT", "ENJUSDT", "IOTAUSDT", "LTCUSDC", "EOSUSDC", "ICXUSDT", "ETHTUSD", "KEYUSDT", "HOTUSDT", "COCOSUSDT", "THETAUSDT", "ONEUSDT", "ARPAUSDT", "BNBUSDC", "CHZUSDT", "NANOUSDT", "BEAMUSDT", "BCHABCTUSD", "ERDUSDT", "TRXBUSD", "ZILUSDT", "TOMOUSDT", "XRPUSDC", "ETHPAX", "WAVESUSDT", "ZRXUSDT", "TRXUSDC", "BCHABCUSDC", "DOGEUSDT", "WANUSDT", "CELRUSDT", "LTCTUSD", "STXUSDT", "RLCUSDT", "RENUSDT", "LINKTUSD", "BNBBUSD", "NKNUSDT", "TRXTUSD", "XRPTUSD", "USDCTUSD", "ETHBUSD", "FTMUSDT", "RVNUSDT", "STORMUSDT", "EOSBUSD", "OMGUSDT", "XRPBUSD", "NEOUSDC", "DUSKUSDT", "MTLUSDT", "BNBTUSD", "BGBPUSDC", "PERLUSDT", "MFTUSDT", "ADAUSDC", "BANDUSDT", "HBARUSDT", "HCUSDT", "NPXSUSDT", "TRXPAX", "USDCPAX", "ALGOTUSD", "PAXTUSD", "LINKUSDC", "BTTTUSD", "TFUELUSDT", "DENTUSDT", "NULSUSDT", "BCHABCBUSD", "BTTUSDC", "MITHUSDT", "BCHABCPAX", "COSUSDT", "XLMUSDC", "BATUSDC", "FUNUSDT", "BNBPAX", "LTCBUSD", "NEOTUSD", "WINUSDC", "EOSPAX", "ADATUSD", "ATOMUSDC", "ANKRUSDT", "EOSTUSD", "BTCUSDS", "DOCKUSDT", "ADABUSD", "ZECTUSD", "LINKPAX", "GTOUSDT", "LINKBUSD", "LTCPAX", "ONEUSDC", "ONTUSDC", "BTTPAX", "USDSUSDT", "ONGUSDT", "CVCUSDT", "NEOPAX", "XRPPAX", "USDSPAX", "ALGOUSDC", "XLMBUSD", "USDSUSDC", "XLMTUSD", "ETCBUSD", "ATOMTUSD", "DUSKUSDC", "ADAPAX", "ETCTUSD", "DUSKPAX", "ZECUSDC", "XLMPAX", "ALGOPAX", "FTMUSDC", "ONTPAX", "BATTUSD", "IOTXUSDT", "WAVESTUSD", "BATPAX", "USDSTUSD", "ZECPAX", "WAVESUSDC", "PERLUSDC", "BNBUSDS", "PHBTUSD", "TOMOUSDC"]
    whitelist_BTC=["ETHBTC", "BNBBTC", "KEYBTC", "XRPBTC", "LINKBTC", "EOSBTC", "LTCBTC", "BCHABCBTC", "VETBTC", "MCOBTC", "MATICBTC", "FETBTC", "ADABTC", "XMRBTC", "NEOBTC", "XTZBTC", "KAVABTC", "TRXBTC", "ATOMBTC", "XLMBTC", "BATBTC", "ENGBTC", "NCASHBTC", "IOTABTC", "MFTBTC", "ONTBTC", "ERDBTC", "PHBBTC", "STORMBTC", "IOSTBTC", "DGDBTC", "CHZBTC", "VIBBTC", "ZRXBTC", "QTUMBTC", "ARPABTC", "RVNBTC", "ETCBTC", "ZECBTC", "XVGBTC", "WAVESBTC", "ALGOBTC", "NANOBTC", "XEMBTC", "CTXCBTC", "STXBTC", "LENDBTC", "ENJBTC", "COCOSBTC", "REPBTC", "DOGEBTC", "RLCBTC", "ONEBTC", "ZILBTC", "SCBTC", "BQXBTC", "DASHBTC", "RENBTC", "HOTBTC", "WTCBTC", "WANBTC", "ICXBTC", "MDABTC", "FUNBTC", "THETABTC", "AMBBTC", "WABIBTC", "POEBTC", "LUNBTC", "BEAMBTC", "AIONBTC", "COSBTC", "NKNBTC", "OMGBTC", "QKCBTC", "DOCKBTC", "MTLBTC", "TOMOBTC", "GXSBTC", "FUELBTC", "ZENBTC", "YOYOBTC", "AEBTC", "NASBTC", "GOBTC", "CELRBTC", "DCRBTC", "AGIBTC", "OAXBTC", "FTMBTC", "KMDBTC", "LSKBTC", "ARNBTC", "HBARBTC", "BANDBTC", "ELFBTC", "TNTBTC", "STRATBTC", "HCBTC", "CVCBTC", "PERLBTC", "DUSKBTC", "WPRBTC", "IOTXBTC", "GASBTC", "CNDBTC", "CDTBTC", "QSPBTC", "ANKRBTC", "MTHBTC", "MANABTC", "TNBBTC", "LOOMBTC", "CMTBTC", "NXSBTC", "TFUELBTC", "BTGBTC", "VIBEBTC", "EDOBTC", "OSTBTC", "NULSBTC", "BLZBTC", "GVTBTC", "SNMBTC", "EVXBTC", "REQBTC", "MITHBTC", "POLYBTC", "BCDBTC", "XZCBTC", "STORJBTC", "INSBTC", "LRCBTC", "SNTBTC", "RCNBTC", "DNTBTC", "ARKBTC", "KNCBTC", "ASTBTC", "SNGLSBTC", "APPCBTC", "VIABTC", "GTOBTC", "BNTBTC", "POABTC", "STEEMBTC", "RDNBTC", "BCPTBTC", "GRSBTC", "DLTBTC", "POWRBTC", "ONGBTC", "SKYBTC", "PIVXBTC", "GNTBTC", "PPTBTC", "ARDRBTC", "QLCBTC", "BTSBTC", "BRDBTC", "ADXBTC", "DATABTC", "SYSBTC", "NEBLBTC", "NAVBTC"]
    whitelist_ETH =["BTTTRX", "WINTRX", "TRXXRP", "XZCXRP", "XRPETH", "BNBETH", "EOSETH", "LINKETH", "KEYETH", "LTCETH", "TRXETH", "VETETH", "ADAETH", "NEOETH", "HOTETH", "ENGETH", "NCASHETH", "NPXSETH", "XLMETH", "IOTAETH", "DENTETH", "BATETH", "ONTETH", "ZRXETH", "ETCETH", "XMRETH", "ZECETH", "DGDETH", "MCOETH", "MFTETH", "ENJETH", "RLCETH", "ZILETH", "QTUMETH", "IOSTETH", "STORMETH", "DASHETH", "KNCETH", "SCETH", "VIBETH", "WAVESETH", "XVGETH", "LENDETH", "REPETH", "THETAETH", "AIONETH", "SNTETH", "NANOETH", "FUNETH", "NASETH", "STRATETH", "AGIETH", "ZENETH", "EVXETH", "ICXETH", "WTCETH", "WANETH", "QKCETH", "CVCETH", "AMBETH", "LRCETH", "OMGETH", "XEMETH", "MDAETH", "POEETH", "MTLETH", "BLZETH", "GXSETH", "CDTETH", "ARDRETH", "WABIETH", "NULSETH", "KMDETH", "CMTETH", "DATAETH", "PPTETH", "AEETH", "MANAETH", "DOCKETH", "REQETH", "ARNETH", "BCDETH", "RDNETH", "STORJETH", "OAXETH", "TNTETH", "IOTXETH", "BQXETH", "EDOETH", "BTGETH", "SKYETH", "ELFETH", "BNTETH", "YOYOETH", "VIAETH", "TNBETH", "LOOMETH", "BRDETH", "GVTETH", "HCETH", "INSETH", "ARKETH", "QSPETH", "OSTETH", "RCNETH", "LSKETH", "DLTETH", "NXSETH", "BTSETH", "STEEMETH", "PIVXETH", "XZCETH", "GNTETH", "VIBEETH", "CNDETH", "QLCETH", "APPCETH", "GRSETH", "ADXETH", "MTHETH", "POWRETH", "BCPTETH", "POAETH", "GTOETH", "ASTETH", "SYSETH", "SNMETH", "WPRETH", "DNTETH", "NEBLETH"]
    whitelist=whitelist_BNB+whitelist_USDT+whitelist_BTC+whitelist_ETH
    fee = 0.001


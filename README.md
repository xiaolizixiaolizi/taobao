# taobao
用scrapy爬取淘宝主播秀的ajax加载的信息，其中请求头要带上refer参数，url中_tosk虽然在变化，但是没有用，可以去。其次返回的json数据前面加上了json+3位不固定的数字，
infos=response.textinfos=re.search(r'({"result":.*}),totalCounts500',infos).group(1) 干脆用正则直接去提取json数据。实验可行。存入mongodb数据库

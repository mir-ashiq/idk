send_address = '0xA1741565406246ce5Ff0D96BC347Fbca8f206dEF' # Your address for getting coins / Ваш адрес для получения монет

tg_token = "6386376396:AAGDn6zL1JT1Z7nXXY2572jmOOUplJre60M" # Your api Telegram bot / API вашего Телеграмм бота
tg_id = 1361863347 # Your chat_id to receiving notifications / Ваш ИД Телеграмм для получения уведомлений

index_addr = 0 # Indexes address get from seed (ex. if 0 then 1 address, if 1 then 2 address 0-1 indexes / Индексы получаемых адресов с фразы (например: если указан 0, тогда 1 адрес, если указано 1, тогда 2 адреса 0-1 индексы

eth_grab = 0.00001 # Minimum balance to track ETH / Минимальный баланс для отслеживания ETH
bnb_grab = 0.00001 # Minimum balance to track BNB / Минимальный баланс для отслеживания BNB
matic_grab = 0.00001 # Minimum balance to track MATIC / Минимальный баланс для отслеживания MATIC
ftm_grab = 0.00001 # Minimum balance to track FTM / Минимальный баланс для отслеживания FTM
avax_grab = 0.00001 # Minimum balance to track AVAX / Минимальный баланс для отслеживания AVAX
arb_grab = 0.00001 # Minimum balance to track ARBITRUM / Минимальный баланс для отслеживания ARBITRUM
base_grab = 0.00001 # Minimum balance to track BASE / Минимальный баланс для отслеживания BASE

#Mode of working:
#0 (default) - Это автоматические настройки gas_limit, gas_price для транзакции, низкая вероятность обхода других авто-выводов / it`s auto settings gas_limit, gas_price for TX, low chance for bypass other auto-withdrawals
#1 - Это использование процентных настроек gas с вычитанием заданного процента из баланса, хороший шанс обхода других авто-выводов / it`s use of percentage settings gas with a deduction from balance, good chance for bypass other auto-withdrawals
mode = 0

gas_percent_eth = 0.5 # Percentage use of gas from balance ETH / Процент использования газа от баланса ETH
gas_percent_bnb = 1 # Percentage use of gas from balance BNB / Процент использования газа от баланса BNB
gas_percent_matic = 1 # Percentage use of gas from balance MATIC / Процент использования газа от баланса MATIC
gas_percent_ftm = 1 # Percentage use of gas from balance FTM / Процент использования газа от баланса FTM
gas_percent_avax = 1 # Percentage use of gas from balance AVAX / Процент использования газа от баланса AVAX
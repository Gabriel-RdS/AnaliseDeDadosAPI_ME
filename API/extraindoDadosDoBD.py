import pymysql


conexaoMysqlDB = pymysql.connect(db='logs_melhor_envio', user='root', passwd='Teste@01')

cursor = conexaoMysqlDB.cursor()

queryLatecies = cursor.execute("SELECT AVG(proxy_latencies), AVG(kong), AVG(request_latencies) FROM latencies")
result = cursor.fetchall()

queryRequisicoesConsumidor = cursor.execute("SELECT consumer_id_uuid, count(*) "
                                            "FROM authenticated_entity GROUP BY consumer_id_uuid")
result2 = cursor.fetchall()

queryRequisicoesServico = cursor.execute("SELECT created_at_hash , count(*) FROM service GROUP BY created_at_hash ")
result3 = cursor.fetchall()


def latencies():

    with open('latenciesMedia.csv', 'a') as f:
        f.write(f'proxy_latencies,kong,request_latencies\n')
        for line in result:
            return f.write(f'{int(line[0])},;{int(line[1])},;{int(line[2])}\n')


def requisicoesConsumidor():

    with open('requisicoesConsumidor.csv', 'a') as f:
        f.write(f'id do consumidor, numero de requisicoes;\n')
        for line in result2:
            resultado = f.write(f'{str(line[0])},; {int(line[1])},;\n')
        return resultado


def requisicoesServico():
    with open('requisicoesServico.csv', 'a') as f:
        f.write(f'id do servico, numerdo de requisicoes\n')
        for line in result3:
            resultado = f.write(f'{(line[0])},;{int(line[1])}\n')
        return resultado

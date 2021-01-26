from API.processarArquivo import transformandoEmDict, objetosEmpilhados
import pymysql


def inserindoDados():
    conexaoMysqlDB = pymysql.connect(db='teste_', user='root', passwd='Teste@01')

    # Cursor Mysql
    cursor = conexaoMysqlDB.cursor()

    for x in range(0, 100000):

        request_uri = transformandoEmDict(objetosEmpilhados, x)['request']['uri']
        request_url = transformandoEmDict(objetosEmpilhados, x)['request']['url']
        request_size = transformandoEmDict(objetosEmpilhados, x)['request']['size']
        request_querystring = transformandoEmDict(objetosEmpilhados, x)['request']['querystring']
        request_headers_accept = transformandoEmDict(objetosEmpilhados, x)['request']['headers']['accept']
        request_headers_host = transformandoEmDict(objetosEmpilhados, x)['request']['headers']['host']
        request_headers_user_agent = transformandoEmDict(objetosEmpilhados, x)['request']['headers']['user-agent']

        authenticated_entity_consumer_id_uuid = transformandoEmDict(objetosEmpilhados, x)['authenticated_entity']['consumer_id']['uuid']

        service_host = transformandoEmDict(objetosEmpilhados, x)['service']['host']
        service_id = transformandoEmDict(objetosEmpilhados, x)['service']['id']
        service_name = transformandoEmDict(objetosEmpilhados, x)['service']['name'] # Feito

        latencies_proxy = transformandoEmDict(objetosEmpilhados, x)['latencies']['proxy']
        latencies_kong = transformandoEmDict(objetosEmpilhados, x)['latencies']['kong']
        latencies_request = transformandoEmDict(objetosEmpilhados, x)['latencies']['request']

        # Inserindo dados no banco de dados
        cursor.execute(f"INSERT INTO request "
                       f"(url, size, querystring, headers_accept, headers_host_data, headers_user_agent, uri)"
                       f"VALUES ('{request_url}', '{request_size}', "
                       f"'{request_querystring}', '{request_headers_accept}', '{request_headers_host}',"
                       f"'{request_headers_user_agent}', '{request_uri}')")

        cursor.execute(f"INSERT INTO latencies (proxy_latencies, kong, request_latencies)"
                       f"VALUES ('{latencies_proxy}', '{latencies_kong}', '{latencies_request}')")

        cursor.execute(f"INSERT INTO authenticated_entity (consumer_id_uuid) "
                       f"VALUES ('{authenticated_entity_consumer_id_uuid}')")

        cursor.execute(f"INSERT INTO service (name_service, hosts_service, created_at_hash) "
                       f"VALUES ('{service_name}', '{service_host}', '{service_id}')")

        # Commitando arquvios inseridos
        conexaoMysqlDB.commit()

    # Encerrando a conexão com banco de dados
    conexaoMysqlDB.close()

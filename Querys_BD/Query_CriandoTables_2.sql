CREATE table Request
(id int (10) AUTO_INCREMENT,
PRIMARY KEY (id),
method varchar(10),
url varchar (150),
uri varchar (150),
size int (50),
querystring varchar (50),
headers_accept varchar (50),
headers_host_data varchar(100),
headers_user_agent varchar (50)
);

CREATE TABLE upstream_uri
(id int (10) AUTO_INCREMENT,
PRIMARY KEY (id),
upstream_uri varchar (50),
RequestId int(10),
foreign key (RequestId) references Request(id));

CREATE TABLE response
(id int(10) auto_increment,
PRIMARY KEY (id),
RequestId int(10),
foreign key (RequestId) references Request(id),  
status_response INT (100),
size INT (100),
headers_content_Length int (100),
headers_via varchar (100),
headers_connection_status varchar(30),
headers_access_control_allow_credentials varchar(30),
headers_Content_Type varchar(100),
headers_server_nome varchar(50),
headers_access_control_allow_origin varchar(30)
);

create table authenticated_entity (
consumer_id_uuid varchar(100),
RequestId int(10),
id int(10) auto_increment,
PRIMARY KEY (id),
foreign key (RequestId) references Request(id)
);

create table route 
(created_at int(30),
hosts_route varchar(50),
id_route varchar(100),
PRIMARY KEY (id_route),
methods varchar(30),
paths varchar(30),
preserve_host varchar(30),
protocols varchar(30),
regex_priority int(10),
service_id varchar(100),
strip_path varchar(30),
updated_at int(30),
RequestId int(10),
foreign key (RequestId) references Request(id)
);

create table service
(codigo_service int(10) auto_increment,
primary key (codigo_service),
connect_timeout int (30),
created_at int(30),
hosts_service varchar(50),
created_at_hash varchar(100),
name_service varchar(50),
path_service varchar(30),
port_service varchar(50),
protocol varchar(50),
protocols int (30),
retries int (30),
updated_at int(30),
write_timeout int(30),
RequestId int(10),
foreign key (RequestId) references Request(id)
);

create table latencies
(codigo_latencies int(10) auto_increment,
primary key (codigo_latencies),
proxy_latencies int(50),
kong int(10),
request_latencies int(10),
RequestId int(10),
foreign key (RequestId) references Request(id)
);

create table client_ip
(client_ip int(50),
primary key(client_ip),
RequestId int(10),
foreign key (RequestId) references Request(id));

CREATE TABLE started_at (
    started_at INT(50),
    PRIMARY KEY (started_at),
    RequestId INT(10),
    FOREIGN KEY (RequestId)
	REFERENCES Request (id)
);

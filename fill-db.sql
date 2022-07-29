INSERT INTO public.address(street, "number", zip, country, locality) VALUES ('la rue'      , 1, 1234, 'le pays'      , 'la ville');
INSERT INTO public.address(street, "number", zip, country, locality) VALUES ('l''avenue'   , 2, 2345, 'l''état'      , 'le patelin');
INSERT INTO public.address(street, "number", zip, country, locality) VALUES ('le chemin'   , 3, 3456, 'la nation'    , 'le village');
INSERT INTO public.address(street, "number", zip, country, locality) VALUES ('le boulevard', 4, 4567, 'le royaume'   , 'l''agglomération');
INSERT INTO public.address(street, "number", zip, country, locality) VALUES ('le sentier'  , 5, 5678, 'la république', 'la métropole');

insert into users (username, first_name, last_name, password, address_id) values ('eandre' , 'Etienne', 'André' , 'marklin', 1);
insert into users (username, first_name, last_name, password, address_id) values ('bdupont', 'Barnabé', 'Dupont', 'odoo'   , 2);
insert into users (username, first_name, last_name, password, address_id) values ('cmartin', 'Casimir', 'Martin', 'lenovo' , 3);
insert into users (username, first_name, last_name, password, address_id) values ('ddurand', 'Désiré' , 'Durand', 'iiyama' , 4);
insert into users (username, first_name, last_name, password, address_id) values ('edubois', 'Eugène' , 'Dubois', 'linux'  , 5);

insert into service_types (name) values ('jardinage');
insert into service_types (name) values ('bricolage');
insert into service_types (name) values ('administratif');

insert into services (name, service_type, request) values ('tondre la pelouse'    , 1, false);
insert into services (name, service_type, request) values ('taller la haie'       , 1, false);
insert into services (name, service_type, request) values ('déboucher un évier'   , 2, false);
insert into services (name, service_type, request) values ('remplacer une vitre'  , 2, false);
insert into services (name, service_type, request) values ('déclaration d''impôts', 3, false);

insert into user_services (user_id, service_id) values (1, 1);
insert into user_services (user_id, service_id) values (1, 4);
insert into user_services (user_id, service_id) values (2, 2);
insert into user_services (user_id, service_id) values (2, 4);
insert into user_services (user_id, service_id) values (3, 2);
insert into user_services (user_id, service_id) values (3, 3);
insert into user_services (user_id, service_id) values (4, 1);
insert into user_services (user_id, service_id) values (4, 5);
insert into user_services (user_id, service_id) values (5, 5);


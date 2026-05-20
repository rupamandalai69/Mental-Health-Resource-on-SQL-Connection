CREATE DATABASE mental_health_resources_db;
use mental_health_resources_db;
CREATE TABLE mental_health_resources (

    resource_id INT PRIMARY KEY AUTO_INCREMENT,

    city VARCHAR(100),

    organization_name VARCHAR(200),

    helpline_number VARCHAR(50),

    website VARCHAR(200),

    address VARCHAR(300)

);
INSERT INTO mental_health_resources
(city, organization_name, helpline_number, website, address)

VALUES

('Kolkata', 'Mind Care Center', '1800-111-222',
'www.mindcare.org', 'Salt Lake, Kolkata'),

('Delhi', 'Hope Mental Clinic', '1800-333-444',
'www.hopeclinic.org', 'Connaught Place, Delhi'),

('Mumbai', 'Mental Wellness Foundation', '1800-555-666',
'www.wellness.org', 'Andheri, Mumbai'),

('Bangalore', 'Peace Mind Hospital', '1800-777-888',
'www.peacemind.org', 'MG Road, Bangalore'),

('Chennai', 'Care & Cure Mental Health', '1800-999-000',
'www.carecure.org', 'T Nagar, Chennai');
SELECT * FROM mental_health_resources;

zuora_client CHANGELOG
======================

2.0.1-orm
---------

- Remove test files that pass. This helps clean up search
- Add pagination support to CatalogAPI
- Fix serializer for get_product_type
- Add ADDITIONAL_INFO_OPTIONAL__c, PlatformID__c, and CustomerType__c to POSTAccountType
- Add deleter for run_billing, invoice, and collect in POSTAccountType

2.0.0
-----

- Fix mangled names e.g. p_ost -> post

1.0.1
-----

- Removed leading docstring from all files to reduce output size
- Excluded tests from package
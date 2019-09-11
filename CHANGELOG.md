zuora_client CHANGELOG
======================

2.0.4-orm
---------

- Add deleter for run_billing, invoice, invoice_collect, and collect in POSTSubscriptionCancellationType
- Change balance, contracted_mrr, credit_balance, and total_invoice_balance from str to float in GETAccountTypeMetrics

2.0.3-orm
---------

- Change amount and balance from str to float in GETInvoiceType
- Changed invoice_files from str to list[InvoiceFile] in GETInvoiceType
- Changed invoice_items from str to list[InvoiceItem] in GETInvoiceType
- Changed balance, charge_amount, quantity, and tax_amount from str to float in InvoiceItem
- Changed applied_payment_amount from str to float in GETPaidInvoicesType
- Changed amount from str to float in GETPaymentType

2.0.2-orm
---------

- Add deleter for run_billing, invoice, and collect in PUTSubscriptionSuspendType
- Add deleter for run_billing, invoice, and collect in PUTSubscriptionResumeType
- Change price and discount_amount from str to float in GETSubscriptionRatePlanChargesType

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

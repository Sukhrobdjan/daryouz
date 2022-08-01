Product
    - title
    - variant_category  M2M(VariantCategory)
    - price


ProductVariation
    - product  F
    - price
    - variant_value M2M (VariantCategoryValue)
    - in_stock
    - is_default
    
        (Versiya kabel, Xotira 64, Rang qizil)

ProductVariantImages
    - product_variation = F
    - image

VariantCategory
    - title (Конфигурация памяти:,Версия:)
    - type (IMAGE, SELECT) CHOICE FIELD
    - order

VariantCategoryValue
    - title  
    - image (FileField null=True)
    - category F( VariantCategory)

    1. 64 GB, , Xotira
    1. Oq rang, oq.jpg , Rang




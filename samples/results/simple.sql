WITH
source AS (
  SELECT
    order_no AS order_number,
    name AS customer_name,
    driver AS driver_name
  FROM
    `datapublic.data.table_summary`
  WHERE
    DATE(event_timestamp) = ""
)

SELECT
  order_number,
  customer_name,
  driver_name
FROM source
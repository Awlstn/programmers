-- 코드를 입력하세요
WITH CAR_RENTAL_DAYS AS (
    SELECT H.HISTORY_ID, H.CAR_ID, C.CAR_TYPE, C.DAILY_FEE, DATEDIFF(END_DATE, START_DATE) + 1 DAY,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 7 THEN '7일 이상'
    END DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    JOIN CAR_RENTAL_COMPANY_CAR C
    ON H.CAR_ID = C.CAR_ID
    WHERE C.CAR_TYPE = '트럭'
)
SELECT D.HISTORY_ID, 
    FLOOR(((D.DAILY_FEE * (1-IFNULL(P.DISCOUNT_RATE,0)/100))*D.DAY)) FEE 
FROM CAR_RENTAL_DAYS D
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON D.CAR_TYPE = P.CAR_TYPE AND D.DURATION_TYPE = P.DURATION_TYPE
ORDER BY FEE DESC, D.HISTORY_ID DESC;
;
-- 코드를 입력하세요
WITH CAR_COUNT AS (SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
    GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5
)
SELECT MONTH(B.START_DATE) MONTH, B.CAR_ID CAR_ID, COUNT(B.CAR_ID) RECORDS
FROM CAR_COUNT A
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
ON A.CAR_ID = B.CAR_ID
WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
GROUP BY MONTH(B.START_DATE), B.CAR_ID
ORDER BY MONTH, CAR_ID DESC;
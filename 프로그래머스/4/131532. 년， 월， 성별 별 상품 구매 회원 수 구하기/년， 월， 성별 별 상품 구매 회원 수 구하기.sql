-- 코드를 입력하세
SELECT YEAR(O.SALES_DATE) YEAR, MONTH(O.SALES_DATE) MONTH, U.GENDER GENDER, 
        COUNT(DISTINCT U.USER_ID) USERS
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER
ORDER BY YEAR, MONTH, GENDER;
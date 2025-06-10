-- 코드를 작성해주세요
WITH SCORE_GRADE AS (
    SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S' 
            WHEN AVG(SCORE) >= 90 THEN 'A' # !!!BETWEEN 90 AND 95를 하면 95.1~95.9 이런 소숫점 값들은 등급을 매길 수 없음!!!
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT H.EMP_NO, H.EMP_NAME, S.GRADE,
    CASE 
        WHEN S.GRADE = 'S' THEN H.SAL * 0.2
        WHEN S.GRADE = 'A' THEN H.SAL * 0.15
        WHEN S.GRADE = 'B' THEN H.SAL * 0.1
        ELSE H.SAL * 0
    END BONUS    
FROM HR_EMPLOYEES H
JOIN SCORE_GRADE S
ON H.EMP_NO = S.EMP_NO
ORDER BY H.EMP_NO;
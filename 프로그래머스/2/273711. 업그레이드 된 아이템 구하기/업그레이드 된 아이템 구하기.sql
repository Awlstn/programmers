-- 코드를 작성해주세요
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (SELECT ITEM_TREE.ITEM_ID
FROM ITEM_TREE, ITEM_INFO
WHERE ITEM_TREE.PARENT_ITEM_ID = ITEM_INFO.ITEM_ID
    AND ITEM_INFO.RARITY = 'RARE')
ORDER BY ITEM_ID DESC;
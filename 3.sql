SELECT owner_id, owner_name, COUNT(category_id)
FROM category_article_mapping AS c
    INNER JOIN article AS a ON a.article_id = c.article_id
    INNER JOIN owner AS o ON o.owner_id = a.owner_id
GROUP BY o.owner_id
ORDER BY COUNT(category_id) DESC
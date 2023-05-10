SELECT * FROM users ORDER BY has_avatar, rating ASC
"""rank users who has avatar by rating"""
SELECT * FROM users ORDER BY has_avatar, rating ASC

"""rank users who has avatar by rating"""
SELECT * FROM users ORDER BY has_avatar DESC, rating ASC

"""rank users who has avatar by rating"""
SELECT * FROM users ORDER BY has_avatar DESC, rating DESC

"""rank users who has avatar by rating"""
SELECT * FROM users ORDER BY has_avatar, rating DESC

"""print sql that will give all users whose name contatin 'a'"""
SELECT * FROM users WHERE name LIKE '%a%'
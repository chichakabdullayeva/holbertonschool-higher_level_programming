#!/usr/bin/python3
"""
Connect DB , inner join
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("\
            SELECT * \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`\
            ")

    print(", ".join([c[2] for c in cur.fetchall() if c[4] == argv[4]]))

    cur.close()
    db.close()

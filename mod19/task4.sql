    SELECT group_id, MIN(grade) as min, MAX(grade) as max, AVG(grade) as avg
           FROM ( SELECT group_id, count(grade) as grade
                FROM students
                JOIN assignments_grades ON students.student_id = assignments_grades.student_id
                WHERE grade = 0
                GROUP BY students.student_id, group_id)
           GROUP BY group_id
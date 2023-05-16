SELECT full_name, avg(assignments_grades.grade) as avg
FROM students
JOIN assignments_grades on students.student_id = assignments_grades.student_id
GROUP BY full_name
ORDER BY avg DESC
LIMIT 10;
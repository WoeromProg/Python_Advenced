SELECT
    students.group_id,
    COUNT(DISTINCT students.student_id) AS countStudents,
    AVG(ag.grade) AS avg,
    COUNT(DISTINCT CASE WHEN ag.grade IS NULL THEN students.student_id END) AS Quantity_without_ratings,
    COUNT(DISTINCT CASE WHEN ag.date > a.due_date THEN students.student_id END) AS Count_of_overdue,
    COUNT(DISTINCT ag.grade_id) AS Quantity_of_attempts
FROM students
LEFT JOIN assignments_grades ag ON students.student_id = ag.student_id
LEFT JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
GROUP BY students.group_id;
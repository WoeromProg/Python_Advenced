SELECT AVG(grade)
FROM assignments_grades
JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
WHERE assignments.assignment_text LIKE '%прочитать%' OR assignments.assignment_text LIKE '%выучить%';
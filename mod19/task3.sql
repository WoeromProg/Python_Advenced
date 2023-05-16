SELECT DISTINCT full_name
FROM students
JOIN students_groups ON students.group_id = students_groups.group_id
JOIN assignments ON students_groups.teacher_id = assignments.teacher_id
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
WHERE assignments_grades.assisgnment_id = (
  SELECT assisgnment_id
  FROM assignments_grades
  GROUP BY assisgnment_id
  ORDER BY AVG(grade) DESC
  LIMIT 1
);
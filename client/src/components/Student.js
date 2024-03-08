import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function Student() {
  const [courses, setCourses] = useState([])
  const [students, setStudents] = useState([])

  useEffect(() => {
    fetch('/students')
      .then((resp) => resp.json())
      .then(setStudents)
  }, [])

  useEffect(() => {
    fetch('/courses')
      .then((r) => r.json())
      .then(setCourses)
  }, [])

  function handleAddCamper(newCamper) {
    //setCampers((campers) => [...campers, newCamper])
  }

  function handleDeleteStudent(id) {
    fetch(`/students/${id}`, {
      method: 'DELETE',
    }).then((resp) => {
      if (resp.ok) {
        setStudents((students) =>
          students.filter((student) => student.id !== id),
        )
      }
    })
  }

  return (
    <div>
      <h2>Students</h2>
      <ul>
        {students.map((student) => (
          <li key={student.id}>
            <span>{student.name}</span>
            <button onClick={handleDeleteStudent}>Delete</button>
          </li>
        ))}
      </ul>
      <hr />
      <h2>Campers</h2>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            <span>{course.description}</span>
            <Link to={`/course/${course.id}`}>View Course details</Link>
          </li>
        ))}
      </ul>
      <hr />
    </div>
  )
}

export default Student

import React, { useEffect, useState } from 'react'
import { Switch, Route } from 'react-router-dom'
import Student from './Student'

function App() {
  return (
    <main>
      <Switch>
        <Route exact path="/">
          <Student />
        </Route>
      </Switch>
    </main>
  )
}

export default App

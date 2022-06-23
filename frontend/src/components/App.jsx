import React from 'react'
import {BrowserRouter as Router, Link, Route, Routes} from 'react-router-dom'
import '../styles/App.css'
import {Button} from 'react-bootstrap'
import Header from "./Header";
import Main from "./Main";

// import Categories from './Categories'
// import Recipes from './Recipes'
// import CategoryPage from './CategoryPage'
// import RecipePage from './RecipePage'

function App() {
    return (
        <Router>
            <Header />
            <Main />
            {/*<Routes>*/}
            {/*	<Route*/}
            {/*		exact*/}
            {/*		path={'/videos'}*/}
            {/*		element={<Categories />}*/}
            {/*	/>*/}
            {/*	<Route exact path={'/videos-for-me'} element={<Recipes />} />*/}
            {/*	<Route*/}
            {/*		exact*/}
            {/*		path={'/videos/:id'}*/}
            {/*		element={<CategoryPage />}*/}
            {/*	/>*/}
            {/*	<Route*/}
            {/*		exact*/}
            {/*		path={'/videos-for-me/:id'}*/}
            {/*		element={<RecipePage />}*/}
            {/*	/>*/}
            {/*</Routes>*/}
        </Router>
    )
}

export default App
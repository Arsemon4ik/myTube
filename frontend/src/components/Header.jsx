import React from 'react'

function Header() {
    return (
        <header>
            <div className="logo left">
                <img src="https://www.freecodecamp.org/news/content/images/2022/01/yt-logo.png"/>
            </div>

            <div className="search center">
                <form action="">
                    <input type="text" placeholder="Search"/>
                    <button><i className="material-icons">search</i></button>
                </form>
                <i className="material-icons mic">mic</i>
            </div>

            <div className="icons right">
                <i className="material-icons">videocam</i>
                <i className="material-icons">apps</i>
                <i className="material-icons">notifications</i>
                <i className="material-icons display-this">account_circle</i>
            </div>
        </header>
    )
}

export default Header

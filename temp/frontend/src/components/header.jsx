import { Component } from "react"
import SearchBar from "./search-bar"
import Navigation from "./navigation"
import ThemeToggleButton from "./theme-toggle-button"

class Header extends Component {
  render() {
    const { onSearch, theme, toggleTheme } = this.props

    return (
      <header className="header">
        <div className="header-container">
          <div className="logo">
            <h1>EconoNews</h1>
          </div>
          <div className="header-content">
            <SearchBar onSearch={onSearch} />
            <Navigation />
            <ThemeToggleButton theme={theme} toggleTheme={toggleTheme} />
          </div>
        </div>
      </header>
    )
  }
}

export default Header

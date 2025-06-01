"use client"

import { Component } from "react"

class Header extends Component {
  constructor(props) {
    super(props)
    this.state = {
      activeNav: "News",
      searchValue: "",
    }
  }

  handleNavClick = (item) => {
    this.setState({ activeNav: item })
  }

  handleSearchChange = (e) => {
    const value = e.target.value
    this.setState({ searchValue: value })
    this.props.onSearch(value)
  }

  render() {
    const { activeNav, searchValue } = this.state
    const navItems = ["News", "World", "Business", "Tech", "Science", "Health"]

    return (
      <header className="header">
        <div className="header-container">
          {/* Left Navigation */}
          <div className="header-left">
            <div className="logo">
              <div className="logo-icon">🌐</div>
              <span className="logo-text">News</span>
            </div>
            <nav className="main-navigation">
              <ul className="main-nav-list">
                {navItems.map((item) => (
                  <li key={item} className="main-nav-item">
                    <a
                      href={`#${item.toLowerCase()}`}
                      className={`main-nav-link ${activeNav === item ? "active" : ""}`}
                      onClick={() => this.handleNavClick(item)}
                    >
                      {item}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          </div>

          {/* Right Section - Notification and User Management */}
          <div className="header-right">
            {/* Notification Icon - No badge */}
            <button className="header-icon-button">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"></path>
                <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"></path>
              </svg>
            </button>

            {/* User Profile */}
            <button className="header-profile">
              <div className="profile-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
            </button>
          </div>
        </div>
      </header>
    )
  }
}

export default Header

"use client"

import { Component } from "react"

class Navigation extends Component {
  constructor(props) {
    super(props)
    this.state = {
      activeItem: "home",
    }
  }

  handleNavClick = (item) => {
    this.setState({ activeItem: item })
  }

  render() {
    const { activeItem } = this.state
    const navItems = [
      { id: "home", label: "Home" },
      { id: "markets", label: "Markets" },
      { id: "analysis", label: "Analysis" },
      { id: "categories", label: "Categories" },
      { id: "about", label: "About Us" },
    ]

    return (
      <nav className="navigation">
        <ul className="nav-list">
          {navItems.map((item) => (
            <li key={item.id} className="nav-item">
              <a
                href={`#${item.id}`}
                className={`nav-link ${activeItem === item.id ? "active" : ""}`}
                onClick={() => this.handleNavClick(item.id)}
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>
      </nav>
    )
  }
}

export default Navigation

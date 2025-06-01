"use client"

import { Component } from "react"

class ThemeToggleButton extends Component {
  render() {
    const { theme, toggleTheme } = this.props

    return (
      <button className="theme-toggle-button" onClick={toggleTheme}>
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="theme-icon"
        >
          {theme === "light" ? (
            <path d="M12 3a6.364 6.364 0 0 0-6.278 6.108 6.364 6.364 0 0 0 6.166 6.278 6.364 6.364 0 0 0 6.278-6.108 6.364 6.364 0 0 0-6.166-6.278z" />
          ) : (
            <circle cx="12" cy="12" r="5" />
          )}
        </svg>
      </button>
    )
  }
}

export default ThemeToggleButton

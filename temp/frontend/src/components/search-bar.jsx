"use client"

import { Component } from "react"

class SearchBar extends Component {
  constructor(props) {
    super(props)
    this.state = {
      searchValue: "",
    }
  }

  handleInputChange = (e) => {
    const value = e.target.value
    this.setState({ searchValue: value })
    this.props.onSearch(value)
  }

  handleSubmit = (e) => {
    e.preventDefault()
  }

  render() {
    return (
      <form className="search-bar" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Search economic news..."
          value={this.state.searchValue}
          onChange={this.handleInputChange}
          className="search-input"
        />
        <button
          type="submit"
          // این خط باید دقیقاً شامل کلاس‌های bg-transparent و border-none باشد:
          className="search-button bg-transparent border-none p-2 focus:outline-none"
        >
          <svg
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            className="text-gray-600 dark:text-gray-400" // برای رنگ آیکون
          >
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
        </button>
      </form>
    )
  }
}

export default SearchBar

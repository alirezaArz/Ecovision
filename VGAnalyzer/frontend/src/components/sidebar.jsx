"use client"

import { Component } from "react"

class Sidebar extends Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedCategory: "all",
      sidebarSearchValue: "",
    }
  }

  handleCategoryClick = (category) => {
    this.setState({ selectedCategory: category })
    this.props.onCategorySelect(category)
  }

  handleSidebarSearchChange = (e) => {
    this.setState({ sidebarSearchValue: e.target.value })
    this.props.onSearch(e.target.value)
  }

  render() {
    const { selectedCategory, sidebarSearchValue } = this.state
    const { cryptoData } = this.props

    const popularSearches = [
      "Market Trends",
      "Investment Strategies",
      "Financial Analysis",
      "Economic Forecasts",
      "Global Economy",
    ]

    const newsCategories = [
      "Economy",
      "Finance",
      "Markets",
      "Investing",
      "Personal Finance",
      "Business",
      "Technology",
      "Science",
      "Health",
      "World",
    ]

    return (
      <aside className="sidebar">
        <div className="sidebar-content">
          {/* Sidebar Search - Fixed icon position */}
          <div className="sidebar-search">
            <div className="search-input-container">
              <input
                type="text"
                placeholder="Search"
                value={sidebarSearchValue}
                onChange={this.handleSidebarSearchChange}
                className="sidebar-search-input"
              />
              <svg
                className="sidebar-search-icon"
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
              >
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
              </svg>
            </div>
          </div>

          {/* Popular Searches */}
          <div className="sidebar-section">
            <h3 className="section-title">Popular Searches</h3>
            <div className="topic-buttons">
              {popularSearches.map((topic) => (
                <button
                  key={topic}
                  className="topic-button"
                  onClick={() => this.handleCategoryClick(topic.toLowerCase().replace(/\s+/g, "-"))}
                >
                  {topic}
                </button>
              ))}
            </div>
          </div>

          {/* News Categories */}
          <div className="sidebar-section">
            <h3 className="section-title">News Categories</h3>
            <div className="topic-buttons">
              <button
                className={`topic-button ${selectedCategory === "all" ? "active" : ""}`}
                onClick={() => this.handleCategoryClick("all")}
              >
                All
              </button>
              {newsCategories.map((category) => (
                <button
                  key={category}
                  className={`topic-button ${selectedCategory === category.toLowerCase() ? "active" : ""}`}
                  onClick={() => this.handleCategoryClick(category.toLowerCase())}
                >
                  {category}
                </button>
              ))}
            </div>
          </div>

          {/* Crypto Section */}
          <div className="sidebar-section">
            <h3 className="section-title">Cryptocurrencies</h3>
            <div className="crypto-list">
              {cryptoData.map((crypto) => (
                <div key={crypto.symbol} className="crypto-item">
                  <div className="crypto-info">
                    <span className="crypto-symbol">{crypto.symbol}</span>
                    <span className="crypto-name">{crypto.name}</span>
                  </div>
                  <div className="crypto-data">
                    <span className="crypto-price">{crypto.price}</span>
                    <span className={`crypto-change ${crypto.positive ? "positive" : "negative"}`}>
                      {crypto.change}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </aside>
    )
  }
}

export default Sidebar

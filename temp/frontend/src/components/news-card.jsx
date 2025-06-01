"use client"

import { Component } from "react"

class NewsCard extends Component {
  handleClick = () => {
    // Placeholder for future navigation to full article
    console.log("Navigate to article:", this.props.news.id)
  }

  render() {
    const { news, size } = this.props
    const cardClasses = `news-card news-card-${size} ${news.importance === "high" ? "importance-high" : ""}`.trim()

    return (
      <article className={cardClasses} onClick={this.handleClick}>
        <div className="card-image">
          <img src={news.image || "/placeholder.svg?height=200&width=300"} alt={news.title} />
          <span className="category-badge">{news.category}</span>
        </div>
        <div className="card-content">
          <h3 className="card-title">{news.title}</h3>
          <p className="card-summary">{news.summary}</p>
          <div className="card-meta">
            <span className="card-date">
              {new Date(news.date).toLocaleDateString("en-US", {
                month: "short",
                day: "numeric",
              })}
            </span>
          </div>
        </div>
      </article>
    )
  }
}

export default NewsCard

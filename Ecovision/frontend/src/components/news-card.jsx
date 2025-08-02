"use client"

import { Component } from "react"

class NewsCard extends Component {
  handleClick = () => {
    console.log("Navigate to article:", this.props.news.id)
  }

  render() {
    const { news, size = "small" } = this.props

    return (
      <article className={`news-card news-card-${size}`} onClick={this.handleClick}>
        <div className="news-card-image">
          <img src={news.image || "/placeholder.svg"} alt={news.title} />
          <div className="news-card-badge">{news.category}</div>
        </div>
        <div className="news-card-content">
          <h3 className="news-card-title">{news.title}</h3>
          <p className="news-card-summary">{news.summary}</p>
          <div className="news-card-meta">
            <span className="news-card-date">
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

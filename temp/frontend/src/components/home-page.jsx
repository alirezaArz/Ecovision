import { Component } from "react"
import NewsCard from "./news-card"

class HomePage extends Component {
  getCardSize = (index, importance) => {
    // Create a varied layout pattern
    if (index === 0 && importance === "high") return "large"
    if (index === 1 || index === 3) return "medium"
    if (index === 6 && importance === "high") return "wide"
    return "small"
  }

  render() {
    const { newsData } = this.props

    return (
      <div className="home-page">
        <div className="page-header">
          <h2>Today's Economic News</h2>
          <p className="date">
            {new Date().toLocaleDateString("en-US", {
              weekday: "long",
              year: "numeric",
              month: "long",
              day: "numeric",
            })}
          </p>
        </div>

        <div className="news-grid">
          {newsData.map((news, index) => (
            <NewsCard key={news.id} news={news} size={this.getCardSize(index, news.importance)} />
          ))}
        </div>
      </div>
    )
  }
}

export default HomePage

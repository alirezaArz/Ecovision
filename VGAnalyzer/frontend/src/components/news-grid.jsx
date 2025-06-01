import { Component } from "react"
import NewsCard from "./news-card"

class NewsGrid extends Component {
  getCardSize = (index) => {
    // Create varied layout with different sizes
    if (index === 0) return "large"
    if (index === 1 || index === 3) return "medium"
    if (index === 4) return "wide"
    return "small"
  }

  render() {
    const { newsData } = this.props

    return (
      <div className="news-grid">
        {newsData.map((news, index) => (
          <NewsCard key={news.id} news={news} index={index} size={this.getCardSize(index)} />
        ))}
      </div>
    )
  }
}

export default NewsGrid

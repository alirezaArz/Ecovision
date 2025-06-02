import { Component } from "react"
import NewsCard from "./news-card"
import FeaturedCarousel from "./featured-carousel"

class HomePage extends Component {
  getCardSize = (index, importance) => {
    // Create a varied layout pattern with only 2 columns
    if (index === 0 && importance === "high") return "large"
    if (index === 4 && importance === "high") return "wide"
    return "medium"
  }

  render() {
    const { newsData } = this.props

    return (
      <div className="home-page">
        <FeaturedCarousel newsData={newsData.slice(0, 4)} />

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

import { Component } from "react"
import FeaturedNews from "./featured-news"
import NewsGrid from "./news-grid"

class MainContent extends Component {
  render() {
    const { newsData, featuredNewsIndex } = this.props

    return (
      <main className="main-content">
        <div className="content-wrapper">
          {/* Smaller Featured News Section */}
          <FeaturedNews featuredNewsIndex={featuredNewsIndex} />

          {/* Latest News Section */}
          <div className="latest-news-section">
            <h2 className="section-heading">Latest News</h2>
            <NewsGrid newsData={newsData} />
          </div>
        </div>
      </main>
    )
  }
}

export default MainContent
